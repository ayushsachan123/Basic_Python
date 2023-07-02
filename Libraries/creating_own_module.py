def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")

# if we directly write main and at second file we import that file then
#main will also execute and print the whole function
#__name__ - This is special variable whose value is automatically set by the python as "main" when we
#run the file from command line

if __name__ == "__main__":
 main()
