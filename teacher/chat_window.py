import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from chat_window_ui import Ui_Form

class ChatWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Chat room")

        ag = QDesktopWidget().availableGeometry()
        sg = QDesktopWidget().screenGeometry()

        widget = self.geometry()
        x = ag.width() - widget.width() - 10
        y = 2 * ag.height() - sg.height() - widget.height()
        self.move(x, y)

    def clear_text(self):
        self.ui.text_browser.setText("")

    def add_text(self, text):
        self.ui.text_browser.setText(self.ui.text_browser.toPlainText() + text + "\n")