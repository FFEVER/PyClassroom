import socket
import sys
import struct
import pickle

def teacher():
    soc = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 8888                # Reserve a port for your service.

    try:
        soc.connect((host, port))
    except:
        print("Connection error")
        sys.exit()

    print("Enter 'quit' to exit")
    message = input(" -> ")

    while message != 'quit':    
        packet = pickle.dumps(message)
        packet_len = struct.pack('>L', len(packet))
        print(packet_len)
        soc.sendall(packet_len + packet)

        message = input(" -> ")

    soc.send(b'--quit--')
    soc.close()

if __name__ == "__main__":
    main()