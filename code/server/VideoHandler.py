from threading import Thread
import pickle
import socket
import sys
import struct

from ClientSocket import ClientSocket
import constant


class VideoHandler(Thread):
    def __init__(self,student_list,video_receiver):
        Thread.__init__(self)
        self.student_list = student_list
        self.video_receiver = video_receiver
        self.is_running = True

    def run(self):
        while self.is_running:
            # print("frame run")
            frame = self.video_receiver.recv_video_frame()
            # if frame == None:
            #     continue
            # print(len(frame))
            self.send_frame_to_all_student(frame)

    def send_frame_to_all_student(self,frame):
        for studentHandler in self.student_list:
            studentHandler.send_frame_to_student(frame)

    def update_student_list(self,student_list):
        self.student_list = student_list
        print("Current student in VideoHandler: ",len(self.student_list))


    def stop(self):
        self.is_running = False