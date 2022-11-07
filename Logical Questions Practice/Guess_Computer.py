import random

def guess_number(x):
    # generating a random number
    # randint will retrun a random integer N such that it will be a <= N <= b
    random_number = random.randint(1, x)

    # So that it != random number and it will never be 0
    guess_number = 0

    # Used while loop to get the guessing going for random number of time
    # expression will help to check it if number = 0 it will run the loop 
    while guess_number != random_number:
        guess_number = int(input(f"Guess the number:"))
        if guess_number < random_number:
            print(f"Enter number greater than number {guess_number}.")
        elif guess_number > random_number:
            print(f"Enter number lower than number {guess_number}.")
        else:
            print("Congratulation!!! You have guessed it correctly.")

# calling the function
guess_number(100)