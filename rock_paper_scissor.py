import random

rock_paper_scissors = ("r", "p", "s")
rock_paper_scissors_icons = {"r": "🪨", "p": "📄", "s": "✂️"}

while True:
    user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
    computer_choice = random.choice(rock_paper_scissors)

    if user_choice in rock_paper_scissors:
        print(f"You chose {rock_paper_scissors_icons[user_choice]}")
        print(f"Computer chose {rock_paper_scissors_icons[computer_choice]}")

        if (
            (user_choice == "r" and computer_choice == "s")
            or (user_choice == "p" and computer_choice == "r")
            or (user_choice == "s" and computer_choice == "p")
        ):
            print("You win! 🥳")

        elif user_choice == computer_choice:
            print("It's a tie!")
        else:
            print("Computer win! 🥲")
    else:
        print("Invalid choice! Try again!")
        continue

    replay = input("Continue? (y/n): ").lower()

    if replay == "n":
        break
