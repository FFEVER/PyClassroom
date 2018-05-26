import cv2
from threading import Thread

class StreamerThread(Thread):
    def __init__(self):
        super().__init__()
        self.streaming = False

    def toggle(self):
        self.streaming = not self.streaming

    def stop(self):
        self.streaming = False

    def run(self):
        self.streaming = True
        cap = cv2.VideoCapture(0)

        while cap.isOpened() and self.streaming:
            ret, frame = cap.read()
            img_string = cv2.imencode('.jpg', frame)[1].tostring()
            #send(img_stirng)
            cv2.imshow('Streaming', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
        
