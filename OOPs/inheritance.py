class Wizard:
    def __int__(self,name):
        if not name:
            raise ValueError("Mising name")
        self.name = name

class Student(Wizard):
    def __init__(self,name,house):
        super().__init__(name)
        self.house = house


class Professor(Wizard):
    def __int__(self,name,subject):
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry","Kanpur")
professor = Professor("Serverus","Science")

