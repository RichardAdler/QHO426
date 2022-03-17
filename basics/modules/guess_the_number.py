from random import randrange

min = int(input("Please enter the minimum value: "))
max = int(input("Please enter the maximum value: "))

random = randrange(min, max)

guess = int(input(f"I am thinking of a number between {min} and {max}.  Can you guess what it is?\n"))

def play_guess_the_number(guess):

    while guess != random:
        if guess < random and guess >= min:
            print("\nYour guess is too low.")
            guess = int(input("Try again.\n"))        
        elif guess > random and guess <= max:
            print("\nYour guess is too high.")
            guess = int(input("Try again.\n"))
        else:
            guess = int(input("Your guess is not in the number range you defined. Try again.\n"))
    print("Congratulations! You guessed my number!")


play_guess_the_number(guess)