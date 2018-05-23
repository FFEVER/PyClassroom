from Teacher import Teacher
from Student import Student


class Room():
    def __init__(self,id,name,max_student,teacher,description):
        self.id = id
        self.name = name
        self.max_student = max_student
        self.teacher = teacher
        self.student = []
        self.description = description

    def set_id(self, id):
        self.id = id

    def __str__(self):
        return str(self.id) + " " + self.name + " " + self.description