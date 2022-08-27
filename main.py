import time
from turtle import Screen, Turtle
from tiles import Tile
from paddle import Pad
from ball import Ball
import random

screen = Screen()
screen.listen()
screen.tracer(0)

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Breakout Game")

tk = Turtle()
tk.penup()
tk.hideturtle()
life = 4


def update_life():
    global life, tk
    life -= 1
    if life == 3:
        hearts = '''♥♥♥'''
    elif life == 2:
        hearts = '''♥♥♡'''
    elif life == 1:
        hearts = '''♥♡♡'''
    else:
        tk.clear()
        tk.goto(0, 250)
        tk.pencolor("white")
        tk.pendown()
        tk.write(f"You ran out of lives", align="center", font=("Arial", 30, "normal"))
        return False
    tk.clear()
    tk.goto(0, 250)
    tk.pencolor("white")
    tk.pendown()
    tk.write(f"Lives: {hearts}", align="center", font=("Arial", 30, "normal"))
    tk.penup()
    return True


update_life()

tiles_list = []
x = 355
y = 200
change = -65
color_list = ["green", "red", "yellow", "blue"]
color_no = 0
for num in range(48):
    if num != 0 and num % 12 == 0:
        y -= 25
        color_no += 1

    tile = Tile(color_list[color_no], (x, y))
    tiles_list.append(tile)
    # screen.update()
    # time.sleep(0.1)

    if x < -355:
        x = -355
        change *= -1
    elif x > 355:
        x = 355
        change *= -1
    else:
        x += change

# Creating Pad
pad = Pad((0, -200))

# Creating Ball
ball = Ball()
screen.update()

game_on = True

sleep_time = 0.03
def game():
    global game_on
    while game_on:
        if tiles_list:
            screen.update()
            ball.move()
            time.sleep(sleep_time)

            # collision with wall
            if ball.xcor() >= 380 or ball.xcor() <= -380:
                heading = ball.heading()
                ball.setheading(180 + 360 - heading)

            if ball.ycor() >= 290:
                heading = ball.heading()
                ball.setheading(360 - heading)

            # collision with paddle
            if pad.xcor() + 50 >= ball.xcor() >= pad.xcor() - 50:
                if -190 <= ball.ycor() <= -180:
                    paddle_hit = True
                else:
                    paddle_hit = False
            else:
                paddle_hit = False
            if paddle_hit:
                heading = ball.heading()
                ball.setheading(360 - heading)
            # collision with tiles

            for tiles in tiles_list:
                if tiles.xcor() - 40 <= ball.xcor() <= tiles.xcor() + 40 and tiles.ycor() - 20 <= ball.ycor() <= tiles.ycor() + 20:
                    hit = True

                else:
                    hit = False

                if hit:
                    if tiles.ycor() + 10 <= ball.ycor() <= tiles.ycor() + 20 and tiles.xcor() + 35 <= ball.xcor() <= tiles.xcor() - 35:
                        heading = ball.heading()
                        ball.setheading(360 - heading)
                        tiles.hideturtle()
                        tiles_list.remove(tiles)

                    elif tiles.ycor() - 10 >= ball.ycor() >= tiles.ycor() - 20 and tiles.xcor() + 35 <= ball.xcor() <= tiles.xcor() - 35:
                        heading = ball.heading()
                        ball.setheading(360 - heading)

                        tiles.hideturtle()
                        tiles_list.remove(tiles)

                    elif tiles.ycor() - 15 <= ball.ycor() <= tiles.ycor() + 15 and tiles.xcor() + 30 <= ball.xcor() <= tiles.xcor() + 40:
                        heading = ball.heading()
                        ball.setheading(180 + 360 - heading)

                        tiles.hideturtle()
                        tiles_list.remove(tiles)

                    elif tiles.ycor() - 15 <= ball.ycor() <= tiles.ycor() + 15 and tiles.xcor() - 30 >= ball.xcor() >= tiles.xcor() - 40:
                        heading = ball.heading()
                        ball.setheading(180 + 360 - heading)

                        tiles.hideturtle()
                        tiles_list.remove(tiles)

                    else:
                        heading = ball.heading()
                        ball.setheading(360 - heading)

                        tiles.hideturtle()
                        tiles_list.remove(tiles)

            # drop

            if ball.ycor() < -290:
                if update_life():
                    ball.goto(200, -290)
                    ball.setheading(random.choice([45, 55, 65, 125, 135, 145]))
                    below_surface = True
                    while below_surface:
                        time.sleep(sleep_time)
                        ball.forward(10)
                        screen.update()
                        if ball.ycor() > -180:
                            below_surface = False
                else:
                    game_on = False

        else:
            tk.goto(0, 0)
            tk.pendown()
            tk.pencolor("cyan")
            tk.write(f"You WON!!!", align="center", font=("Arial", 70, "normal"))
            game_on = False


def move_pad(x_val, y_val):
    if -390 < x_val < 390:
        pad.goto(x_val, -200)


screen.onkey(game, "space")
pad.ondrag(move_pad)

screen.mainloop()
