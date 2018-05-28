import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from UI.studentinputinfo import Ui_Form
from studentLobby import StudentLobby


from Student import Student
from ClientSocket import ClientSocket
import constant

import socket
import sys
import struct
import pickle
import traceback
from threading import Thread


class StudentInput(QtWidgets.QMainWindow):
    onInputClosed = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, None)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.startButton.clicked.connect(self.startButtonOnClick)

        self.nextPage = StudentLobby()
        self.nextPage.on_lobby_closed.connect(self.onLobbyClose)

        self.setWindowTitle("Enter Your Name!")

    def startButtonOnClick(self):
        # save input name
        self.inputName = self.ui.inputBox.text()

        sender, student_id, room_list = self.create_sender(Student(self.inputName))
        receiver = self.create_receiver(student_id)
        video_receiver = self.create_video_sender(student_id)
        

        self.nextPage.setRoomList(room_list)
        self.nextPage.updateRoomList()

        self.nextPage.setSender(sender)
        self.nextPage.setReceiver(receiver)
        self.nextPage.setStudentId(student_id)

        self.nextPage.createServerHandler()

        # open lobby
        self.hide()
        self.nextPage.show()

    def connect_to_server(self, socket, host, port):
        try:
            socket.connect((host, port))
            return socket
        except:
            print("Connection error")
            sys.exit()

    def create_sender(self, student):
        ''' if can connect to server this will return (sender,student_id,room_list) '''
        soc = socket.socket()         # Create a socket object
        host = socket.gethostname()  # Get local machine name
        port = constant.PORT                # Reserve a port for your service.

        soc = self.connect_to_server(soc, host, port)
        sender = ClientSocket(soc)

        data = []
        data.append(constant.I_AM_STUDENT_SENDER)
        data.append(student)
        sender.sendall_with_size(data)

        decoded_input = sender.recv_with_size_and_decode()
        student_id = decoded_input[0]
        room_list = decoded_input[1]
        print(student_id, room_list)
        return (sender, student_id, room_list)

    def create_receiver(self, student_id):
        ''' if can connect to server this will return receiver '''
        soc = socket.socket()         # Create a socket object
        host = socket.gethostname()  # Get local machine name
        port = constant.PORT                # Reserve a port for your service.

        soc = self.connect_to_server(soc, host, port)
        receiver = ClientSocket(soc)

        data = [constant.I_AM_STUDENT_RECEIVER, student_id]
        receiver.sendall_with_size(data)

        is_success = receiver.recv_with_size_and_decode()
        print("create_receiver is ", is_success)

        return receiver

    def create_video_sender(self, student_id):
        ''' if can connect to server this will return receiver '''
        soc = socket.socket()  # Create a socket object
        host = socket.gethostname()  # Get local machine name
        port = constant.PORT  # Reserve a port for your service.

        soc = self.connect_to_server(soc, host, port)
        video_sender = ClientSocket(soc)

        data = [constant.I_AM_STUDENT_VIDEO_RECEIVER, student_id]
        video_sender.sendall_with_size(data)

        is_success = video_sender.recv_with_size_and_decode()
        print("create_video_receiver is ", is_success)

        return video_sender

    def create_sound_sender(self, student_id):
        ''' if can connect to server this will return receiver '''
        soc = socket.socket()  # Create a socket object
        host = socket.gethostname()  # Get local machine name
        port = constant.PORT  # Reserve a port for your service.

        soc = self.connect_to_server(soc, host, port)
        sound_sender = ClientSocket(soc)

        data = [constant.I_AM_STUDENT_SOUND_RECEIVER, student_id]
        sound_sender.sendall_with_size(data)

        is_success = sound_sender.recv_with_size_and_decode()
        print("create_sound_receiver is ", is_success)

        return sound_sender

    @QtCore.pyqtSlot()
    def onLobbyClose(self):
        pass
        #print("Input Close")
        # self.onInputClosed.emit()
        # self.close()
