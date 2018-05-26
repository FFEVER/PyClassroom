from Teacher import Teacher
from Room import Room
from ClientSocket import ClientSocket
import constant 

import socket
import sys
import struct
import pickle

def main():
    sender,room_id = create_sender()
    receiver = create_receiver(room_id)
    Thread(target=self.receiver_handler, args=(receiver).start())
    
    try:
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
    ''' if can connect to server this will return (sender,room_id) '''
    soc = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = constant.PORT                # Reserve a port for your service.
    
    soc = connect_to_server(soc,host,port)
    sender = ClientSocket(soc)

    data = []
    data.append(constant.I_AM_TEACHER_SENDER)
    data.append(Room(0,"JavaScript",50,Teacher("John Smith"),"This is a javascript class."))
    sender.sendall_with_size(data)
    
    decoded_input = sender.recv_with_size_and_decode()
    is_room_created = decoded_input[0]
    room_id = decoded_input[1]
    print(is_room_created,"with id",room_id)
    return (sender,room_id)

def create_receiver(room_id):
    ''' if can connect to server this will return receiver '''
    soc = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = constant.PORT                # Reserve a port for your service.
    
    soc = connect_to_server(soc,host,port)
    receiver = ClientSocket(soc)

    data = [constant.I_AM_TEACHER_RECEIVER,room_id]
    receiver.sendall_with_size(data)

    is_success = receiver.recv_with_size_and_decode()
    print("create_receiver is ",is_success)

    return receiver 


def receiver_handler(receiver):
    pass


if __name__ == "__main__":
    main()