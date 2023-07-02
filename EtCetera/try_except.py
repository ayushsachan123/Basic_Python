def main():
    x = get_int("What's x?")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("x is not an integer")
            #Instead of printing again and again we can use pass it will not end the loop but simply pass it
            # pass
        else:
            return x

main()

# We will run else only when we succeed int try otherwise will will not run else block
# Else will help to handle the name error
# Except will help to handle the value error