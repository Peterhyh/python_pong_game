from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

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
    screen.update()
    ball.move()

    if ball.ycor() > 320 or ball.ycor() < -320:
        ball.bounce_y()

    if ball.distance(right_paddle) < 40 and ball.xcor() == 290:
        ball.bounce_x()
        # right_scoreboard.score_up()

    if ball.distance(left_paddle) < 40 and ball.xcor() == -290:
        ball.bounce_x()
        # left_scoreboard.score_up()

    if ball.xcor() > 310 or ball.xcor() < -310:
        game_on = False
        # left_scoreboard.game_over()

    # reset ball when out of bound and moves towards the scoring side


screen.exitonclick()
