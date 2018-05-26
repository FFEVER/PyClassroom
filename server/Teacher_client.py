from Teacher import Teacher
from Room import Room
from ClientSocket import ClientSocket
import constant 

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
        sender = ClientSocket(soc)
    except:
        print("Connection error")
        sys.exit()
    data = []
    data.append("Teacher")
    data.append(Room(0,"JavaScript",50,Teacher("John Smith"),"This is a javascript class."))
    sender.sendall_with_size(data)
    
    is_room_created = sender.recv_with_size_and_decode()
    print(is_room_created)

    while True:
        command = input()
        command = str(command).strip().split(" ")
        if command[0] == "start_live":
            sender.sendall_with_size([constant.START_LIVE])
        elif command[0] == "end_live":
            sender.sendall_with_size([constant.END_LIVE])
        elif command[0] == "add_mat":
            material = command[1]
            sender.sendall_with_size([constant.ADD_MATERIAL,material])
        elif command[0] == "remove_mat":
            material = command[1]
            sender.sendall_with_size([constant.REMOVE_MATERIAL,material])
        elif command[0] == "kick":
            student_name = command[1]
            sender.sendall_with_size([constant.KICK_STUDENT,student_name])
        elif command[0] == "close_room":
            sender.sendall_with_size([constant.CLOSE_ROOM])

    soc.close()

if __name__ == "__main__":
    main()