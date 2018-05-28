from Teacher import Teacher
from Room import Room
from ClientSocket import ClientSocket
import constant

import socket
import sys
import struct
import pickle
from threading import Thread
import traceback


def main():
    sender, room_id = create_sender()
    receiver = create_receiver(room_id)
    try:
        Thread(target=receiver_handler, args=(receiver,)).start()
    except:
        print("Thread did not start.")
        traceback.print_exc()

    materials = []
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
                materials.append(material)
                sender.sendall_with_size([constant.ADD_MATERIAL, materials])
            elif command[0] == "remove_mat":
                material = command[1]
                sender.sendall_with_size([constant.REMOVE_MATERIAL, material])
            elif command[0] == "kick":
                student_name = command[1]
                sender.sendall_with_size([constant.KICK_STUDENT, student_name])
            elif command[0] == "close_room":
                sender.sendall_with_size([constant.CLOSE_ROOM])
                sys.exit(1)
    except KeyboardInterrupt:
        pass
    finally:
        sender.close()
        receiver.close()


def connect_to_server(socket, host, port):
    try:
        socket.connect((host, port))
        return socket
    except:
        print("Connection error")
        sys.exit()


def create_sender():
    ''' if can connect to server this will return (sender,room_id) '''
    soc = socket.socket()         # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = constant.PORT                # Reserve a port for your service.

    soc = connect_to_server(soc, host, port)
    sender = ClientSocket(soc)

    data = []
    data.append(constant.I_AM_TEACHER_SENDER)
    data.append(Room(0, "JavaScript", 2, Teacher(
        "John Smith"), "This is a javascript class."))
    sender.sendall_with_size(data)

    decoded_input = sender.recv_with_size_and_decode()
    is_room_created = decoded_input[0]
    room_id = decoded_input[1]
    print(is_room_created, "with id", room_id)
    return (sender, room_id)


def create_receiver(room_id):
    ''' if can connect to server this will return receiver '''
    soc = socket.socket()         # Create a socket object
    host = socket.gethostname()  # Get local machine name
    port = constant.PORT                # Reserve a port for your service.

    soc = connect_to_server(soc, host, port)
    receiver = ClientSocket(soc)

    data = [constant.I_AM_TEACHER_RECEIVER, room_id]
    receiver.sendall_with_size(data)

    is_success = receiver.recv_with_size_and_decode()
    print("create_receiver is ", is_success)

    return receiver


def receiver_handler(receiver):
    while True:
        decoded_input = receiver.recv_with_size_and_decode()
        if decoded_input == None:
            print("Server has down.")
            sys.exit(1)
            break
        # print(decoded_input)
        cmd = decoded_input[0]
        if cmd == constant.STUDENT_LIST_UPDATED:
            student_list = decoded_input[1]
            print_list(student_list)
        elif cmd == constant.MESSAGE_FROM_STUDENT:
            data = decoded_input[1]
            student = data[0]
            msg = data[1]
            # Please check if it is your own msg, so don't print it.
            print(student,": ",msg)
            
            


def print_list(data_list):
    print("[", end="")
    for item in data_list:
        print(item, end=",")
    print("]")


if __name__ == "__main__":
    main()
