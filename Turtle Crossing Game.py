import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)


player = Player()
car_manager = CarManager()


screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(player.move_speed)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            scoreboard.game_over()
            game_is_on = False
    if player.ycor() > 280:
        player.reset_position()
        scoreboard.point()







screen.exitonclick()