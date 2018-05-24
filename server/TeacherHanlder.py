from Teacher import Teacher
from threading import Thread
from ClientSocket import ClientSocket
import pickle
import socket
import sys
import struct


START_LIVE = "start_live"
END_LIVE = "end_live"
ADD_MATERIAL = "add_material"
REMOVE_MATERIAL = "remove_mat"
KICK_STUDENT = "kick_student"


class TeacherHanlder(Thread):

    def __init__(self, server, socket, teacher, room):
        Thread.__init__(self)
        self.alive = True  # use for server to remove this from the teacher_list
        self.server = server
        self.teacher = teacher
        self.socket = ClientSocket(socket)  # TODO: self.socket = socket
        self.room = room
        self.student_list = []  # list of studentHandler

    def run(self):
        '''#TODO: run() -> Teacher handler
        [ ] close connection when down
        [ ] add material
        [ ] start live
        [ ] observer for each student (chat)
        '''

        print("Teacher Thread:", self.teacher)
        print(self.room)

        while True:
            decoded_input = self.socket.recv_with_size_and_decode()
            if decoded_input == None:
                self.disconnected()
                break

            command = decoded_input[0]
            if command == START_LIVE:
                pass
            elif command == END_LIVE:
                pass
            elif command == ADD_MATERIAL:
                pass
            elif command == REMOVE_MATERIAL:
                pass
            elif command == KICK_STUDENT:
                pass

    def add_student_handler(self, studentHanlder):
        self.student_list.append(studentHanlder)

    def disconnected(self):
        ''' Clean up after teacher disconnected'''
        # tell every student that teacher has disconnected
        msg = ["room_closed", "The room has been closed"]
        for student in self.student_list:
            student.room = None
            student.socket.sendall_with_size(msg)
