from Student import Student
from ClientSocket import ClientSocket
import constant

import socket
import sys
import struct
import pickle

def main():
    
    sender, student_id, room_list = create_sender()
    receiver = create_receiver(student_id)
    Thread(target=self.receiver_handler, args=(receiver).start())


    try:
        while True:
            command = input()
            command = str(command).strip().split(" ")
            if command[0] == "join":
                room_id = command[1]
                sender.sendall_with_size([constant.JOIN_ROOM,command[1]])
            elif command[0] == "refresh_room":
                sender.sendall_with_size([constant.REFRESH_ROOM_LIST])
            elif command[0] == "send":
                msg = command[1]
                sender.sendall_with_size([constant.SEND_MSG,msg])
            elif command[0] == "leave_room":
                sender.sendall_with_size([constant.LEAVE_ROOM])
            elif command[0] == "refresh_mat":
                sender.sendall_with_size([constant.REFRESH_MATERIAL])
    except KeyboardInterrupt:
        pass
    finally:
        sender.close()
        receiver.close()

def connect_to_server(socket,host,port):
    try:
        socket.connect((host, port))
        return socket
    except:
        print("Connection error")
        sys.exit()

def create_sender():
    ''' if can connect to server this will return (sender,student_id,room_list) '''
    soc = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = constant.PORT                # Reserve a port for your service.

    soc = connect_to_server(soc,host,port)
    sender = ClientSocket(soc)

    data = []
    data.append(constant.I_AM_STUDENT_SENDER)
    data.append(Student("Nattaphol Srisa"))
    sender.sendall_with_size(data)
    
    decoded_input = sender.recv_with_size_and_decode()
    student_id = decoded_input[0]
    room_list = decoded_input[1]
    return (sender,student_id,room_list)

def create_receiver(student_id):
    ''' if can connect to server this will return receiver '''
    soc = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = constant.PORT                # Reserve a port for your service.
    
    soc = connect_to_server(soc,host,port)
    receiver = ClientSocket(soc)

    data = [constant.I_AM_STUDENT_RECEIVER,student_id]
    receiver.sendall_with_size(data)

    is_success = receiver.recv_with_size_and_decode()
    print("create_receiver is ",is_success)

    return receiver

def receiver_handler(receiver):
    pass

if __name__ == "__main__":
    main()