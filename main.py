import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score_board = Scoreboard()
screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.car_move()
    # Detect the collision with the destination.
    if player.player_score():
        score_board.level_up()
        car.speed_up()
    # Detect the collision with cars.
    for this_car in car.cars:
        if this_car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
