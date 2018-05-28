from threading import Thread

from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave
from threading import Thread

THRESHOLD = 500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 44100

class SoundStreamerThread(Thread):
    def __init__(self,sound_sender):
        super().__init__()
        self.streaming = False
        self.sound_sender = sound_sender

    def toggle(self):
        self.streaming = not self.streaming

    def stop(self):
        self.streaming = False

    def run(self):
        self.streaming = True

        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=1, rate=RATE,
                            input=True, output=True,
                            frames_per_buffer=CHUNK_SIZE)

        while self.streaming:
            snd_data = stream.read(CHUNK_SIZE)
            self.sound_sender.send_sound(snd_data)

        print("Sound Streamer ended")

        
