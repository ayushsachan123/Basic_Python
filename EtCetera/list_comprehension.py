def main():
    yell("This", "is", "CS50")

def yell(*words):
    upercased = [word.upper() for word in words]
    print(*upercased)

if __name__ == "__main__":
    main()
