# with open("names.txt","r") as file:
    # lines = file.readlines()
# end will not not generate a blank line that print will insert
# for line in lines:
#     print("hello,", line, end="")

# also line.rstrip() - to remove extra line


# or
# with open("names.txt","r") as file:
#     for line in file:
#         print("hello,", line.rstrip())



# Printing data in sorted order
# names = []
#
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
#
# for name in sorted(names):
#     print(f"hello, {name}")



# or we can sort directly
with open("names.txt") as file:
     for line in sorted(file):
         print("hello,", line.rstrip())

print("\n")
# print names in reverse order
with open("names.txt") as file:
    for line in sorted(file, reverse = True):
        print("hello,", line.rstrip())