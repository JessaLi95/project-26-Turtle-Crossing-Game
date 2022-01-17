from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.setpos(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def move(self):
        self.fd(MOVE_DISTANCE)

    def player_score(self):
        if self.ycor() == 280:
            self.setpos(STARTING_POSITION)
            return True




