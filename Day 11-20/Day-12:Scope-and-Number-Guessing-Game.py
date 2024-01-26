#Number Guessing Game

import random

print("Welcome to the Number Guessing Game.")
print("I'm thinking of a number between 1 and 100.")
ans = random.randint(1, 100)
guess = 0
difficulty = input("Choose a difficulty. Type 'easy' or 'hard' ").lower()
lives = 0

def result():
    print("Your guess:", guess)
    print("Answer:", ans)

if difficulty == "hard":
    lives = 5
elif difficulty == "easy":
    lives = 10
else:
    print("Invalid user input.")
    exit()

for i in range(lives):
    guess = int(input("Enter your guess: "))
    if guess == ans:
        result()
        print("You won!")
        break
    elif guess > ans:
        print("Guess a smaller number.")
    elif guess < ans:
        print("Guess a larger number.")
    lives -= 1
    print("Remaining lives:", lives)
