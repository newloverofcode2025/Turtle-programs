import turtle

def draw_circle(color, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.width(7)
    turtle.circle(30)

def main():
    turtle.speed(0)
    turtle.bgcolor("white")

    # Draw the top row of circles
    draw_circle("blue", -110, 0)
    draw_circle("black", 0, 0)
    draw_circle("red", 110, 0)

    # Draw the bottom row of circles
    draw_circle("yellow", -55, -50)
    draw_circle("green", 55, -50)

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()