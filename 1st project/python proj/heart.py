import turtle
import math
import time

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.title("Animated Heart")
screen.tracer(0)   # Turn off automatic updates

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def draw_heart(scale):
    t.clear()

    t.penup()
    t.goto(0, -10)
    t.pendown()

    t.color("red")
    t.begin_fill()

    for i in range(360):
        x = scale * 16 * math.sin(math.radians(i)) ** 3
        y = scale * (
            13 * math.cos(math.radians(i))
            - 5 * math.cos(2 * math.radians(i))
            - 2 * math.cos(3 * math.radians(i))
            - math.cos(4 * math.radians(i))
        )
        t.goto(x, y)

    t.end_fill()

    t.penup()
    t.goto(0, -180)
    t.color("white")
    t.write(
        "I miss you ❤",
        align="center",
        font=("Arial", 22, "bold")
    )

while True:
    for size in range(12, 18):
        draw_heart(size)
        screen.update()
        time.sleep(0.05)

    for size in range(18, 12, -1):
        draw_heart(size)
        screen.update()
        time.sleep(0.05)

turtle.done()