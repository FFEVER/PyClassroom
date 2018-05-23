from Student import Student

import socket
import sys
import struct
import pickle

def main():
    soc = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 8888                # Reserve a port for your service.

    try:
        soc.connect((host, port))
    except:
        print("Connection error")
        sys.exit()
    data = []
    data.append("Student")
    data.append(Student("Nattaphol Srisa"))
    sendall_with_size(soc,data)
    
    decoded_input = recv_with_size_and_decode(soc)
    print(decoded_input)

    soc.close()

def sendall_with_size(soc,data):
    packet = pickle.dumps(data)
    packet_len = struct.pack('>L', len(packet))
    soc.sendall(packet_len + packet)

def recv_with_size_and_decode(sock):
        # Get buffer size by reading the first 4 bytes of a buffer
        raw_buffer_size = recv_n(sock,4)
        if(raw_buffer_size == None):
            print("Error: buffer_size can't be None type")
            sock.close()
            return
        # decode buffer from binary to integer by unpacking
        buffer_size = struct.unpack('>L',raw_buffer_size)[0]

        # get the data from buffer
        client_input = recv_n(sock,buffer_size)
        
        decoded_input = pickle.loads(client_input)

        return decoded_input
        
def recv_n(sock, n):
    ''' recv n bytes or return None if EOF is hit '''
    data = b''
    while len(data) < n:
        packet = sock.recv(n - len(data))
        if not packet:
            return None
        data += packet
    return data

if __name__ == "__main__":
    main()