from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
from line import Line
from turtle import Screen
import time

MOVE_TIME = 0.1

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

line = Line()
# line.draw_line()

paddle_1 = Paddle(-350, 0)
paddle_2 = Paddle(350, 0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle_1.up_movement, "w")
screen.onkey(paddle_1.down_movement, "s")
screen.onkey(paddle_2.up_movement, "Up")
screen.onkey(paddle_2.down_movement, "Down")


play = True
while play:
    serve = True
    while serve:
        screen.update()
        time.sleep(MOVE_TIME)
        ball.move()
        scoreboard.update_scoreboard()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
        if ball.distance(paddle_1) < 50 and ball.xcor() < -320 or ball.distance(paddle_2) < 50 and ball.xcor() > 320:
            ball.bounce_x()
        if ball.xcor() > 400:
            ball.reset_position()
            scoreboard.l_point()
            serve = False
        elif ball.xcor() < -400:
            ball.reset_position()
            scoreboard.r_point()
            serve = False


screen.exitonclick()
