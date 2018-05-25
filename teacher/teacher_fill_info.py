import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from teacher_fill_info_ui import Ui_Form
from teacher_main import TeacherMain
from validator import *

class TeacherFillInfo(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Information")

        self.main_window = TeacherMain(self)
        self.main_window.hide()

        self.ui.create_button.clicked.connect(self.create)

    def clear_info(self):
        name = self.ui.teacher_name_edit.setText("")
        room_name = self.ui.room_name_edit.setText("")
        description = self.ui.description_edit.setText("")
        capacity = self.ui.capacity_edit.setText("")

    def create(self):
        name = self.ui.teacher_name_edit.text()
        room_name = self.ui.room_name_edit.text()
        description = self.ui.description_edit.toPlainText()
        capacity = self.ui.capacity_edit.text()

        if is_valid_string(name) and is_valid_string(room_name) and is_valid_int(capacity):
            self.main_window.set_full_capacity(int(capacity))
            self.main_window.set_info("0", name, room_name, description)
            self.main_window.show()
            self.hide()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TeacherFillInfo()
    w.show()
    sys.exit(app.exec_())