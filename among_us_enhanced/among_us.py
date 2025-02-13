import turtle

class AmongUsCharacter:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y
        self.body = None
        self.face = None
        self.eyes = []
        self.mouth = None
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.pen.hideturtle()

    def draw_body(self):
        self.pen.penup()
        self.pen.goto(self.x, self.y - 100)
        self.pen.pendown()
        self.pen.color(self.color)
        self.pen.begin_fill()
        self.pen.circle(100)
        self.pen.end_fill()

    def draw_face(self):
        self.pen.penup()
        self.pen.goto(self.x, self.y)
        self.pen.pendown()
        self.pen.color("white")
        self.pen.begin_fill()
        self.pen.circle(50)
        self.pen.end_fill()

    def draw_eyes(self):
        self.eyes = []
        for offset in [-20, 20]:
            self.pen.penup()
            self.pen.goto(self.x + offset, self.y + 60)
            self.pen.pendown()
            self.pen.color("black")
            self.pen.begin_fill()
            self.pen.circle(10)
            self.pen.end_fill()
            self.eyes.append((self.x + offset, self.y + 60))

    def draw_mouth(self):
        self.pen.penup()
        self.pen.goto(self.x - 20, self.y + 30)
        self.pen.pendown()
        self.pen.color("black")
        self.pen.setheading(-60)
        self.pen.circle(20, 120)

    def draw(self):
        self.draw_body()
        self.draw_face()
        self.draw_eyes()
        self.draw_mouth()

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.pen.clear()
        self.draw()

def main():
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Among Us Character")

    character = AmongUsCharacter("blue", 0, 0)
    character.draw()

    def move_up():
        character.move(0, 10)

    def move_down():
        character.move(0, -10)

    def move_left():
        character.move(-10, 0)

    def move_right():
        character.move(10, 0)

    screen.onkeypress(move_up, "Up")
    screen.onkeypress(move_down, "Down")
    screen.onkeypress(move_left, "Left")
    screen.onkeypress(move_right, "Right")
    screen.listen()

    screen.mainloop()

if __name__ == "__main__":
    main()