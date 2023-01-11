# Dice Roll Simulator Assignment

import random

n = 1
while n <= 5:
    # Flip a Coin
    randNum = random.randrange(1, 3)
    if randNum == 1:
        print("Heads")
    else:
        print("Tails")

    # Increment n
    n += 1

print("Goodbye")
