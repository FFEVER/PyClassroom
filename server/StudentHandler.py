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
        self.video_sender = None
        self.sound_sender = None
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
                    self.cmd_join_room(room_id)
                elif command == constant.REFRESH_ROOM_LIST:
                    print(self.student.name,"refresh room list.")
                    self.cmd_refresh_room_list()
                else:
                    pass
            else:
                if command == constant.SEND_MSG:
                    msg = decoded_input[1]
                    print(self.student.name,"send a msg ->",msg)
                    self.cmd_send_msg(msg)
                elif command == constant.LEAVE_ROOM:
                    print(self.student.name,"leave a room.")
                    self.cmd_leave_room()
                else:
                    pass

        self.receiver.close()

    def cmd_join_room(self,room_id):
        try:
            self.teacher = self.server.teacher_list[room_id]
        except KeyError:
            return self.notify_student(constant.JOIN_ROOM_FAIL,"Room doesn't exist.")
        self.teacher.add_student_handler(self)
    def cmd_refresh_room_list(self):
        self.notify_student(constant.REFRESH_ROOM_LIST,self.server.room_list)
    def cmd_send_msg(self,msg):
        self.teacher.notify_all_student(constant.MESSAGE_FROM_STUDENT,[self.student,msg])
        self.teacher.notify_teacher(constant.MESSAGE_FROM_STUDENT,[self.student,msg])
    def cmd_leave_room(self):
        self.teacher.remove_student_handler(self)
        self.teacher = None

    def notify_student(self,cmd,data):
        if self.sender != None:
            self.sender.sendall_with_size([cmd,data])

    def send_frame_to_student(self,frame):
        self.video_sender.send_video_frame(frame)

    def send_sound_to_student(self,sound):
        self.sound_sender.sendall_with_size(sound)

    def set_sender(self, sender):
        self.sender = sender

    def set_video_sender(self,video_sender):
        self.video_sender = video_sender

    def set_sound_sender(self,sound_sender):
        self.sound_sender = sound_sender    

    def disconnected(self):
        if self.teacher != None:
            self.teacher.remove_student_handler(self)

