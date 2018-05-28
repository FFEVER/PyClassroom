from threading import Thread
import pickle
import socket
import sys
import struct

from ClientSocket import ClientSocket
from VideoHandler import VideoHandler
from SoundHandler import SoundHandler
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
        self.video_receiver = None
        self.sound_receiver = None
        self.video_handler = None
        self.sound_handler = None

        self.room = room
        self.student_list = []  # list of studentHandler

    def run(self):
        print("Teacher Thread:", self.teacher)
        print(self.room)

        while True:
            if self.sender == None:
                continue
            decoded_input = self.receiver.recv_with_size_and_decode()
            if decoded_input == None:
                self.disconnected()
                return

            command = decoded_input[0]
            if command == constant.START_LIVE:
                self.cmd_start_live()
            elif command == constant.END_LIVE:
                self.cmd_end_live()
            elif command == constant.ADD_MATERIAL:
                materials = decoded_input[1]
                self.cmd_added_material(materials)
            elif command == constant.REMOVE_MATERIAL:
                material = decoded_input[1]
                self.cmd_remove_material(materials)
            elif command == constant.KICK_STUDENT:
                student_id = decoded_input[1]
                self.cmd_kick_student(student_id)
            elif command == constant.CLOSE_ROOM:
                self.cmd_close_room()
                return

    def cmd_start_live(self):
        print(self.teacher.name, "starting a live.")
        self.notify_all_student(constant.START_LIVE,None)
        self.video_handler = VideoHandler(self.student_list,self.video_receiver)
        self.sound_handler = SoundHandler(self.student_list,self.sound_receiver)
        self.video_handler.start()
        self.sound_handler.start()

    def cmd_end_live(self):
        print(self.teacher.name, "end a live.")
        self.notify_all_student(constant.END_LIVE,None)
        self.video_handler.stop()
        self.sound_handler.stop()
        self.video_handler = None
        self.sound_handler = None

    def cmd_added_material(self, materials):
        print(self.teacher.name, "added a materail ->", materials)
        self.room.set_materials(materials)
        self.notify_all_student(constant.REFRESH_MATERIAL, materials)

    def cmd_remove_material(self, materials):
        print(self.teacher.name, "removed a materail ->", material)
        self.room.set_materials(materials)
        self.notify_all_student(constant.REFRESH_MATERIAL, materials)

    def cmd_kick_student(self, student_id):
        print(self.teacher.name, "kick student ->", student_id)
        target = None
        for studentHandler in self.student_list:
            if studentHandler.student.id == student_id:
                studentHandler.teacher = None
                target = studentHandler
                studentHandler.notify_student(constant.KICK_STUDENT, None)
        self.student_list.remove(target)

        student_data_list = []
        for studentHandler in self.student_list:
            student_data_list.append(studentHandler.student)
        self.notify_all_student(
            constant.STUDENT_LIST_UPDATED, student_data_list)
        self.notify_teacher(constant.STUDENT_LIST_UPDATED, student_data_list)

    def cmd_close_room(self):
        print(self.teacher.name, "closed a room.")
        self.disconnected()

    def add_student_handler(self, studentHandler):
        if len(self.student_list) >= self.room.max_student:
            studentHandler.teacher = None
            return studentHandler.notify_student(constant.JOIN_ROOM_FAIL, "Room is full.")
        
        self.student_list.append(studentHandler)
        student_data_list = []
        for studentHandler in self.student_list:
            student_data_list.append(studentHandler.student)

        studentHandler.notify_student(constant.JOIN_ROOM_SUCCESS, [self.room,student_data_list])

        self.notify_all_student(
            constant.STUDENT_LIST_UPDATED, student_data_list)
        self.notify_teacher(constant.STUDENT_LIST_UPDATED, student_data_list)

        if self.video_handler != None and self.sound_handler != None:
            print("Enter while live")
            studentHandler.notify_student(constant.START_LIVE,None)
            self.video_handler.update_student_list(self.student_list)

    def remove_student_handler(self, studentHandler):
        self.student_list.remove(studentHandler)
        student_data_list = []
        for studentHandler in self.student_list:
            student_data_list.append(studentHandler.student)
        self.notify_all_student(
            constant.STUDENT_LIST_UPDATED, student_data_list)
        self.notify_teacher(constant.STUDENT_LIST_UPDATED, student_data_list)

        if self.video_handler != None and self.sound_handler != None:
            print("Leave while live")
            self.video_handler.update_student_list(self.student_list)

    def notify_all_student(self, cmd, data):
        for student in self.student_list:
            student.notify_student(cmd, data)

    def notify_teacher(self, cmd, data):
        if self.sender != None:
            self.sender.sendall_with_size([cmd, data])

    def set_sender(self, sender):
        self.sender = sender

    def set_video_receiver(self,video_receiver):
        self.video_receiver = video_receiver

    def set_sound_receiver(self,sound_receiver):
        self.sound_receiver = sound_receiver

    def disconnected(self):
        ''' Clean up after teacher disconnected'''
        # tell every student that teacher has disconnected
        for student in self.student_list:
            student.teacher = None
            student.notify_student(constant.CLOSE_ROOM,
                                   "The room has been closed.")
        self.sender.close()
        self.receiver.close()
