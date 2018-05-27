import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *

from UI.mainpage import Ui_Form

class StudentMain(QMainWindow):
    def __init__(self, roomID):
        print("studentMain: ")
        QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)


        # sample list of data
        self.allData = [] 
        # sample data 1 : roomID, courseName, lecturer, description, currentviewer 
        self.python = ["0001", "Python", "(python's)", "(python's)", "(python's)"] 
        # sample data 2 
        self.stats = ["0002", "Stats", "(stat's)", "(stat's)", "(stat's)"]
        # sample data 3
        self.database = ["0003", "DB", "(db's)", "(db's)", "(db's)"]
        #sample data 4
        self.cplusplus = ["0004", "C++", "(c++'s)", "(c++'s)", "(c++'s)"]
        #sample data 5
        self.os = ["0005", "OS", "(os's)", "(os's)", "(os's)"]
        #sample data 6
        self.math3 = ["0006", "Maths 3", "(math3's)", "(math3's)", "(math3's)"]

        self.allData.append(self.python)
        self.allData.append(self.stats)
        self.allData.append(self.database)
        self.allData.append(self.cplusplus)
        self.allData.append(self.os)
        self.allData.append(self.math3) 

        # sample demonstration , showing the correct information of the selected course 
        # from the previous page 

        #self.ui.testLabel.setText('aaa')
        for item in self.allData: 
            if item[0] == roomID: 

                print("roomID: " + roomID)
                print("item[0]: " + item[0])
                self.ui.roomIDinfo.setText(item[0])
                self.ui.courseNameInfo.setText(item[1])
                self.ui.lecturerInfo.setText(item[2])
                self.ui.descriptionInfo.setText(item[3])
                self.ui.currentViewInfo.setText(item[4])
                break







        




        

