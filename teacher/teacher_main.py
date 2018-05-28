import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from teacher_main_ui import Ui_Form
from chat_window import ChatWindow
from validator import *
from streamer_thread import StreamerThread
from threading import Thread

from Room import Room
from Teacher import Teacher
from Student import Student
from ClientSocket import ClientSocket
import constant
import socket
import struct
import pickle
import traceback

class TeacherMain(QWidget):

    chat_window_updater = pyqtSignal(str)

    def __init__(self, info_window):
        QWidget.__init__(self, None)

        self.info_window = info_window
        self.chat_window = ChatWindow()
        self.chat_window.hide()

        self.streamer_thread = None

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Teaching Lobby")

        self.students = []
        self.materials = []

        self.playing = False
        self.full_capacity = 0
        self.current_capacity = 0

        self.sender = None
        self.receiver = None
        self.receiver_thread_running = False

        box_layout = QVBoxLayout()
        box_layout.setSpacing(10)
        box_layout.setAlignment(Qt.AlignTop)
        self.list_container = QWidget()
        pal = self.list_container.palette()
        pal.setColor(self.list_container.backgroundRole(), Qt.white)
        self.list_container.setPalette(pal)
        self.list_container.setLayout(box_layout)

        self.ui.start_button.clicked.connect(self.start_stop)
        self.ui.material_button.clicked.connect(self.add_material)
        self.ui.exit_button.clicked.connect(self.end_connection)
        self.ui.kick_button.clicked.connect(self.kick_selected)

        self.ui.scroll_area.setWidget(self.list_container)
        self.ui.scroll_area.verticalScrollBar().rangeChanged.connect(self.scroll_to_material_bottom)

        self.chat_window_updater.connect(self.update_chat_window_text)

        self.ui.start_button.setText("Start streaming")

        self.update_student_list()


    def set_sender(self, sender):
        self.sender = sender

    def set_receiver(self, rec):
        self.receiver = rec

    def start_receiver_thread(self):
        try:
            self.receiver_thread_running = True
            self.receiver_thread = Thread(target = self.receiver_handler, args=(self.receiver,))
            self.receiver_thread.start()
        except:
            traceback.print_exc()

    @pyqtSlot(str)
    def update_chat_window_text(self, value):
        self.chat_window.add_text(value)

    def receiver_handler(self, receiver):
        while self.receiver_thread_running:
            decoded_input = receiver.recv_with_size_and_decode()
            if decoded_input == None:
                print("Server has down.")
                self.exit_room()
            cmd = decoded_input[0]
            if cmd == constant.STUDENT_LIST_UPDATED:
                self.students = decoded_input[1]
                self.update_student_list()
            elif cmd == constant.MESSAGE_FROM_STUDENT:
                if self.playing:
                    data = decoded_input[1]
                    student = data[0]
                    msg = data[1]
                    msg = student.name + "(" + student.id + "):" + msg
                    self.chat_window_updater.emit(msg)
                    # Please check if it is your own msg, so don't print it.
                    print(student, ": ", msg)

    def start_stop(self):
        self.playing = not self.playing
        if self.playing:
            self.streamer_thread = StreamerThread()
            self.streamer_thread.start()

            self.showMinimized()
            self.ui.start_button.setText("Stop streaming")
            self.chat_window.show()
            self.chat_window.setWindowState(self.chat_window.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
            self.chat_window.activateWindow()
        else:
            self.streamer_thread.stop()
            self.streamer_thread = None

            self.ui.start_button.setText("Start streaming")
            self.chat_window.hide()


    def kick_selected(self):
        index = self.ui.student_list.currentRow()
        if index != -1:
            student_id = self.students[index].id
            self.students.pop(index)
            self.sender.sendall_with_size([constant.KICK_STUDENT, student_id])


    def update_student_list(self):
        self.ui.student_list.clear()
        for i in self.students:
            self.ui.student_list.addItem(QListWidgetItem(i.id + " " + i.name))
        self.set_current_capacity(len(self.students))

    def add_material(self):
        entered = self.ui.material_edit.text()
        if is_valid_string(entered):
            self.materials.append(entered)

            label = QLabel(entered)
            label.setMargin(10)
            label.setStyleSheet("QLabel { background:rgb(200,200,200);}")
            label.setFixedHeight(50)
            self.list_container.layout().addWidget(label)
            self.ui.scroll_area.ensureWidgetVisible(label, 0, 50)

            #self.ui.material_browser.setText(self.ui.material_browser.toPlainText() + entered + "\n")
            self.sender.sendall_with_size([constant.ADD_MATERIAL, self.materials])
            self.ui.material_edit.setText("")

    def scroll_to_material_bottom(self, min, maxi):
        self.ui.scroll_area.verticalScrollBar().setValue(maxi)

    def end_connection(self):
        self.receiver_thread_running = False
        self.sender.sendall_with_size([constant.CLOSE_ROOM])
        self.sender.close()
        self.receiver.close()
        self.exit_room()

    def exit_room(self):
        if self.streamer_thread != None:
            self.streamer_thread.stop()
            self.streamer_thread = None
        self.playing = False
        self.info_window.clear_info()
        self.info_window.show()
        self.chat_window.clear_text()
        self.chat_window.hide()
        self.hide()

    def set_current_capacity(self, cap):
        self.current_capacity = cap
        self.update_capacity()

    def set_full_capacity(self, cap):
        self.full_capacity = cap
        self.update_capacity()

    def update_capacity(self):
        text = str(self.current_capacity) + "/" + str(self.full_capacity)
        self.ui.capacity_label.setText(text)

    def set_info(self, id, name, room_name, description):
        self.ui.id_label.setText(id)
        self.ui.teacher_name_label.setText(name)
        self.ui.room_name_label.setText(room_name)
        self.ui.description_label.setText(description)