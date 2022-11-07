import random

def computer_guess(x):
    guess = 0
    # intializing the values and setting up the range of the number
    low = 1
    high = x

    feedback = ''

    # using while loop to ensure to check if any undefined conditions are met then stop the loop or continue
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high) # setting up the range
        else:
            guess = low # guessed number is == low or high

        # feedback to check the number
        feedback = input(f'if the {guess} is too (h) or too low (l) or guessed correctly (c)')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Congratulations! The computer guessed the number {guess} correctly.')

# calling the function
computer_guess(500)
