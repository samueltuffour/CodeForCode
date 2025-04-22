import turtle
import math

def draw_dna():
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.speed(0)
    pen.pensize(2)

    # Setup colors
    color1 = "cyan"
    color2 = "magenta"
    base_colors = ["yellow", "green"]

    # Draw the helix
    for x in range(-200, 201, 4):
        y = 100 * math.sin(x * 0.04)
        pen.penup()
        pen.goto(x, y)
        pen.pendown()

        # Draw spiral backbone
        pen.color(color1)
        pen.dot(10)
        pen.color(color2)
        pen.goto(x, -y)
        pen.dot(10)

        # Connect the bases
        pen.color(base_colors[(x//4) % 2])
        pen.goto(x, y)

    pen.hideturtle()
    turtle.done()

draw_dna()
