import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Turtle Crossing Game")
screen.tracer(0)

turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(turtle.move_up, "Up")
screen.onkeypress(turtle.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()

    scoreboard.update_scoreboard()

    # Detect if turtle pass the finish line
    if turtle.ycor() > 280:
        scoreboard.add_score()
        turtle.reset_position()
        car_manager.level_up()

    #Detect collision with the car
    for car in car_manager.all_cars:
        if car.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()