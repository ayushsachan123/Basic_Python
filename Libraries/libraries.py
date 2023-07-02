# import is used to bring different functions from the predefined module
import random

#choice takes the sequence and return a random number from that sequence
coin = random.choice(["heads","tails"])
print(coin)

#randint will generate the number between 1 and 10
number = random.randint(1,10)
print(number)

# shuffle It takes a list for instance of value and shuffle them
cards = ["jack","queen","King"]
random.shuffle(cards)
for card in cards:
    print(card)
