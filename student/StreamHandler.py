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
        self.parent = parent
        self.video_receiver = video_receiver
        self.is_running = True

    def run(self):
        print("StreamHandler running")
        while self.is_running:
            # print("frame run")
            data = self.video_receiver.recv_video_frame()
            if data == None:
                print("None")
                continue
            try:
                print(len(data))
                self.parent.set_stream_string(data)
            except:
                pass
        print("Student stream end")


    def stop(self):
        self.is_running = False