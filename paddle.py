from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,x ,y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(x, y)

    def get_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def get_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



