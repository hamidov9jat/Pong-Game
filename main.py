from turtle import Screen
from paddle import Paddle

screen = Screen()
screen.bgcolor('white')
screen.setup(width=1280, height=720)
screen.title('Pong Game')

r_paddle = Paddle(position=(-590, 0))
l_paddle = Paddle(position=(590, 0))

screen.listen()
screen.onkeypress(key='w', fun=r_paddle.go_up)
screen.onkeypress(key='s', fun=r_paddle.go_down)
screen.onkeypress(key='Up', fun=l_paddle.go_up)
screen.onkeypress(key='Down', fun=l_paddle.go_down)



screen.exitonclick()