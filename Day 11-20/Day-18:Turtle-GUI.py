#Circle Spirograph Program

import turtle
import math
import random

def random_color():
    # Generate a random color in the format #RRGGBB
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def draw_spirograph(radius, speed):
    turtle.width(2)
    turtle.speed(speed)

    for _ in range(100):
        color1 = random_color()
        color2 = random_color()
        turtle.color(color1, color2)
        turtle.circle(radius)
        turtle.left(360 / 100)

def main():
    turtle.bgcolor("black")
    turtle.title("Spirograph")

    draw_spirograph(100, speed=40)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()
