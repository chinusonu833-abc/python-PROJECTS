import turtle 
import math

screen = turtle.Screen()
screen.setup(width=700 , height = 700) 
screen.bgcolor(" black")
screen.title ("you are  my star !")

t= turtle.Turtle()
t.hideturtle()
t.widhth(2)

def star (scale, color):
    t.penup()
    t.goto(0, -10)
    t.pendown()
    t.color(color)
    t.begin_fill()


