# visualization.py
# Turtle-based DNA visualization

import math
import turtle

def draw_dna(dna_sequence):
    """
    Visualizes a DNA sequence using turtle graphics by drawing base pairs
    along a sine wave to simulate the helix shape.
    
    Parameters:
        dna_sequence (str): A string of DNA bases (A, T, C, G).
    """

    # Set up turtle screen and turtle pen
    screen = turtle.Screen()
    screen.bgcolor("black")  # Set background color to black
    pen = turtle.Turtle()
    pen.speed(0)             # Fastest drawing speed
    pen.pensize(2)

    # Colors for the dots on each strand
    color1 = "cyan"
    color2 = "magenta"

    # Color mapping for base pair connectors
    base_pair_colors = {
        ('A', 'T'): "yellow",
        ('T', 'A'): "yellow",
        ('C', 'G'): "green",
        ('G', 'C'): "green"
    }

    # Starting x-coordinate based on sequence length
    x = -len(dna_sequence) * 4

    # Iterate through the sequence to draw each base pair
    for base in dna_sequence:
        y = 100 * math.sin(x * 0.04)  # Generate a wave pattern for the helix

        # Draw first base dot
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        pen.color(color1)
        pen.dot(10)

        # Draw complementary base dot
        pen.color(color2)
        pen.goto(x, -y)
        pen.dot(10)

        # Determine complementary base
        pair = None
        if base == 'A': pair = 'T'
        elif base == 'T': pair = 'A'
        elif base == 'C': pair = 'G'
        elif base == 'G': pair = 'C'

        # Draw the connecting line between base pairs
        if pair:
            color = base_pair_colors.get((base, pair), "white")
            pen.color(color)
            pen.penup()
            pen.goto(x, y)
            pen.pendown()
            pen.goto(x, -y)

        x += 8  # Move to the right for next base pair

    pen.hideturtle()
    turtle.done()  # Keep the window open until user closes it
