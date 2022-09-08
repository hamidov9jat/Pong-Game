from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__('circle')
        self.color('red')
        self.penup()
        self.x_move = 3
        self.y_move = 3

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_x(self):
        self.x_move *= -1

    def bounce_y(self):
        self.y_move *= -1

    def reset_ball_position(self):
        self.home()
        # If the right paddle misses (loses) next time ball will go to left paddle
        self.bounce_x()