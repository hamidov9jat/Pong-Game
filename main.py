from turtle import Screen
from paddle import Paddle
from pong_ball import Ball
from scoreboard import ScoreBoard
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

score_board = ScoreBoard()

screen.listen()
screen.onkeypress(key='w', fun=l_paddle.go_up)
screen.onkeypress(key='s', fun=l_paddle.go_down)
screen.onkeypress(key='Up', fun=r_paddle.go_up)
screen.onkeypress(key='Down', fun=r_paddle.go_down)

while True:
    sleep(.001)
    screen.update()

    ball.move_ball()

    # Detect collision with wall
    if ball.ycor() > 340 or ball.ycor() < -340:
        ball.bounce_y()

    # print(ball.distance(r_paddle))
    # print(ball.distance(l_paddle))

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 128 and ball.xcor() > 560) or (ball.distance(l_paddle) < 128 and ball.xcor() < -560):
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 600:
        ball.reset_ball_position()
        score_board.increase_l_score()

    # Detect L paddle misses:
    if ball.xcor() < -600:
        ball.reset_ball_position()
        score_board.increase_r_score()

    if score_board.l_score == 10:
        score_board.clear()
        score_board.home()
        score_board.write('L is the winner!', align='center', font=('Times New Roman', 40, 'normal'))
        break

    if score_board.r_score == 10:
        score_board.clear()
        score_board.home()
        score_board.write('R is the winner!', align='center', font=('Times New Roman', 40, 'normal'))
        break

screen.exitonclick()
