#Rock Paper Scissors Game

import random

choices=["rock","papers","scissors"]

computer=random.choice(choices)
player=0

while player not in choices:
    player=input("rock,paper or scissors:").lower()

if player == computer:
    print("Computer:",computer)
    print("Tie!")

#Player choice == rock
elif player == "rock":
    print("Computer:", computer)
    if computer == "rock":
        print("Tie!")
    elif computer == "paper":
        print("You Lose!")
    elif computer == "scissors":
        print("You Win!")

#Player choice == paper
elif player == "paper":
    print("Computer:", computer)
    if computer == "rock":
        print("You Win!")
    elif computer == "paper":
        print("Tie!")
    elif computer == "scissors":
        print("You Lose!")

#Player choice == scissors
elif player == "scissors":
    print("Computer:", computer)
    if computer == "rock":
        print("You Lose!")
    elif computer == "paper":
        print("You Win!")
    elif computer == "scissors":
        print("Tie!")
