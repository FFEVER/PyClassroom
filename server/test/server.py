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
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.

a_list = [Item('A'),Item('B'),Item('C')]
try:
    while True:
        c, addr = s.accept()     # Establish connection with client.
        print ('Got connection from', addr)
        # c.send('Thank you for connecting'.encode('utf-8'))
        c.send(pickle.dumps(a_list))
        c.close()
except:
    c.close()