#Guess the Number game

import random

def guess_number_game():
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

def rock_paper_scissors():
    print("\n=== Rock Paper Scissors Game ===")
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        print("\nChoose: rock, paper, or scissors")
        player_choice = input("Your choice: ").lower()
        
        if player_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"\nComputer chose: {computer_choice}")
        print(f"You chose: {player_choice}")
        
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == 'rock' and computer_choice == 'scissors') or \
             (player_choice == 'paper' and computer_choice == 'rock') or \
             (player_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
        else:
            print("Computer wins!")
            
        if input("\nPlay again? (y/n): ").lower() != 'y':
            break

def main():
    while True:
        print("\nSelect a game:")
        print("1. Guess Number Game")
        print("2. Rock Paper Scissors")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ")
        
        if choice == '1':
            guess_number_game()
        elif choice == '2':
            rock_paper_scissors()
        elif choice == '3':
            print("\nThanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
            
        if input("\nWould you like to try another game? (y/n): ").lower() != 'y':
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()