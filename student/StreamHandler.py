from threading import Thread
import pickle
import socket
import sys
import struct

from ClientSocket import ClientSocket
import constant


class StreamHandler(Thread):
    def __init__(self,parent,video_receiver):
        Thread.__init__(self)
        self.video_receiver = video_receiver
        self.is_running = True

    def run(self):
        while self.is_running:
            # print("frame run")
            self.video_receiver.recv_video_frame()
            # if frame == None:
            #     continue
            print(len(frame))


    def stop(self):
        self.is_running = False