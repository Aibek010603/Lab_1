import random

def guess_the_number():
#Greeting the player
    name = input("Hello! What is your name?\n")

    #Random between 1-20
    number_to_guess = random.randint(1, 20)
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")

    guesses_taken = 0

    while True:
        guesses_taken += 1
        guess = int(input("Take a guess.\n"))

        if guess < number_to_guess:
            print("Your guess is too low.")
        elif guess > number_to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_taken} guesses!")
            break

guess_the_number()
