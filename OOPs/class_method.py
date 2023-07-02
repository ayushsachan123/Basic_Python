import random
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
# sort is only one so we use as classmethod we pass clas as a reference of class
# house can be access by cls.houses because it is the house variable
    @classmethod
    def sort(cls,name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry")