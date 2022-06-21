n = 45
num_of_guesses = 1
print("Guess the exact number to win a prize.")
print("Maximum number of guesses are 9.\n")
while(num_of_guesses<=9):
    guess_num = int(input("enter your guess\n"))
    if guess_num < 45:
        print("you have entered a number less than actual number\n")
    elif guess_num > 45:
        print("you have entered a number more than actual number\n")
    elif guess_num == 45:
        print("you have won\n")
        break
    print(9-num_of_guesses, "guesses left")
    num_of_guesses = num_of_guesses + 1

if num_of_guesses == 9:
    print("\ngame over\n")