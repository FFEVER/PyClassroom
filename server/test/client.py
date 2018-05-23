import socket               # Import socket module
import pickle

class Item():
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 12347                # Reserve a port for your service.

s.connect((host, port))
a_list = pickle.loads(s.recv(1024))
for a in a_list:
    print(a)
s.close                     # Close the socket when done