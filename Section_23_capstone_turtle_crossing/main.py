import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move_cars()
    car_manager.add_row_of_cars()

    if player.has_crossed_finish():
        scoreboard.increment_level()
        car_manager.increase_speed()
        player.reset_position()

    for car in car_manager.cars:
        if car.distance(player) < 15:
            game_is_on = False
            scoreboard.print_game_over()

screen.exitonclick()
