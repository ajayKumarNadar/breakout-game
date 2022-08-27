from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.pencolor("white")
        self.penup()
        self.setheading(25)
        self.goto(0, -150)

    def move(self):
        self.forward(10)
        # new_x = self.xcor() + self.x_move
        # new_y = self.ycor() + self.y_move
        # self.goto(new_x, new_y)


