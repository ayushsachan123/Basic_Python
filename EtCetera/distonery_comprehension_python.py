students = ["Hermione","Harry","Ron"]

# gryffindors = []
#
# for student in students:
#     gryffindors.append({"name":student, "house": "Gryffindor"})

#or
gryffindors = [{"name":student, "house": "Gryffindor"} for student in students]

# or if we want same list
gryffindors = {student: "Gryffindor" for student in students}


print(gryffindors)