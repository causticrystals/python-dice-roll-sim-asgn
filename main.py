# Dice Roll Simulator Assignment

# Import math things
import math
import random

# Main Program Loop
loop = True
while loop:

    # Print main menu
    print("\nDice Roll Simulator Menu")
    print("1. Roll Dice Once")
    print("2. Roll Dice 5 Times")
    print("3. Roll Dice 'n' Times ")
    print("4. Roll Dice Until Snake Eyes")
    print("5. Exit")

    # Menu selection from user
    selection = input("Select an option (1-5): ")

    # Action taken based on selection
    if selection == "1":
        print("Roll Dice Once")

        dice1 = random.randrange(1, 7)
        dice2 = random.randrange(1, 7)
        dice_sum = dice1 + dice2
        print(str(dice1) + "," + str(dice2) + " (sum: " + str(dice_sum) + ")")
    elif selection == "2":
        print("Roll Dice 5 Times")

        n = 1
        while n <= 5:
            dice1 = random.randrange(1, 7)
            dice2 = random.randrange(1, 7)
            dice_sum = dice1 + dice2
            print(str(dice1) + "," + str(dice2) +
                  " (sum: " + str(dice_sum) + ")")
            n += 1
    elif selection == "3":
        print("Roll Dice 'n' Times")

        roll_amount = input("How many rolls would you like? ")
        for n in range(int(roll_amount)):
            dice1 = random.randrange(1, 7)
            dice2 = random.randrange(1, 7)
            dice_sum = dice1 + dice2
            print(str(dice1) + "," + str(dice2) +
                  " (sum: " + str(dice_sum) + ")")
    elif selection == "4":
        print("Roll Dice Until Snake Eyes")

        # Totals
        dice_rolls = 0
    elif selection == "5":
        print("EXIT")
        loop = False
