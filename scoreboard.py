from turtle import Turtle
FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-230,260)
        self.write(f"Level: {self.score}", align = "center", font= FONT)
    def point(self):
        self.score +=1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0, -280)
        self.write("GAME OVER", align=ALIGNMENT, font = FONT)
