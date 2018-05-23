import socket
import sys
import traceback
from threading import Thread
import pickle
import struct

from StudentHandler import StudentHandler
from TeacherHanlder import TeacherHanlder

class Server:
    def __init__(self):
        self.room_list = []      # list of room
        self.teacher_list = []  # list of teacher handler
        self.student_list = []  # list of student handler
        self.room_count = 0

    def start_server(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   # SO_REUSEADDR flag tells the kernel to reuse a local socket in TIME_WAIT state, without waiting for its natural timeout to expire
        print("Socket created")

        host = socket.gethostname()
        port = 8888         # arbitrary non-privileged port

        try:
            soc.bind((host, port))
        except:
            print("Bind failed. Error : " + str(sys.exc_info()))
            sys.exit()

        soc.listen(5)       # queue up to 5 requests
        print("Socket now listening")

        # infinite loop- do not reset for every requests
        while True:
            connection, address = soc.accept()
            ip, port = str(address[0]), str(address[1])
            print("Incoming connection -> " + ip + ":" + port)
            try:
                Thread(target=self.manage_incoming_connection, args=(connection, ip, port)).start()
            except:
                print("Thread did not start.")
                traceback.print_exc()

        soc.close()

    def manage_incoming_connection(self, connection, ip, port):
        '''Differentiate between Student or Teacher'''

        decoded_input = self.recv_with_size_and_decode(connection)
        print(decoded_input)

        if decoded_input[0] == "Teacher":
            # room
            room = decoded_input[1]
            self.room_count += 1
            room.set_id(self.room_count)
            self.room_list.append(room)

            # teacher
            teacher = room.teacher
            # teacher handler
            teacherHandler = TeacherHanlder(self,connection,teacher,room)
            self.teacher_list.append(teacherHandler)
            teacherHandler.start()
            # response to teacher
            self.sendall_with_size(connection,"Create room successfully.")

        elif decoded_input[0] == "Student":
            student = decoded_input[1]
            # send room list to student
            self.sendall_with_size(connection,self.room_list)
            # student handler
            studentHandler = StudentHandler(self,connection,student)
            self.student_list.append(studentHandler)
            studentHandler.start()

        else:
            self.sendall_with_size(connection,"Error: You are not teacher or student.")
            connection.close()

    def recv_with_size_and_decode(self,sock):
        # Get buffer size by reading the first 4 bytes of a buffer
        raw_buffer_size = self.recv_n(sock,4)
        if(raw_buffer_size == None):
            print("Error: buffer_size can't be None type")
            sock.close()
            return
        # decode buffer from binary to integer by unpacking
        buffer_size = struct.unpack('>L',raw_buffer_size)[0]

        # get the data from buffer
        client_input = self.recv_n(sock,buffer_size)
        
        decoded_input = pickle.loads(client_input)

        return decoded_input
        
    def recv_n(self, sock, n):
        ''' recv n bytes or return None if EOF is hit '''
        data = b''
        while len(data) < n:
            packet = sock.recv(n - len(data))
            if not packet:
                return None
            data += packet
        return data

    def sendall_with_size(self,sock,data):
        packet = pickle.dumps(data)
        size = struct.pack('>L',len(packet))
        sock.sendall(size + packet)

if __name__ == "__main__":
    server = Server()
    server.start_server()
