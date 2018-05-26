from threading import Thread
import pickle
import socket
import sys
import struct

from Student import Student
import constant

class StudentHandler(Thread):
    def __init__(self,server,receiver,student):
        Thread.__init__(self)
        self.alive = True
        self.server = server
        self.student = student
        self.receiver = receiver
        self.sender = None
        self.teacher = None # Teacher Handler

    def run(self):
        '''#TODO: run() -> Student handler
        [ ] refresh room list
        [ ] select room (create new thread, this thread wait)
        [ ] close connection when down
        '''
        print("Student thread:", self.student)
        while True:
            if self.sender == None:
                continue
            # Not in room
            decoded_input = self.receiver.recv_with_size_and_decode()
            if decoded_input == None:
                self.disconnected()
                break

            command = decoded_input[0]
        
            if self.teacher == None:
                if command == constant.JOIN_ROOM:
                    room_id = decoded_input[1]
                    print(self.student.name,"join a room ->",room_id)
                elif command == constant.REFRESH_ROOM_LIST:
                    print(self.student.name,"refresh room list.")
                else:
                    pass
            else:
                if command == constant.SEND_MSG:
                    msg = decoded_input[1]
                    print(self.student.name,"send a msg ->",msg)
                elif command == constant.LEAVE_ROOM:
                    print(self.student.name,"leave a room.")
                elif command == constant.REFRESH_MATERIAL:
                    print(self.student.name,"refresh materail")
                else:
                    pass

        self.receiver.close()

    def set_sender(self, sender):
        self.sender = sender

    def disconnected(self):
        if self.teacher != None:
            self.teacher.remove_student_handler(self)

