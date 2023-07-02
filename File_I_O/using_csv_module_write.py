import csv

name = input("What's your Name? ")
home = input("Where's your home? ")

# Using writer

# with open("students_write.csv","a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name,home])


# Using DictWriter

with open("students_write.csv","a") as file:
     writer = csv.DictWriter(file, fieldnames=["name","home"])
     writer.writerow({"name": name,"home":home})

