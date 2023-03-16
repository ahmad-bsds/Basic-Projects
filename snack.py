from turtle import Turtle

positions = [(20, 0), (0, 0), (-20, 0)]
UP = 90
LEFT = 180
RIGHT = 360
DOWN = 270


class Snack:
    def __init__(self):
        self.snack_segments = []
        self.create_snack()
        self.head = self.snack_segments[0]

    def create_snack(self):
        # Create a snack.
        for _ in range(0, 3):
            self.snack = Turtle('square')
            self.snack.fillcolor('white')
            self.snack.goto(positions[_])
            self.snack.pencolor('white')
            self.snack.penup()
            self.snack_segments.append(self.snack)
        self.snack_segments[0].shape('turtle')

    def move(self):
        # Run snack
        for seg_nums in range(len(self.snack_segments) - 1, 0, -1):  # -1 third parameter is step , it means reverse.
            x = self.snack_segments[seg_nums - 1].xcor()
            y = self.snack_segments[seg_nums - 1].ycor()
            self.snack_segments[seg_nums].goto(x, y)
        self.snack.speed('fastest')
        self.snack_segments[0].forward(21)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() == RIGHT:
            self.head.setheading(DOWN)
        elif self.head.heading() == LEFT:
            self.head.setheading(DOWN)
        elif self.head.heading() == 0:
            self.head.setheading(DOWN)

    def reset(self):
        for seg in self.snack_segments:
            seg.goto(1000, 1000)
        self.snack_segments.clear()
        self.create_snack()
        self.head = self.snack_segments[0]

    def size(self):
        self.snack = Turtle('square')
        self.snack.hideturtle()
        self.snack.fillcolor('white')
        x = self.snack_segments[-1].xcor()
        y = self.snack_segments[-1].ycor()
        self.snack.penup()
        self.snack.goto(x, y)
        self.snack.showturtle()
        # See in food file why hide and show.
        self.snack.pencolor('white')
        self.snack_segments.append(self.snack)
