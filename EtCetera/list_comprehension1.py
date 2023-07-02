students = [
    {"name": "Ayush", "house": "Noida"},
    {"name": "Shubham", "house": "Kanpur"},
    {"name": "Sumit", "house": "Kanpur"},
    {"name": "Siddh", "house": "Kanpur"},
]

kanpurs = [
    student["name"] for student in students if student["house"] == "Kanpur"
]

for kanpur in sorted(kanpurs):
    print(kanpur)