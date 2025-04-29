# Turtle-based DNA visualization
import math
import turtle

def draw_dna(dna_sequence):
    screen = turtle.Screen()
    screen.bgcolor("black")
    pen = turtle.Turtle()
    pen.speed(0)
    pen.pensize(2)

    color1 = "cyan"
    color2 = "magenta"

    base_pair_colors = {
        ('A', 'T'): "yellow",
        ('T', 'A'): "yellow",
        ('C', 'G'): "green",
        ('G', 'C'): "green"
    }

    x = -len(dna_sequence) * 4

    for base in dna_sequence:
        y = 100 * math.sin(x * 0.04)
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color(color1)
        pen.dot(10)

        pen.color(color2)
        pen.goto(x, -y)
        pen.dot(10)

        pair = None
        if base == 'A': pair = 'T'
        elif base == 'T': pair = 'A'
        elif base == 'C': pair = 'G'
        elif base == 'G': pair = 'C'

        if pair:
            color = base_pair_colors.get((base, pair), "white")
            pen.color(color)
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.goto(x, -y)

        x += 8

    pen.hideturtle()
    turtle.done()
