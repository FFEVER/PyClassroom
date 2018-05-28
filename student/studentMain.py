import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import *

from PyQt5 import QtWidgets,QtCore

from UI.mainpage import Ui_Form
from StreamHandler import StreamHandler

class StudentMain(QtWidgets.QMainWindow):
    onCloseButtonClicked = QtCore.pyqtSignal()
    def __init__(self):
        print("studentMain: ")
        QtWidgets.QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.room = None 
        self.student_list = None

        self.stream_handler = None

        box_layout = QVBoxLayout()
        box_layout.setSpacing(10)
        box_layout.setAlignment(Qt.AlignTop)
        self.list_container = QWidget()
        pal = self.list_container.palette()
        pal.setColor(self.list_container.backgroundRole(), Qt.white)
        self.list_container.setPalette(pal)
        self.list_container.setLayout(box_layout)
        self.ui.leave_button.clicked.connect(self.close)

        self.ui.scroll_area.setWidget(self.list_container)
        self.ui.scroll_area.verticalScrollBar().rangeChanged.connect(self.scroll_to_material_bottom)

    def setUI(self):
        self.ui.roomIDinfo.setText(self.room.id)
        self.ui.courseNameInfo.setText(self.room.name)
        self.ui.lecturerInfo.setText(self.room.teacher.name)
        self.ui.descriptionInfo.setText(self.room.description)
        self.ui.currentViewInfo.setText(str(len(self.student_list)) + "/" + str(self.room.max_student))

    def addMaterial(self, text):
        label = QLabel(text)
        label.setMargin(10)
        label.setStyleSheet("QLabel { background:rgb(200,200,200);}")
        label.setFixedHeight(50)
        self.list_container.layout().addWidget(label)


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

    def startStreamThread(self,video_receiver):
        self.stream_handler = StreamHandler(self,video_receiver)
        self.stream_handler.start()

    def stopStreamThread(self):
        self.stream_handler.stop()
    
    # overrided method, don't change its name
    def closeEvent(self,event):
        print("Close event")
        self.onCloseButtonClicked.emit()
        event.accept()

    def scroll_to_material_bottom(self, min, maxi):
        self.ui.scroll_area.verticalScrollBar().setValue(maxi)
    


        




        

