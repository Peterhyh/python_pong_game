from turtle import Turtle


FONT = ("Arial", 30, "normal")
ALIGN = "center"
TEXT_COLOR = "white"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color(TEXT_COLOR)
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 280)
        self.write(f"{self.left_score}",
                   align=ALIGN, font=FONT)
        self.goto(100, 280)
        self.write(f"{self.right_score}",
                   align=ALIGN, font=FONT)

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.color(TEXT_COLOR)
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
