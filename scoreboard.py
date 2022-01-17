from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.pu()
        self.setpos(-260, 260)
        self.level = 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", font=FONT)

    def level_up(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.setpos(0, 0)
        self.write("GAME OVER", font=FONT)
