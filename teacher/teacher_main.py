import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from teacher_main_ui import Ui_Form
from validator import *

class TeacherMain(QMainWindow):
    def __init__(self, info_window):
        QMainWindow.__init__(self, None)

        self.info_window = info_window

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.material_button.clicked.connect(self.add_material)
        self.ui.exit_button.clicked.connect(self.exit_room)

        self.full_capacity = 0
        self.current_capacity = 0

    def add_material(self):
        entered = self.ui.material_edit.text()
        if is_valid_string(entered):
            self.ui.material_browser.setText(self.ui.material_browser.toPlainText() + entered + "\n")
            self.ui.material_edit.setText("")

    def exit_room(self):
        #TODO - close room
        self.info_window.show()
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