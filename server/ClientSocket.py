import socket
import sys
import pickle
import struct

class ClientSocket():
    def __init__(self,socket):
        self.socket = socket

    def recv_with_size_and_decode(self):
        # Get buffer size by reading the first 4 bytes of a buffer
        raw_buffer_size = self.recv_n(4)
        if(raw_buffer_size == None):
            self.close()
            return None
        # decode buffer from binary to integer by unpacking
        buffer_size = struct.unpack('>L',raw_buffer_size)[0]

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
            print("Connection has dropped.")
        return data

    def sendall_with_size(self,data):
        packet = pickle.dumps(data)
        size = struct.pack('>L',len(packet))
        self.socket.sendall(size + packet)

    def close(self):
        self.socket.close()