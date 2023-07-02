# we can add comment in file by also using """ """ triple code
def meow(n: int) -> str:
    """ meow n times"""
    #or
    """
    Meow n times.
    
    :param n: number of times to meow
    :type n: int
    :raise TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")