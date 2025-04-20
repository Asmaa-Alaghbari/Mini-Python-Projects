import random


def roll_dice():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    print(f"You rolled a {x} and a {y}.")


while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice != "n":
        if choice == "y":
            roll_dice()
        else:
            print("Invalid choice!")
    else:
        print("Thank for playing!")
        break
