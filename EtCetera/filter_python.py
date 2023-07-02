students = [
    {"name": "Ayush", "house": "noida"},
    {"name": "Shubham", "house": "kanpur"},
    {"name": "Sumit", "house": "kanpur"},
    {"name": "Siddh", "house": "kanpur"},
]

def is_kanpur(s):
    return s["house"] == "kanpur"

# kanpurs = filter(is_kanpur, students)
#or
kanpurs = filter(lambda s: s["house"] == "kanpur", students)

for kanpur in sorted(kanpurs, key=lambda s: s["name"]):
    print(kanpur["name"])
