from turtle import Screen

screen = Screen()
screen.bgcolor('white')
screen.setup(width=.75, height=.5)
screen.title('Pong Game')


screen.listen()
# screen.onkeypress(key='w', fun=sn.up)
# screen.onkeypress(key='s', fun=sn.down)
# screen.onkeypress(key='a', fun=sn.left)
# screen.onkeypress(key='d', fun=sn.right)



screen.exitonclick()