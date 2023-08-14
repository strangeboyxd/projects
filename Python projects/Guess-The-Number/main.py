#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

print(logo)

randomNum = random.randint(1, 100)

user_Input_difficulty = input("Select game difficulty (easy, hard): ")
while user_Input_difficulty != "easy" and user_Input_difficulty != "hard":
    print("Please enter a valid difficulty ('easy', 'hard') ")
    user_Input_difficulty = input("Select game difficulty (easy, hard): ")
if user_Input_difficulty == "easy":
    lives = 10
elif user_Input_difficulty == "hard":
    lives = 5

user_Input = int(input("Submit your guess (numbers should be from 1 to 100): "))

while lives > 0:
    if user_Input == randomNum:
        print(f"You won! the number was {randomNum} and you had {lives} remaining")
        break
    elif user_Input > randomNum:
        lives -= 1
        print(f"Remaining lives = {lives}")
        print("Try lower number")
        user_Input = int(input("Submit your guess (numbers should be from 1 to 100): "))
    elif user_Input < randomNum:
        lives -= 1
        print(f"Remaining lives = {lives}")
        print("Try higher number")
        user_Input = int(input("Submit your guess (numbers should be from 1 to 100): "))
if lives <= 0:
    print("Unfortunely you lost ):")