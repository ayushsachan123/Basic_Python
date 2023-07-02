# with open("names.csv") as file:
#     for line in file:
#         name,house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

students = []
with open("names.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

# Sort the list of dictonary using key name

for student in sorted(students, key =lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

