import random


# Function to generate a random number between 1 and 100
def comp_guess():
    return random.randint(1, 100)


# Function to compare the user's guess with the computer's number
def user_guess(num, comp_num):
    if num < comp_num:
        return "below"
    elif num > comp_num:
        return "above"
    else:
        return "congrats"


# Main game logic
comp_num = comp_guess()  # Computer generates the random number once
game_active = True

while game_active:
    try:
        num = int(input("Enter a number: "))
        result = user_guess(num, comp_num)

        if result == "congrats":
            print("Congrats! You won the game.")
            game_active = False  # End the game
        elif result == "above":
            print("Think less than this number.")
        elif result == "below":
            print("Think of a number greater than this.")
    except ValueError:
        print("Please enter a valid number.")
