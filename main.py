from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=700, height=700)
screen.title("Pong Game")

left_paddle = Paddle((-300, 0))
right_paddle = Paddle((300, 280))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")


game_on = True

while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 320 or ball.ycor() < -320:
        ball.bounce_y()

    if ball.distance(right_paddle) < 40 and ball.xcor() == 290:
        ball.bounce_x()

    if ball.distance(left_paddle) < 40 and ball.xcor() == -290:
        ball.bounce_x()

    if ball.xcor() > 310:
        scoreboard.left_point()
        ball.reset_ball()

    if ball.xcor() < -310:
        scoreboard.right_point()
        ball.reset_ball()


screen.exitonclick()
