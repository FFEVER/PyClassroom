from Teacher import Teacher
from Student import Student


class Room():
    def __init__(self,id,name,max_student,teacher,description):
        self.id = id
        self.name = name
        self.max_student = max_student
        self.teacher = teacher
        self.description = description
        self.materials = []

    def set_id(self, id):
        self.id = id

    def add_material(self,material):
        self.materials.append(material)

    def set_materials(self,materials):
        self.materials = materials

    def __str__(self):
        return str(self.id) + " " + self.name + " " + self.description