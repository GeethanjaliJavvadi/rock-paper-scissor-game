#import required modules

import random

#define the function for user'choice

def get_user_choice():
    
#Get user's choice of rock, paper, or scissors.
    
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ["rock", "paper", "scissors"]:
            return user_choice
        else:
            print("Entered choice is invalid choice. Please try again.")

#define the fumction for computer's choice            

def get_computer_choice():
    
# Get computer's random choice of stone, paper, or scissors.
    
    return random.choice(["rock", "paper", "scissors"])

def decide_winner(user_choice, computer_choice):
    
#Determine the winner based on user's choice and computer's choice.
    
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "You win! \n{} beats {}".format(user_choice,computer_choice)

    else:
        return "Computer wins! \n{} beats {}".format(computer_choice,user_choice)

def main():
    print("Let's play rock-Paper-Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print("Computer's choice:", computer_choice)

        result = decide_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
