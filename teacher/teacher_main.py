import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from teacher_main_ui import Ui_Form
from chat_window import ChatWindow
from validator import *

class TeacherMain(QWidget):
    def __init__(self, info_window):
        QWidget.__init__(self, None)

        self.info_window = info_window
        self.chat_window = ChatWindow()
        self.chat_window.hide()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Teaching Lobby")

        self.students = ["qwerty", "asdfgh", "zxcfvb", "][poi"]

        self.playing = False
        self.full_capacity = 0
        self.current_capacity = 0

        self.ui.start_button.clicked.connect(self.start_stop)
        self.ui.material_button.clicked.connect(self.add_material)
        self.ui.exit_button.clicked.connect(self.exit_room)
        self.ui.kick_button.clicked.connect(self.kick_selected)
        self.ui.start_button.setText("Start streaming")

        self.update_student_list()

    def start_stop(self):
        self.playing = not self.playing
        if self.playing:
            self.showMinimized()
            self.ui.start_button.setText("Stop streaming")
            self.chat_window.show()
            self.chat_window.setWindowState(self.chat_window.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
            self.chat_window.activateWindow()
        else:
            self.ui.start_button.setText("Start streaming")
            self.chat_window.hide()


    def kick_selected(self):
        index = self.ui.student_list.currentRow()
        if index != -1:
            self.students.pop(index)
            self.update_student_list()

    def update_student_list(self):
        self.ui.student_list.clear()
        for i in self.students:
            self.ui.student_list.addItem(QListWidgetItem(i))
        self.set_current_capacity(len(self.students))

    def add_material(self):
        entered = self.ui.material_edit.text()
        if is_valid_string(entered):
            self.ui.material_browser.setText(self.ui.material_browser.toPlainText() + entered + "\n")
            self.ui.material_edit.setText("")

    def exit_room(self):
        #TODO - close room
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