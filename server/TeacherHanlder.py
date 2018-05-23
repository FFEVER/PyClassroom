from Teacher import Teacher
from threading import Thread
import pickle
import socket
import sys
import struct

class TeacherHanlder(Thread):
    def __init__(self,server,socket,teacher,room):
        Thread.__init__(self)
        self.server = server
        self.teacher = teacher
        self.socket = socket
        self.room = room

    def run(self):
        print("Teacher thread:",self.teacher,self.room)