import sys

from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from UI.selectrole import Ui_Form 
from studentInput import StudentInput
from teacher_fill_info import TeacherFillInfo

class SelectRole(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, None) 
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.studentButton.clicked.connect(self.studentButtonOnClick)
        self.ui.teacherButton.clicked.connect(self.teacherButtonOnClick)

        self.nextPage = StudentInput()
        self.teacherPage = TeacherFillInfo()

        self.setWindowTitle("Select Your Role")
#        self.nextPage.onInputClosed.connect(self.onStudentInputClosed)


    def studentButtonOnClick(self): 
        self.hide() 

        #open studentInput window
        self.nextPage.show()

    def teacherButtonOnClick(self):
        self.hide()
        self.teacherPage.show()

    # @QtCore.pyqtSlot()
    # def onStudentInputClosed(self):
    #     print("Exit App")
    #     self.close()
        
         

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    w = SelectRole() 
    w.show()
    sys.exit(app.exec_())
    print("Exit")





    
