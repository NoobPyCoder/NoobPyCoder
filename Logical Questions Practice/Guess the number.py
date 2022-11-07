# defining the number
n = 45

# intializing the counting of num_of_guesses to start from 1
num_of_guesses = 1

print("Guess the exact number to win a prize.")
print("Maximum number of guesses are 9.\n")

# using while loop to run for indefinite number of time
while(num_of_guesses<=9):
    guess_num = int(input("enter your guess\n"))
    if guess_num < 45:
        print("you have entered a number less than actual number\n")
    elif guess_num > 45:
        print("you have entered a number more than actual number\n")
    elif guess_num == 45:
        print("you have won\n")
        break

    # printing the number of guesses left
    print(9-num_of_guesses, "guesses left")

    # countng the number of guesses
    num_of_guesses = num_of_guesses + 1

# restricting the number of guesses 
if num_of_guesses == 9:
    print("\ngame over\n")