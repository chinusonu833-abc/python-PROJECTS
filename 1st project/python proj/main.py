import turtle
import math

screen = turtle.Screen()
screen.setup(width=600, height=500)
screen.bgcolor("pink")
screen.title("I miss you!")

t = turtle.Turtle()
t.hideturtle()
t.width(2)

def heart(scale, color):
    t.penup()
    t.goto(0, -10)
    t.pendown()
    t.color(color)
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

screen.tracer(0)
heart(15, "#330000")
screen.update()

screen.tracer(1)
heart(14, "#F80C0C")

screen.tracer(2)
heart(7,"#FAF8F8" )

t.penup()
t.goto(0, -150)
t.color("#fffefe")
try:
    t.write("I miss you \u2764", align="center",
            font=("Segoe UI", 22, "bold"))
except Exception:
    t.write("I miss you <3", align="center",
            font=("Segoe UI", 22, "bold"))
    
turtle.done()