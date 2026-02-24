

import random

while True:
    number = random.randint(1, 50)
    attempts = 7

    print("\nGuess the number between 1 and 50")

    for i in range(attempts):
        guess = int(input("Enter guess: "))

        if guess == number:
            print("Correct! You won.")
            break
        elif guess < number:
            print("Too low")
        else:
            print("Too high")

    else:
        print("Game Over! Number was:", number)

    again = input("Play again? (yes/no): ")
    if again.lower() != "yes":
        break

print("Thank you for playing!")