import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from UI.lobbystudent import Ui_Form
from popUpDialog import popUpDialog
from studentMain import StudentMain

from Student import Student
from ClientSocket import ClientSocket
import constant

import socket
import sys
import struct
import pickle
import traceback
from threading import Thread


class StudentLobby(QtWidgets.QMainWindow):
    join_room_success = QtCore.pyqtSignal(list)
    kicked = QtCore.pyqtSignal(str)
    join_room_failed = QtCore.pyqtSignal(str)
    student_list_updated = QtCore.pyqtSignal(list)
    room_closed = QtCore.pyqtSignal(str)
    refresh_materials = QtCore.pyqtSignal(list)

    on_lobby_closed = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.sender = None
        self.receiver = None
        self.student_id = None

        self.nextPage = StudentMain()

        self.ui.searchButton.clicked.connect(self.searchClicked)
        self.ui.refreshButton.clicked.connect(self.refreshClicked)
        self.ui.joinButton.clicked.connect(self.joinClicked)

        # connect signal & slot
        self.join_room_success.connect(self.onJoinRoomSuccess)
        self.join_room_failed.connect(self.onJoinRoomFailed)
        self.kicked.connect(self.onKicked)
        self.nextPage.onCloseButtonClicked.connect(self.onExitRoom)
        self.student_list_updated.connect(self.onStudentListUpdated)
        self.room_closed.connect(self.onRoomClosed)
        self.refresh_materials.connect(self.onMaterialRefresh)

        self.model = QtGui.QStandardItemModel(self.ui.listView)

        self.receiver_thread_running = True

        self.allCourses = None

    def setSender(self, sender):
        self.sender = sender

    def setReceiver(self, receiver):
        self.receiver = receiver

    def setStudentId(self, student_id):
        self.student_id = student_id

    def createServerHandler(self):
        self.receiver_thread_running = True

        Thread(target=self.receiver_handler, args=(self.receiver,)).start()

    def updateRoomList(self):
        self.model.clear()
        for course in self.allCourses:
            courseString = course.id + " | " + course.name + " | " + course.teacher.name
            item = QtGui.QStandardItem(courseString)
            item.setCheckable(False)
            self.model.appendRow(item)

        self.ui.listView.setModel(self.model)

    def setRoomList(self, roomList):
        print("roomList: ", roomList)
        self.allCourses = roomList
        print("self.allCourses: ", self.allCourses)

    def joinClicked(self):

        index = QtCore.QModelIndex()
        index = self.ui.listView.currentIndex()

        if index == -1:
            return

        # selected course from the listView
        self.selectedCourse = self.model.itemFromIndex(index).text()
        tosend = self.selectedCourse.split(' | ')

        i = 0
        # avoiding empty key
        while True:

            if not tosend[i] == '':
                break
            i += 1

        # use tosend[i] to represent the Room ID
        # and open StudentMain

        choosed_room = None
        for course in self.allCourses:
            if course.id == tosend[i]:
                choosed_room = course

        self.sender.sendall_with_size([constant.JOIN_ROOM, tosend[i]])

    def searchClicked(self):
        filter_text = str(self.ui.searchBox.text()).lower()
        for row in range(self.model.rowCount()):
            if filter_text in str(self.model.item(row).text()).lower():
                self.ui.listView.setRowHidden(row, False)
            else:
                self.ui.listView.setRowHidden(row, True)

    def refreshClicked(self):
        self.updateRoomList()
        self.sender.sendall_with_size([constant.REFRESH_ROOM_LIST])

    @QtCore.pyqtSlot(list)
    def onJoinRoomSuccess(self, data_list):
        room = data_list[0]
        student_list = data_list[1]
        self.nextPage.setRoom(room)
        self.nextPage.setStudentList(student_list)
        self.nextPage.setUI()
        self.hide()
        self.nextPage.show()

    @QtCore.pyqtSlot(str)
    def onJoinRoomFailed(self, msg):
        QtWidgets.QMessageBox.critical(self, "Join error.", msg)

    @QtCore.pyqtSlot(str)
    def onKicked(self, string):
        QtWidgets.QMessageBox.critical(self, "", string)
        self.nextPage.hide()
        self.show()
        self.nextPage.resetState()

    @QtCore.pyqtSlot()
    def onExitRoom(self):
        self.sender.sendall_with_size([constant.LEAVE_ROOM])
        self.show()
        self.nextPage = StudentMain()
        self.nextPage.onCloseButtonClicked.connect(self.onExitRoom)

    @QtCore.pyqtSlot(list)
    def onStudentListUpdated(self, student_list):
        self.nextPage.updateViewInfo(student_list)

    @QtCore.pyqtSlot(str)
    def onRoomClosed(self, msg):
        QtWidgets.QMessageBox.critical(self, "Room closed", msg)
        self.show()
        self.nextPage = StudentMain()
        self.nextPage.onCloseButtonClicked.connect(self.onExitRoom)

    @QtCore.pyqtSlot(list)
    def onMaterialRefresh(self, materials_list):
        self.nextPage.addMaterial(materials_list[len(materials_list)-1])

    # # replaced method, don't change its name
    def closeEvent(self, event):
        self.receiver_thread_running = False
        
        self.sender.close()
        self.receiver.close()
        event.accept()

    def receiver_handler(self, receiver):
        while self.receiver_thread_running:
            decoded_input = self.receiver.recv_with_size_and_decode()
            if decoded_input == None:
                print("Server has down.")
                break
            print(decoded_input)
            cmd = decoded_input[0]
            if cmd == constant.REFRESH_ROOM_LIST:
                room_list = decoded_input[1]
                self.setRoomList(room_list)
                self.updateRoomList()

            elif cmd == constant.STUDENT_LIST_UPDATED:
                student_list = decoded_input[1]
                self.student_list_updated.emit(student_list)

            elif cmd == constant.MESSAGE_FROM_STUDENT:
                data = decoded_input[1]
                student = data[0]
                msg = data[1]
                # Please check if it is your own msg, so don't print it.
                print(student, ": ", msg)

            elif cmd == constant.REFRESH_MATERIAL:
                materials = decoded_input[1]
                print("Materials updated: ", materials)
                self.refresh_materials.emit(materials)

            elif cmd == constant.JOIN_ROOM_SUCCESS:

                data = decoded_input[1]
                room = data[0]
                student_list = data[1]
                self.join_room_success.emit(data)
                print("Joined room: ", room)

            elif cmd == constant.JOIN_ROOM_FAIL:

                msg = decoded_input[1]
                self.join_room_failed.emit(msg)
                print("Join room failed: ", msg)

            elif cmd == constant.KICK_STUDENT:
                print("You have been kicked")
                self.kicked.emit("You have been kicked from the room.")

            elif cmd == constant.CLOSE_ROOM:
                print("Room has been closed")
                msg = decoded_input[1]
                self.room_closed.emit(msg)

        print("Receiver END")
