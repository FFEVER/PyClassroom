import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *

from PyQt5 import QtWidgets,QtCore


from UI.mainpage import Ui_Form

class StudentMain(QtWidgets.QMainWindow):
    onCloseButtonClicked = QtCore.pyqtSignal()
    def __init__(self):
        print("studentMain: ")
        QtWidgets.QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.room = None 
        self.student_list = None


    def setUI(self):
        self.ui.roomIDinfo.setText(self.room.id)
        self.ui.courseNameInfo.setText(self.room.name)
        self.ui.lecturerInfo.setText(self.room.teacher.name)
        self.ui.descriptionInfo.setText(self.room.description)
        self.ui.currentViewInfo.setText(str(len(self.student_list)) + "/" + str(self.room.max_student))


    def setRoom(self, room):
        self.room = room 

    def setStudentList(self, student_list):
        self.student_list = student_list

    def resetState(self):
        self.setStudentList(None)
        self.setRoom(None)

    def updateViewInfo(self,student_list):
        self.student_list = student_list
        self.ui.currentViewInfo.setText(str(len(self.student_list)) + "/" + str(self.room.max_student))
    
    # overrided method, don't change its name
    def closeEvent(self,event):
        print("Close event")
        self.onCloseButtonClicked.emit()
        event.accept()
    


        




        

