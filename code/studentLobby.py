import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from UI.lobbystudent import Ui_Form
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
    live_start = QtCore.pyqtSignal()
    live_end = QtCore.pyqtSignal()
    msg_receive = QtCore.pyqtSignal(str)

    on_lobby_closed = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.sender = None
        self.receiver = None
        self.video_receiver = None
        self.sound_receiver = None
        self.student_id = None

        self.nextPage = StudentMain()
        self.is_in_room = False

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
        self.live_start.connect(self.onLiveStart)
        self.live_end.connect(self.onLiveEnd)
        self.msg_receive.connect(self.onMessageReceive)
        self.nextPage.onSendTextButtonClicked.connect(self.onMessageSend)

        self.ui.table.verticalHeader().setVisible(False)
        self.ui.table.setColumnWidth(0, 50)
        self.ui.table.setColumnWidth(1, 189)
        self.ui.table.setColumnWidth(2, 150)
        self.ui.table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        #self.model = QtGui.QStandardItemModel(self.ui.listView)

        self.receiver_thread_running = True

        self.allCourses = None
        self.shownCourses = None

    def setSender(self, sender):
        self.sender = sender

    def setReceiver(self, receiver):
        self.receiver = receiver
    
    def setVideoReceiver(self,video_receiver):
        self.video_receiver = video_receiver
    
    def setSoundReceiver(self,sound_receiver):
        self.sound_receiver = sound_receiver

    def setStudentId(self, student_id):
        self.student_id = student_id

    def createServerHandler(self):
        self.receiver_thread_running = True

        Thread(target=self.receiver_handler, args=(self.receiver,)).start()

    def updateRoomList(self):
        self.ui.table.setRowCount(0)
        for i in range(len(self.shownCourses)):
            self.ui.table.insertRow(i)
            self.ui.table.setItem(i, 0, QtWidgets.QTableWidgetItem(self.shownCourses[i].id))
            self.ui.table.setItem(i, 1, QtWidgets.QTableWidgetItem(self.shownCourses[i].name))
            self.ui.table.setItem(i, 2, QtWidgets.QTableWidgetItem(self.shownCourses[i].teacher.name))
            #self.model.appendRow(item)
        #self.ui.listView.setModel(self.model)

    def setRoomList(self, roomList):
        print("roomList: ", roomList)
        self.allCourses = roomList
        self.shownCourses = roomList
        print("self.shownCourse: ", self.shownCourses)
        print("self.allCourses: ", self.allCourses)

    def joinClicked(self):

        index = self.ui.table.currentRow()

        if index == -1:
            return

        room_id = self.shownCourses[index].id

        self.sender.sendall_with_size([constant.JOIN_ROOM, room_id])

    def searchClicked(self):
        self.filterCourses()
        self.updateRoomList()

    def refreshClicked(self):
        self.sender.sendall_with_size([constant.REFRESH_ROOM_LIST])

    @QtCore.pyqtSlot(list)
    def onJoinRoomSuccess(self, data_list):
        self.is_in_room = True
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
        self.is_in_room = False
        QtWidgets.QMessageBox.critical(self, "", string)
        self.nextPage.hide()
        self.show()
        self.nextPage = StudentMain()
        self.nextPage.onCloseButtonClicked.connect(self.onExitRoom)
        self.nextPage.onSendTextButtonClicked.connect(self.onMessageSend)

    @QtCore.pyqtSlot()
    def onExitRoom(self):
        self.is_in_room = False
        self.sender.sendall_with_size([constant.LEAVE_ROOM])
        self.show()
        self.nextPage.hide()
        self.nextPage = StudentMain()
        self.nextPage.onCloseButtonClicked.connect(self.onExitRoom)
        self.nextPage.onSendTextButtonClicked.connect(self.onMessageSend)

    @QtCore.pyqtSlot(list)
    def onStudentListUpdated(self, student_list):
        self.nextPage.updateViewInfo(student_list)

    @QtCore.pyqtSlot(str)
    def onRoomClosed(self, msg):
        self.is_in_room = False
        QtWidgets.QMessageBox.critical(self, "Room closed", msg)
        self.show()
        self.nextPage.hide()
        if self.nextPage.stream_handler != None:
            print("Live now -> closing videoHandler")
            self.nextPage.stopStreamThread()
        self.nextPage = StudentMain()
        self.nextPage.onCloseButtonClicked.connect(self.onExitRoom)
        self.nextPage.onSendTextButtonClicked.connect(self.onMessageSend)

    @QtCore.pyqtSlot(list)
    def onMaterialRefresh(self, materials_list):
        self.nextPage.addMaterial(materials_list[len(materials_list)-1])

    @QtCore.pyqtSlot()
    def onLiveStart(self):
        self.nextPage.startStreamThread(self.video_receiver,self.sound_receiver)
        self.nextPage.hide_cover()

    @QtCore.pyqtSlot()
    def onLiveEnd(self):
        self.nextPage.stopStreamThread()
        self.nextPage.show_cover()

    @QtCore.pyqtSlot(str)
    def onMessageReceive(self,msg):
        self.nextPage.update_message_box(msg)

    @QtCore.pyqtSlot(str)
    def onMessageSend(self,msg):
        self.sender.sendall_with_size([constant.SEND_MSG,msg])

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
            print(self.is_in_room, cmd)
            if not self.is_in_room:
                if cmd == constant.REFRESH_ROOM_LIST:
                    room_list = decoded_input[1]
                    self.setRoomList(room_list)
                    self.updateRoomList()

                elif cmd == constant.STUDENT_LIST_UPDATED:
                    student_list = decoded_input[1]
                    self.student_list_updated.emit(student_list)

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

                else:
                    continue

            else:
                if cmd == constant.MESSAGE_FROM_STUDENT:
                    data = decoded_input[1]
                    student = data[0]
                    msg = data[1]
                    # Please check if it is your own msg, so don't print it.
                    full_message = "[" + student.id + "]" + student.name + ": " + msg
                    print(full_message)
                    self.msg_receive.emit(full_message)

                elif cmd == constant.STUDENT_LIST_UPDATED:
                    student_list = decoded_input[1]
                    self.student_list_updated.emit(student_list)

                elif cmd == constant.REFRESH_MATERIAL:
                    materials = decoded_input[1]
                    print("Materials updated: ", materials)
                    self.refresh_materials.emit(materials)

                elif cmd == constant.KICK_STUDENT:
                    print("You have been kicked")
                    self.kicked.emit("You have been kicked from the room.")

                elif cmd == constant.CLOSE_ROOM:
                    print("Room has been closed")
                    msg = decoded_input[1]
                    self.room_closed.emit(msg)

                elif cmd == constant.START_LIVE:
                    print("teacer has started live")
                    self.live_start.emit()

                elif cmd == constant.END_LIVE:
                    print("teacher has ended live")
                    self.live_end.emit()

        print("Receiver END")

    def filterCourses(self):
        self.shownCourses = []
        filter_text = str(self.ui.searchBox.text()).lower()
        if self.ui.filter.currentIndex() == 0:
            for row in range(len(self.allCourses)):
                row_id = self.allCourses[row].id.lower()
                if filter_text in row_id:
                    self.shownCourses.append(self.allCourses[row])
        else:
            for row in range(len(self.allCourses)):
                row_id = self.allCourses[row].name.lower()
                if filter_text in row_id:
                    self.shownCourses.append(self.allCourses[row])


