#Challenge: Write a number guessing game where the user has 5 attempts.
#Use break to end early if the guess is right, and continue to skip invalid input.
import random

secret_number = random.randint(1,50)

attempts = 5

print("Guess the number, it is in between 1 to 50 !")

for i in range(1, attempts+1):
    guess = input("\nEnter your guess: ")
    

    if not guess.isdigit():
        print("Invlid input. Please enter a number: ")
        continue


    guess = int(guess)

    if guess> secret_number:
        print("Number is too big!")

    elif guess< secret_number:
        print("Number is too small!")
    else :
        print("Congratulations, you guessed the number right")


if guess != secret_number:
        print("Out of attempts! The secret number was", secret_number )
