import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from UI.dialog import Ui_dialog

class popUpDialog(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, None)
        self.ui = Ui_dialog()
        self.ui.setupUi(self)

    def setText(self, text): 
        self.ui.label.setText(text)