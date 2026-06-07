import turtle

screen = turtle.Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.title("Star")

t = turtle.Turtle()
t.hideturtle()
t.width(2)
t.speed(0)

def star(size, color):
    t.penup()
    t.goto(0, 50)
    t.pendown()

    t.color(color)
    t.begin_fill()

    for i in range(5):
        t.forward(size)
        t.right(144)

    t.end_fill()

# Large star
star(250, "#F7F4F4")

# Smaller star
t.penup()
t.goto(20, 40)
t.setheading(0)
t.pendown()
star(220, "#E1E81E")

# Small center star
t.penup()
t.goto(40, 30)
t.setheading(0)
t.pendown()
star(100, "#FAF8F8")

# Message
t.penup()
t.goto(0, -180)
t.color("white")

t.write(
    "you are my star ⭐",
    align="center",
    font=("Segoe UI", 22, "bold")
)

turtle.done()