class Student:
    def __init__(self,name,house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

# _house bcz if we use house then the function name and variable will have same name
# we don't put _house in init bcz if we put _ then it avoid setter and directly assign the house str
#Getter
    @property
    def name(self):
        return self._name
#property created consist of name so use @name.setter
    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

#Setter
    @house.setter
    def house(self,house):
        if house not in ["Gryffindor","Hufflepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name,house)


if __name__ == "__main__":
    main()
