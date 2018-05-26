import socket
import sys
import traceback
from threading import Thread, Timer
import pickle
import struct

from StudentHandler import StudentHandler
from TeacherHanlder import TeacherHanlder
from ClientSocket import ClientSocket
import constant

class Server:
    def __init__(self):
        self.room_list = []     # list of room
        self.teacher_list = {}  # dict of teacher handler -> {room_id : teacherHandler}
        self.student_list = []  # list of student handler
        self.room_count = 0

    def start_server(self):
        self.inactive_handler()

        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire
        print("Socket created")

        host = socket.gethostname()
        port = constant.PORT         # arbitrary non-privileged port

        try:
            soc.bind((host, port))
        except:
            print("Bind failed. Error : " + str(sys.exc_info()))
            sys.exit()

        soc.listen(5)       # queue up to 5 requests
        print("Socket now listening")

        try:
            # infinite loop- do not reset for every requests
            while True:
                cli_soc, address = soc.accept()
                connection = ClientSocket(cli_soc)
                
                ip, port = str(address[0]), str(address[1])
                print("Incoming connection -> " + ip + ":" + port)
                try:
                    Thread(target=self.manage_incoming_connection, args=(connection, ip, port)).start()
                except:
                    print("Thread did not start.")
                    traceback.print_exc()
        except KeyboardInterrupt:
            pass
        finally:
            # Clean up.
            for room_id in self.teacher_list:
                self.teacher_list[room_id].socket.close()
            for student_handler in self.student_list:
                student_handler.socket.close()
            soc.close()

    def manage_incoming_connection(self, connection, ip, port):
        '''Differentiate between Student or Teacher'''

        decoded_input = connection.recv_with_size_and_decode()
        print(decoded_input)

        if decoded_input[0] == "Teacher":
            # room
            room = decoded_input[1]
            self.room_count += 1
            room.set_id(self.room_count)
            self.room_list.append(room)

            # teacher
            teacher = room.teacher
            # response to teacher
            connection.sendall_with_size(["room_id",str(room_count)])
            # teacher handler
            teacherHandler = TeacherHanlder(self,connection,teacher,room)
            self.teacher_list[room.id] = teacherHandler
            teacherHandler.start()

        elif decoded_input[0] == "Student":
            student = decoded_input[1]
            # send room list to student
            connection.sendall_with_size(self.room_list)
            # student handler
            studentHandler = StudentHandler(self,connection,student)
            self.student_list.append(studentHandler)
            studentHandler.start()

        else:
            connection.sendall_with_size("Error: You are not teacher or student.")
            connection.close()


    def inactive_handler(self):
        Timer(1.0,self.inactive_handler).start()

        inactive_room = []
        for room_id in self.teacher_list:
            if not self.teacher_list[room_id].isAlive():
                inactive_room.append(room_id)

        for room_id in inactive_room:
            del self.teacher_list[room_id]
        self.room_list = [room for room in self.room_list if room.id not in inactive_room]


        for student in self.student_list:
            if not student.isAlive():
                student.alive = False
        self.student_list = [student for student in self.student_list if student.alive]

if __name__ == "__main__":
    server = Server()
    server.start_server()
