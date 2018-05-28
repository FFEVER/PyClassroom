from threading import Thread
import pickle
import socket
import sys
import struct
import pyaudio

from ClientSocket import ClientSocket
import constant


THRESHOLD = 500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 44100

class SoundStreamHandler(Thread):
    def __init__(self,parent,sound_receiver):
        Thread.__init__(self)
        self.parent = parent
        self.sound_receiver = sound_receiver
        self.is_running = True

    def run(self):
        print("SoundStreamHandler running")

        pa = pyaudio.PyAudio()
        stream = pa.open(format=FORMAT,channels=1,rate=RATE,output=True)
        while self.is_running:
            sound = self.sound_receiver.recv_sound(CHUNK_SIZE)
            if not sound:
                break
            stream.write(data)

        print("Student sound stream end")


    def stop(self):
        self.is_running = False