import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from teacher_fill_info_ui import Ui_Form

class TeacherFillInfo(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TeacherFillInfo()
    w.show()
    sys.exit(app.exec_())