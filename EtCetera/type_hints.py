# :int - it just a hint, an annotation to python that this variable on
# the left i.e n should be an int
# -> None it tells that function is returning none
def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")