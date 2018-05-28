import sys 
import socket
import numpy as np
import cv2

from PyQt5 import QtCore, QtGui, QtWidgets
from UI.mainpage import Ui_Form

class StudentStream(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, None)

        self.server = socket.socket()
        self.server.connect(('127.0.0.1', 5005))

        while True:
            data = server.recv(100000)
            if not data:
                break
            print(data)
            nparr = np.fromstring(data, np.uint8)
            self.image = cv2.imdecode(nparr, 1)
            height, width, byteValue = self.image.shape
            byteValue = byteValue * width

            cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB, self.image)

            self.mQImage = QImage(self.image, width, height,
                                  byteValue, QImage.Format_RGB888)

            try:
                self.paintEvent()

            except:
                pass

    def paintEvent(self, QPaintEvent):
        painter = QPainter()
        painter.begin(self.ui.streamWidget)
        painter.drawImage(self.ui.streamWidget.geometry(),  self.mQImage)
        painter.end()
        self.update()

    def keyPressEvent(self, QKeyEvent):
        super(StudentStream, self).keyPressEvent(QKeyEvent)
        if 'q' == QKeyEvent.text():
            app.exit(1) 
        
        

