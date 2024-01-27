#Higher or Lower Game

import random

def higher_lower_game():
    country_populations = {
        'China': 1444216107,
        'India': 1393409038,
        'United States': 332915073,
        'Indonesia': 276361783,
        'Pakistan': 225199937,
        'Brazil': 213993437,
        'Nigeria': 211400708,
        'Bangladesh': 166303498,
        'Russia': 145912025,
        'Mexico': 130262216,
        # Add more countries and their populations as needed
    }

    countries = list(country_populations.keys())
    score = 0

    print("Welcome to the Higher or Lower Game with Country Populations!")
    print("Guess whether the population of the next country is higher or lower.")

    while True:
        country1 = random.choice(countries)
        country2 = random.choice(countries)

        print(f"Population of {country1}: {country_populations[country1]}")

        while True:
            guess = input(f"Is the population of {country2} higher or lower than {country1}? ").lower()

            if guess not in ['higher', 'lower']:
                print("Invalid input. Please enter 'higher' or 'lower'.")
            else:
                break

        if (country_populations[country2] > country_populations[country1] and guess == 'higher') or \
           (country_populations[country2] < country_populations[country1] and guess == 'lower'):
            score += 1
            print(f"Correct! Population of {country2}: {country_populations[country2]}")
        else:
            print(f"Wrong! The correct answer is {country2}.")
            print(f"Your final score: {score}")
            break

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print(f"Your final score: {score}")
            break

if __name__ == "__main__":
    higher_lower_game()
