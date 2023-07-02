def main():
    yell("This", "is", "CS50")

def yell(*words):
    upercased = map(str.upper, words)
    print(*upercased)

if __name__ == "__main__":
    main()
