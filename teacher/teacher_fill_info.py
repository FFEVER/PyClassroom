import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from teacher_fill_info_ui import Ui_Form
from teacher_main import TeacherMain
from validator import *

from Room import Room
from Teacher import Teacher
from Student import Student
from ClientSocket import ClientSocket
import constant
import socket
import struct
import pickle



class TeacherFillInfo(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Information")

        self.main_window = TeacherMain(self)
        self.main_window.hide()

        self.ui.create_button.clicked.connect(self.create)

    def clear_info(self):
        self.ui.teacher_name_edit.setText("")
        self.ui.room_name_edit.setText("")
        self.ui.description_edit.setText("")
        self.ui.capacity_edit.setText("")

    def create(self):
        name = self.ui.teacher_name_edit.text()
        room_name = self.ui.room_name_edit.text()
        description = self.ui.description_edit.toPlainText()
        capacity = self.ui.capacity_edit.text()

        if is_valid_string(name) and is_valid_string(room_name) and is_valid_int(capacity):
            room = Room("0", room_name, int(capacity), Teacher(name), description)
            sender, room_id = self.create_sender(room)
            receiver = self.create_receiver(room_id)
            video_sender = self.create_video_sender(room_id)
            sound_sender = self.create_sound_sender(room_id)

            self.main_window.set_full_capacity(int(capacity))
            self.main_window.set_info(room_id, name, room_name, description)
            self.main_window.set_sender(sender)
            self.main_window.set_receiver(receiver)
            self.main_window.start_receiver_thread()
            self.main_window.show()

            self.hide()

    def connect_to_server(self, socket, host, port):
        try:
            socket.connect((host, port))
            return socket
        except:
            print("Connection error")
            sys.exit()

    def create_sender(self, room):
        ''' if can connect to server this will return (sender,room_id) '''
        soc = socket.socket()  # Create a socket object
        host = socket.gethostname()  # Get local machine name
        port = constant.PORT  # Reserve a port for your service.

        soc = self.connect_to_server(soc, host, port)
        sender = ClientSocket(soc)

        data = []
        data.append(constant.I_AM_TEACHER_SENDER)
        data.append(room)
        sender.sendall_with_size(data)

        decoded_input = sender.recv_with_size_and_decode()
        is_room_created = decoded_input[0]
        room_id = decoded_input[1]
        print(is_room_created, "with id", room_id)
        return (sender, room_id)

    def create_receiver(self, room_id):
        ''' if can connect to server this will return receiver '''
        soc = socket.socket()  # Create a socket object
        host = socket.gethostname()  # Get local machine name
        port = constant.PORT  # Reserve a port for your service.

        soc = self.connect_to_server(soc, host, port)
        receiver = ClientSocket(soc)

        data = [constant.I_AM_TEACHER_RECEIVER, room_id]
        receiver.sendall_with_size(data)

        is_success = receiver.recv_with_size_and_decode()
        print("create_receiver is ", is_success)

        return receiver


    def create_video_sender(self, room_id):
        ''' if can connect to server this will return receiver '''
        soc = socket.socket()  # Create a socket object
        host = socket.gethostname()  # Get local machine name
        port = constant.PORT  # Reserve a port for your service.

        soc = self.connect_to_server(soc, host, port)
        video_sender = ClientSocket(soc)

        data = [constant.I_AM_TEACHER_VIDEO_SENDER, room_id]
        video_sender.sendall_with_size(data)

        is_success = video_sender.recv_with_size_and_decode()
        print("create_video_sender is ", is_success)

        return video_sender

    def create_sound_sender(self, room_id):
        ''' if can connect to server this will return receiver '''
        soc = socket.socket()  # Create a socket object
        host = socket.gethostname()  # Get local machine name
        port = constant.PORT  # Reserve a port for your service.

        soc = self.connect_to_server(soc, host, port)
        sound_sender = ClientSocket(soc)

        data = [constant.I_AM_TEACHER_SOUND_SENDER, room_id]
        sound_sender.sendall_with_size(data)

        is_success = sound_sender.recv_with_size_and_decode()
        print("create_sound_sender is ", is_success)

        return sound_sender


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = TeacherFillInfo()
    w.show()
    sys.exit(app.exec_())