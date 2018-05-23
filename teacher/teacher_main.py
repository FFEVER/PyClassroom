import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from teacher_main_ui import Ui_Form

class TeacherMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self, None)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TeacherMain()
    w.show()
    sys.exit(app.exec_())