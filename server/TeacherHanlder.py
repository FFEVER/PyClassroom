from threading import Thread
import pickle
import socket
import sys
import struct

from ClientSocket import ClientSocket
from Teacher import Teacher
import constant


class TeacherHanlder(Thread):

    def __init__(self, server, receiver, teacher, room):
        Thread.__init__(self)
        self.alive = True  # use for server to remove this from the teacher_list
        self.server = server
        self.teacher = teacher
        self.receiver = receiver 
        self.sender = None
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
            if self.sender == None:
                continue
            decoded_input = self.receiver.recv_with_size_and_decode()
            if decoded_input == None:
                self.disconnected()
                break
            

            command = decoded_input[0]
            if command == constant.START_LIVE:
                print(self.teacher.name,"starting a live.")
            elif command == constant.END_LIVE:
                print(self.teacher.name,"end a live.")
            elif command == constant.ADD_MATERIAL:
                material = decoded_input[1]
                print(self.teacher.name,"added a materail ->",material)
            elif command == constant.REMOVE_MATERIAL:
                material = decoded_input[1]
                print(self.teacher.name,"removed a materail ->",material)
            elif command == constant.KICK_STUDENT:
                student_name = decoded_input[1]
                print(self.teacher.name,"kick student ->",student_name)
            elif command == constant.CLOSE_ROOM:
                print(self.teacher.name,"closed a room.")
        self.receiver.close()

    def add_student_handler(self, studentHanlder):
        self.student_list.append(studentHanlder)

    def remove_student_handler(self, studentHandler):
        self.student_list.remove(studentHandler)
    
    def set_sender(self, sender):
        self.sender = sender

    def disconnected(self):
        ''' Clean up after teacher disconnected'''
        # tell every student that teacher has disconnected
        msg = [constant.CLOSE_ROOM, "The room has been closed"]
        for student in self.student_list:
            student.room = None
            student.socket.sendall_with_size(msg)
