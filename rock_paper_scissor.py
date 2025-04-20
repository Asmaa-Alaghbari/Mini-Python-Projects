import random

ROCK = "r"
PAPER = "p"
SCISSORS = "s"

rock_paper_scissors = {ROCK: "🪨", PAPER: "📄", SCISSORS: "✂️"}
Choices = tuple(rock_paper_scissors.keys())


def get_user_choice():
    while True:
        user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
        if user_choice in Choices:
            return user_choice
        else:
            print("Invalid choice! Try again!")


def display_chioces(user_choice, computer_choice):
    print(f"You chose {rock_paper_scissors[user_choice]}")
    print(f"Computer chose {rock_paper_scissors[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    if (
        (user_choice == ROCK and computer_choice == SCISSORS)
        or (user_choice == PAPER and computer_choice == ROCK)
        or (user_choice == SCISSORS and computer_choice == PAPER)
    ):
        print("You win! 🥳")

    elif user_choice == computer_choice:
        print("It's a tie!")
    else:
        print("Computer win! 🥲")


def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(Choices)

        get_user_choice()
        display_chioces(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        replay = input("Continue? (y/n): ").lower()

        if replay == "n":
            break


play_game()
