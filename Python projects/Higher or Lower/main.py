from art import logo
from art import vs
from game_data import data
import random

print(logo)

has_lost = False
points = 0


while has_lost != True:
    opponent1 = random.choice(data)
    opponent2 = random.choice(data)
    print(f"{opponent1['name']}, {opponent1['description']}, {opponent1['country']} ")
    print(vs)
    print(f"{opponent2['name']}, {opponent2['description']}, {opponent2['country']} ")
    user_input = input("higher or lower? ")

    follower_count_value_1 = opponent1['follower_count']
    follower_count_value_2 = opponent2['follower_count']

    if follower_count_value_1 > follower_count_value_2:
        if user_input == "higher":
            print("you got +1 point")
            points += 1
        else:
            print(f"you lost, highscore = {points}")
            has_lost = True
    elif follower_count_value_1 < follower_count_value_2:
        if user_input == "lower":
            print("you got +1 point")
            points += 1
        else:
            print(f"you lost, highscore = {points}")
            has_lost = True