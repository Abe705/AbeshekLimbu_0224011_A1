import random

guesses_taken = 0

print("Hello! What is your name?")
my_name = input()

number = random.randint(1, 20)
print("Well, " + my_name + ", I am thinking of a number between 1 and 20.")

for guesses_taken in range(6):
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    if guess < number:
        print("Your guess is too low.")
    elif guess > number:
        print("Your guess is too high.")
    else:
        guesses_taken += 1
        print("Good job, " + my_name + "! You guessed my number in " + str(guesses_taken) + " guesses!")
        break

if guess != number:
    print("Nope, the number I was thinking of was " + str(number) + ".")

    
