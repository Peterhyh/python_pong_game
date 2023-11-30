from turtle import Screen
from paddle import Paddle
from ball import Ball

screen = Screen()
screen.bgcolor("black")
screen.setup(width=700, height=700)
screen.title("Pong Game")

left_paddle = Paddle((-300, 0))
right_paddle = Paddle((300, 0))

ball = Ball()

screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")


game_on = True

while game_on:
    screen.update()
    ball.move()
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()


screen.exitonclick()
