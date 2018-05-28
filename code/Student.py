class Student():
    def __init__(self,name):
        self.name = name
        self.id = '0'
    def set_id(self,id):
        self.id = id
    def __str__(self):
        return self.name + "(" + self.id + ")"