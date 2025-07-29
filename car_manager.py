import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LANE_Y_POSITIONS = [-200,-100,0,100,200]


class CarManager():
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_car_row(self, y_position):
        for x in range(-280, 300, 60):
            new_car = Turtle("Square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.goto(x, y_position)
            self.all_cars.append(new_car)
    def create_car(self):
        spawn_x = 300
        min_gap = 50
        for y in LANE_Y_POSITIONS:
            if random.randint(1, 25) == 1:
                can_spawn = True
                for car in self.all_cars:
                    if car.ycor() == y and abs(car.xcor() - spawn_x) < min_gap:
                        can_spawn = False
                        break
                if can_spawn:
                    new_car = Turtle("square")
                    new_car.penup()
                    new_car.color(random.choice(COLORS))
                    new_car.shapesize(stretch_len=3, stretch_wid=1)
                    new_car.goto(300, y)
                    self.all_cars.append(new_car)
    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT
