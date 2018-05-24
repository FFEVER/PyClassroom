from Student import Student
from threading import Thread
import pickle
import socket
import sys
import struct

JOIN_ROOM = "join_room"
LEAVE_ROOM = "leave_room"
SEND_MSG = "send_message"
REFRESH_ROOM_LIST = "refresh_room_list"
REFRESH_MATERIAL = "refresh_material"

class StudentHandler(Thread):
    def __init__(self,server,socket,student):
        Thread.__init__(self)
        self.alive = True
        self.server = server
        self.student = student
        self.socket = socket
        self.teacher = None # Teacher Handler

    def run(self):
        '''#TODO: run() -> Student handler
        [ ] refresh room list
        [ ] select room (create new thread, this thread wait)
        [ ] close connection when down
        '''
        print("Student thread:", self.student)
        while True:
            # Not in room
            decoded_input = self.socket.recv_with_size_and_decode()
            if decoded_input == None:
                break

            command = decoded_input[0]
        
            if room == None:
                if command == JOIN_ROOM:
                    pass
                elif command == REFRESH_ROOM_LIST:
                    pass
                else:
                    pass
            else:
                if command == SEND_MSG:
                    pass
                elif command == LEAVE_ROOM:
                    pass
                elif command == REFRESH_MATERIAL:
                    pass
                else:
                    pass

