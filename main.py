from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setup screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Create paddles, ball, and scoreboard
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

# Keyboard bindings
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# Game loop setup
game_is_on = True
fps = 60  # Frames per second
frame_duration = 1.0 / fps  # Duration of each frame in seconds

previous_time = time.time()

while game_is_on:
    current_time = time.time()
    elapsed_time = current_time - previous_time

    if elapsed_time >= frame_duration:
        screen.update()
        ball.move()

        # Collision with top and bottom walls
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()

        # Collision with paddles
        if (ball.distance(r_paddle) < 90 and ball.xcor() > 320) or (ball.distance(l_paddle) < 90 and ball.xcor() < -320):
            ball.bounce_x()

        # Right paddle misses
        if ball.xcor() > 380:
            scoreboard.l_point()
            ball.reset_position()

        # Left paddle misses
        if ball.xcor() < -380:
            scoreboard.r_point()
            ball.reset_position()

        previous_time = current_time

screen.exitonclick()
