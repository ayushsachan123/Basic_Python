import sys

#by using sys.argv[1] we does not need to take input from user and then print it. The user can
#directly give input at the time of file running
# we does not take sys.argv[0] because it is the name of the program

# try:
#     print("hello, my name is", sys.argv[1])
# except IndexError:
#     print("Two few argument")

#                  or

if len(sys.argv)<2:
    sys.exit("Too few Argument")
elif len(sys.argv) > 2:
    sys.exit("Too many Argument")

print("hello, my name is", sys.argv[1])

#               or
#If we want to print many input from the user
if len(sys.argv)<2:
    sys.exit("Too few Argument")

for arg in sys.argv[1:]:
    print("hello, my name is",arg)

