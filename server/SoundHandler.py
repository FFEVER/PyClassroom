from threading import Thread
import pickle
import socket
import sys
import struct

from ClientSocket import ClientSocket
import constant


class VideoHandler(Thread):
    def __init__(self,student_list,sound_receiver):
        Thread.__init__(self)
        self.student_list = student_list
        self.video_receiver = sound_receiver
        self.is_running = True

    def run(self):
        while self.is_running:
            sound = self.video_receiver.recv_video_frame()
            self.send_sound_to_all_student(sound)

    def send_sound_to_all_student(self,sound):
        for studentHandler in self.student_list:
            studentHandler.send_sound_to_student(sound)

    def update_student_list(self,student_list):
        self.student_list = student_list
        print("Current student in SoundHandler: ",len(self.student_list))

    def stop(self):
        self.is_running = False