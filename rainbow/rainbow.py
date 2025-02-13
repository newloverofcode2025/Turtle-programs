import turtle

def draw_rainbow():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    turtle.speed(0)
    turtle.bgcolor("white")
    turtle.width(10)

    for i, color in enumerate(colors):
        turtle.penup()
        turtle.goto(0, -50 * (len(colors) - i - 1))
        turtle.pendown()
        turtle.color(color)
        turtle.circle(50 * (len(colors) - i))

    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    draw_rainbow()