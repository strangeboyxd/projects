from turtle import Turtle, Screen
import random

is_race_on = False
Screen = Screen()
Screen.setup(width=500, height=400)
user_bet = Screen.textinput(title="Make Your Bet", prompt="Which Turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

i = 0
for color in colors:
    tim = Turtle(shape="turtle")
    tim.color(color)
    tim.penup()
    tim.goto(-230, -80 + i)
    i += 40
    all_turtles.append(tim)
if user_bet:
    is_race_on = True
while is_race_on:
  for turtle in all_turtles:
    if turtle.xcor() > 230:
       is_race_on = False
       wining_color = turtle.pencolor()
       if wining_color == user_bet:
          print(f"You have won! {wining_color} turtle won the race")
       else:
          print(f"you have lost {wining_color} turtle won the race")
          
    r_distance = random.randint(0, 10)
    turtle.forward(r_distance)
  
    

Screen.exitonclick()