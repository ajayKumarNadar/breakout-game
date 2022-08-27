from turtle import Turtle


class Pad(Turtle):
    def __init__(self, xy_cor):
        super().__init__("square")
        self.penup()
        self.shapesize(1, 5)
        self.color("white")
        self.goto(xy_cor)

    def go_right(self):
        if not self.xcor() == 340:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())
            print(self.xcor())

    def go_left(self):
        if not self.xcor() == -340:
            new_x = self.xcor() - 20
            self.goto(new_x, self.ycor())
            print(self.xcor())

