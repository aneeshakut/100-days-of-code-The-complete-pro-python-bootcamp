#Hangman Project

import random

word_list = ["tiger","lion","jaguar"]

chosen_word = random.choice(word_list)
display = []

for letter in chosen_word:
    display += "_"
print("Word to guess:",display)
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter:").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if(letter == guess):
            display[position] = letter
    print(display)
    if "_" not in display:
        end_of_game = True
        print(" The word was:",chosen_word)
        print("You win!")
