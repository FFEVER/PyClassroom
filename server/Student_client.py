from Student import Student
from ClientSocket import ClientSocket
import constant

import socket
import sys
import struct
import pickle

def main():
    soc = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = constant.PORT                # Reserve a port for your service.

    try:
        soc.connect((host, port))
        cli_socket = ClientSocket(soc)
    except:
        print("Connection error")
        sys.exit()
    data = []
    data.append("Student")
    data.append(Student("Nattaphol Srisa"))
    cli_socket.sendall_with_size(data)
    
    room_list = cli_socket.recv_with_size_and_decode()
    print(room_list)

    while True:
        command = input()
        command = str(command).strip().split(" ")
        if command[0] == "join":
            room_id = command[1]
            cli_socket.sendall_with_size([constant.JOIN_ROOM,command[1]])
        elif command[0] == "refresh_room":
            cli_socket.sendall_with_size([constant.REFRESH_ROOM_LIST])
        elif command[0] == "send":
            msg = command[1]
            cli_socket.sendall_with_size([constant.SEND_MSG,msg])
        elif command[0] == "leave_room":
            cli_socket.sendall_with_size([constant.LEAVE_ROOM])
        elif command[0] == "refresh_mat":
            cli_socket.sendall_with_size([constant.REFRESH_MATERIAL])

    soc.close()

if __name__ == "__main__":
    main()