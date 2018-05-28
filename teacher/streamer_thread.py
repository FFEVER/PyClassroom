import cv2
from threading import Thread

class StreamerThread(Thread):
    def __init__(self,video_sender):
        super().__init__()
        self.streaming = False
        self.video_sender = video_sender

    def toggle(self):
        self.streaming = not self.streaming

    def stop(self):
        self.streaming = False

    def run(self):
        self.streaming = True
        cap = cv2.VideoCapture(0)
        #Thread(target = self.send_to_server).start()

        while cap.isOpened() and self.streaming:
            ret, frame = cap.read()
            img_string = cv2.imencode('.jpg', frame)[1].tostring()
            cv2.imshow('Streaming', frame)
            self.video_sender.send_video_frame(img_string)
            cv2.waitKey(1)

        cap.release()
        cv2.destroyAllWindows()
        print("Streamer ended")

        
