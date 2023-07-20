def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)

# yield return one value at a time
def sheep(n):
    flock = []
    for i  in range(n):
        yield "🐏" * i

if __name__ == "__main__":
    main()