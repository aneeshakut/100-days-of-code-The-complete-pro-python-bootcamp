#BlackJack Capstone Project
import random

print("Welcome to the BlackJack Game!")
play = input("Do you want to play the game? Type 'y' or 'n':")

if play.lower() == "y":
    game = True
    cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def get_card():
        return random.choice(cards)

    def calculate_score(cards):
        return sum(cards)

    your_cards = [get_card(), get_card()]
    comp_cards = [get_card(), get_card()]

    def show_initial_cards():
        print("Your Cards: ", your_cards)
        print("Computer's Card: ", comp_cards[0])

    show_initial_cards()

    while game:
        another_card = input("Type 'y' to get more cards, 'n' to pass: ")

        if another_card.lower() == "n":
            your_score = calculate_score(your_cards)
            comp_score = calculate_score(comp_cards)

            def show_score():
                print("Computer's Cards: ", comp_cards)
                print("Computer's Score: ", comp_score)
                print("Your Cards: ", your_cards)
                print("Your Score: ", your_score)

            show_score()

            if your_score > comp_score:
                print("You won!")
            elif your_score < comp_score:
                print("You lose!")
            else:
                print("It's a Tie!")

            game = False
        else:
            your_cards.append(get_card())
            comp_cards.append(get_card())

            print("Your Cards: ", your_cards)
            print("Computer's Card: ", comp_cards[0])

elif play.lower() == "n":
    pass
else:
    print("Invalid user input!")
