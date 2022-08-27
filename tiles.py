from turtle import Turtle


class Tile(Turtle):
    def __init__(self, color, xy_cor):
        super().__init__("square")
        self.penup()
        self.shapesize(1, 3)
        self.color(color)
        self.goto(xy_cor)
        self.alive = True

    def check_col(self, xy_cor):
        x_value = xy_cor[0]
        y_value = xy_cor[1]

        x = self.xcor()
        y = self.ycor()

        if y + 20 >= y_value or y - 20 <= y_value or x + 40 >= x_value or x - 40 <= x_value:
            self.hideturtle()
            return "b"
        elif y + 20 >= y_value or y - 20 <= y_value:
            self.hideturtle()
            return "y"
        elif x + 40 >= x_value or x - 40 <= x_value:
            self.hideturtle()
            return "x"
        else:
            return None

