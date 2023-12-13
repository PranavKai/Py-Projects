import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("Crossing Game")
screen.onkey(player.move, "Up")




game_is_on = True
while game_is_on:
    time.sleep(0.01)
    screen.update()
    
    car.create_car()
    car.move_cars()

    #Detect collision
    for c in car.all_cars:
        if c.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect collison with the wall
    if player.is_at_finish_line():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()
        

screen.exitonclick()