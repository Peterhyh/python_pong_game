from turtle import Turtle


FONT = ("Arial", 15, "normal")
ALIGN = "center"
TEXT_COLOR = "white"


class Scoreboard(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.color(TEXT_COLOR)
        self.player_score = 0
        self.hideturtle()
        self.penup()
        self.goto(x_cor, y_cor)
        self.update_score()

    def game_over(self):
        self.color(TEXT_COLOR)
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def update_score(self):
        self.write(f"Score: {self.player_score}",
                   align=ALIGN, font=FONT)

    def score_up(self):
        self.player_score += 1
        self.clear()
        self.update_score()
