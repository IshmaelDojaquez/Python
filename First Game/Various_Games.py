import random
from random import randint


print("Welcome to the Game Selector")

# Use of a dictionary
gameConversion = {
    1: "Random Number Guesser",
    2: "MadLib",
    3: "Rock Paper Scissors"
    }

# Use of methods
def gameMenu():
    print("1. Random Number Guesser")
    print("2. MadLib")
    print("3. Rock Paper Scissors\n")
    game_selected = int(input("Please Select Your Game: "))

# Use of a while loop
    while game_selected > 3 or game_selected < 0:
        print("This was not a value...\n")
        game_selected = int(input("Select Your Game: "))

# Use of an if statement
    if game_selected == 1:
        print(f"You selected: {gameConversion[1]}!\n")
    elif game_selected == 2:
        print(f"You selected: {gameConversion[2]}!\n")
    elif game_selected == 3:
        print(f"You selected: {gameConversion[3]}!\n")
    return game_selected

def randomNumberGuesser():
    # Use of random
    correct_answer = randint(0, 100)
    number_guessed = int(input("Choose a random number between 1-100: "))

# Use of while and if
    while number_guessed > 100 or number_guessed < 1:
        print("This was not a value...\n")
        number_guessed = int(input("Choose a random number between 1-100: "))

    while number_guessed != correct_answer:
        if number_guessed < correct_answer:
            print("Not quiet there... You're too low!")
            number_guessed = int(input("\nChoose another number: "))
        elif number_guessed > correct_answer:
            print("Oh no... That's too high!")
            number_guessed = int(input("\nChoose another number: "))
    print("Congratulations! You guessed the right answer!")

def madLib():
    adjective1 = input("Enter an adjective: ")
    color = input("Enter a color: ")
    thing = input("Enter a thing:")
    place = input("Enter a place: ")
    person = input("Enter the name of a person: ")
    adjective2 = input("Enter an adjective: ")
    insect = input("Enter an insect: ")
    food = input("Enter a type of food: ")
    verb = input("Enter a verb: ")
    print(f"Last night I dreamed I was a {adjective1} butterfly with {color} spots that looked like {thing}.\n "
          f"I flew to {place} with my best-friend and {person} who was a {adjective2} {insect}.\n"
          f"We ate some {food} when we got there and then decided to {verb} and the dream ended when I said \"Lets {verb}!\".")

def rockPaperScissors():
    matches_played = 0
    computer_won = 0
    player_won = 0

# Use of while and if
    while matches_played != 3:
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)
        player_choice = input("Choose Your Weapon: ")
        player_choice.lower()
        print("Rock... Paper.. Scissors. SHOOT!\n")
        if player_choice == computer_choice:
            print(f"Both players selected {player_choice}. It's a tie!")
        elif player_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win!")
                player_won += 1
            else:
                print("Paper covers rock! You lose.")
                computer_won += 1
        elif player_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
                player_won += 1
            else:
                print("Scissors cuts paper! You lose.")
                computer_won += 1
        elif player_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win!")
                player_won += 1
            else:
                print("Rock smashes scissors! You lose.")
                computer_won += 1
        matches_played += 1
        print(f"\nYou have {player_won} wins. The computer has {computer_won} wins.\n"
              f"There is {3 - matches_played} game left!\n")

game_selected = gameMenu()
if game_selected == 1:
    randomNumberGuesser()
elif game_selected == 2:
    madLib()
elif game_selected == 3:
    rockPaperScissors()
print("\nI Hope You Had Fun!")