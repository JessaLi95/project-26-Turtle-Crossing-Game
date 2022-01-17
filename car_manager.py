from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_change = random.randint(1, 6)
        if random_change == 1:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.pu()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.cars.append(new_car)

    def car_move(self):
        for car in self.cars:
            car.backward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
