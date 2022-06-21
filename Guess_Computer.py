import random

def guess_number(x):
    random_number = random.randint(1, x)
    guess_number = 0

    while guess_number != random_number:
        guess_number = int(input(f"Guess the number:"))
        if guess_number < random_number:
            print(f"Enter number greater than number {guess_number}.")
        elif guess_number > random_number:
            print(f"Enter number lower than number {guess_number}.")
        else:
            print("Congratulation!!! You have guessed it correctly.")

guess_number(10)