name = input("What's your name? ")
# with automatically close the file
with open("names.txt", "a") as file:
    file.write(f"{name}\n")


