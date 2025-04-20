import random

numbre_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess > numbre_to_guess:
            print("Too high!")
        elif guess < numbre_to_guess:
            print("Too low!")
        else:
            print("Congratulation! You guessed the number.")
            break

    except ValueError:
        print("Please enter a valid number")
