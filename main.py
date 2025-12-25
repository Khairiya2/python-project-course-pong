from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

#create screen
screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

#create and move paddle
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down, "s")


#create ball and make it move

#detect when paddle misses
#keep score
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect collision with wall and bounce
    if ball.ycor()  > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() <-320:
        ball.bounce_x()

    #detect when r paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #detect when l paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()





screen.exitonclick()
