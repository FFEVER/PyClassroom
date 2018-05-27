import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *

from PyQt5 import QtWidgets

from UI.mainpage import Ui_Form

class StudentMain(QtWidgets.QMainWindow):
    def __init__(self, room, student_list):
        print("studentMain: ")
        QtWidgets.QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.room = room 


        self.ui.roomIDinfo.setText(self.room.id)
        self.ui.courseNameInfo.setText(self.room.name)
        self.ui.lecturerInfo.setText(self.room.teacher.name)
        self.ui.descriptionInfo.setText(self.room.description)
        self.ui.currentViewInfo.setText(str(len(student_list)) + "/" + str(self.room.max_student))
                







        




        

