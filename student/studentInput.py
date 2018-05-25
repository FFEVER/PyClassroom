import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from UI.studentinputinfo import Ui_Form
from studentLobby import StudentLobby

class StudentInput(QtWidgets.QMainWindow): 
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, None) 
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.startButton.clicked.connect(self.startButtonOnClick)
        
        self.nextPage = StudentLobby() 

        self.setWindowTitle("Enter Your Name!")
    

    def startButtonOnClick(self):
        #save input name
        self.inputName = self.ui.inputBox.text() 
         
        #open lobby 
        self.hide()
        self.nextPage.show() 
        
        






