from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=700, height=700)
screen.title("Pong Game")

left_paddle = Paddle((-300, 0))
right_paddle = Paddle((300, 0))

screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")


game_on = True

while game_on:
    screen.update()


screen.exitonclick()
