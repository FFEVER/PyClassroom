from Student import Student
from threading import Thread
import pickle
import socket
import sys
import struct

class StudentHandler(Thread):
    def __init__(self,server,socket,student):
        Thread.__init__(self)
        self.server = server
        self.student = student
        self.socket = socket
        self.room = None

    def run(self):
        print("Student thread:", self.student)

