from threading import Thread
import pickle
import socket
import sys
import struct

from ClientSocket import ClientSocket
from Teacher import Teacher
import constant


class SoundHandler(Thread):
    def __init__(self,student_list,sound_receiver):
        Thread.__init__(self)
        self.student_list = student_list
        self.sound_receiver = sound_receiver
        self.is_running = True

    def run(self):
        while self.is_running:
            sound = self.sound_receiver.recv_with_size_and_decode()
            self.send_sound_to_all_student(sound)

    def send_sound_to_all_student(self,sound):
        for studentHandler in self.student_list:
            studentHandler.send_sound_to_student(sound)

    def stop(self):
        self.is_running = False