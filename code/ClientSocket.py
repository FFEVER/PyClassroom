import socket
import sys
import pickle
import struct
from sys import byteorder


class ClientSocket():
    def __init__(self, socket):
        self.socket = socket

    def recv_with_size_and_decode(self):
        # Get buffer size by reading the first 4 bytes of a buffer
        raw_buffer_size = self.recv_n(4)
        if(raw_buffer_size == None):
            self.close()
            return None
        # decode buffer from binary to integer by unpacking

        try:
            buffer_size = struct.unpack('>L', raw_buffer_size)[0]
        except struct.error:
            return "struct error"

        # get the data from buffer
        client_input = self.recv_n(buffer_size)

        decoded_input = pickle.loads(client_input)

        return decoded_input

    def recv_n(self, n):
        ''' recv n bytes or return None if EOF is hit '''
        data = b''
        try:
            while len(data) < n:
                packet = self.socket.recv(n - len(data))
                if not packet:
                    return None
                data += packet
        except:
            # print("Connection has dropped.")
            pass
        return data

    def sendall_with_size(self, data):
        packet = pickle.dumps(data)
        size = struct.pack('>L', len(packet))
        self.socket.sendall(size + packet)

    def send_video_frame(self, frame):
        packet = pickle.dumps(frame)
        size = struct.pack('L', len(packet))
        self.socket.sendall(size + packet)

    def recv_video_frame(self):
        data = b""
        payload_size = struct.calcsize("L")

        try:
            while len(data) < payload_size:
                data += self.socket.recv(4096)
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("L", packed_msg_size)[0]
            while len(data) < msg_size:
                data += self.socket.recv(4096)
            frame_data = data[:msg_size]
            data = data[msg_size:]

            frame = pickle.loads(frame_data)
            return frame
        except ConnectionResetError:
            return None
        except ConnectionAbortedError:
            return None
        except ConnectionRefusedError:
            return None
        except ConnectionError:
            return None

    def send_sound(self,sound):
        if byteorder == 'big':
            sound.byteswap()
        self.socket.send(sound)

    def receive_sound(self,chunk_size):
        data = self.socket.recv(chunk_size)
        return data

    def close(self):
        self.socket.close()
