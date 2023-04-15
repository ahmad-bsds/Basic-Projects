import time
import turtle
from turtle import Screen
from score_board import Score
from food import Food
from snack import Snack

screen = Screen()
screen.setup(width=500, height=400)
screen.bgcolor('black')
screen.title("Snack Game")
screen.listen()  # listen events as on key press do something.
screen.tracer(0)  # control animation and handel delay.
# creating a snack.
snack = Snack()
# creating food.
food = Food()
# creating score.
score = Score()
# Creating keyboard key events.
screen.onkeypress(snack.up, 'Up')
screen.onkeypress(snack.left, 'Left')
screen.onkeypress(snack.right, 'Right')
screen.onkeypress(snack.down, 'Down')

is_game_on = True
while is_game_on:
    snack.move()
    turtle.update()
    time.sleep(0.2)

    # Handling food.
    if snack.head.distance(food) < 15:  # no need to food.food food is self a turtle object as it uses inheritance.
        food.refresh()
        score.increase_score()
        snack.size()

    # End when touch to border.
    if snack.head.xcor() > 230 or snack.head.xcor() < -230 or snack.head.ycor() > 190 or snack.head.ycor() < -190:
        snack.reset()
        score.reset_score()
        score.update()

    # Game over.
    for segments in snack.snack_segments[1:]:
        if snack.head.distance(segments) < 10:
            snack.reset()
            score.reset_score()
            score.update()

screen.exitonclick()
