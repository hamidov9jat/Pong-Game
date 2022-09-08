from turtle import Screen
from paddle import Paddle
from pong_ball import Ball
from time import sleep

screen = Screen()
screen.bgcolor('white')
screen.setup(width=1280, height=720)
screen.title('Pong Game')
# Turn off tracer
screen.tracer(0)

l_paddle = Paddle(position=(-590, 0))
r_paddle = Paddle(position=(590, 0))
ball = Ball()
# ball.speed(1)


screen.listen()
screen.onkeypress(key='w', fun=l_paddle.go_up)
screen.onkeypress(key='s', fun=l_paddle.go_down)
screen.onkeypress(key='Up', fun=r_paddle.go_up)
screen.onkeypress(key='Down', fun=r_paddle.go_down)

game_is_on = True

while game_is_on:
    screen.update()
    ball.move_ball()
    sleep(.001)

    # Detect collision with wall
    if ball.ycor() > 340 or ball.ycor() < -340:
        ball.bounce_y()

    # print(ball.distance(r_paddle))
    # print(ball.distance(l_paddle))

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 100 and ball.xcor() > 565) or (ball.distance(l_paddle) < 100 and ball.xcor() < -565):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 600:
        ball.reset_ball_position()
        # scoreboard.l_point()

    # Detect L paddle misses:
    if ball.xcor() < -600:
        ball.reset_ball_position()
        # scoreboard.r_point()

screen.exitonclick()
