from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "aquamarine2", "CadetBlue2", "chocolate2",
          "DarkOliveGreen", "DarkOrchid2", "DarkOrange2", "DodgerBlue", "firebrick", "khaki", "LightPink", "LimeGreen",
          "MistyRose2", "SpringGreen", "salmon3", "SlateBlue2"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2

class CarManager():

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            #new_car.x_move = 10
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def level_up(self):
            self.car_speed += MOVE_INCREMENT
