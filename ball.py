from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.ball_speed = 1
        self.speed(self.ball_speed)
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def increase_speed(self):
        self.ball_speed += 1
        print(self.ball_speed)

    def reset_ball(self):
        self.goto(0, 0)
        self.ball_speed = 0.1
        self.bounce_x()
        self.bounce_y()
