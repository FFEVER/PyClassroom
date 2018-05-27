import sys

from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
from UI.selectrole import Ui_Form 
from studentInput import StudentInput

class StudentLogic(QtWidgets.QMainWindow): 
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, None) 
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.studentButton.clicked.connect(self.studentButtonOnClick) 

        self.nextPage = StudentInput() 
        self.setWindowTitle("Select Your Role")


    def studentButtonOnClick(self): 
        self.hide() 

        #open studentInput window
        self.nextPage.show() 
        
         

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) 
    w = StudentLogic() 
    w.show()
    sys.exit(app.exec_())





    