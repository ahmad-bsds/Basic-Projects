from turtle import Turtle

# constants
FONT = ('Arial', 20, 'normal')
ALIGN = 'center'


class Score(Turtle):  # score is inherit of Turtle. Mean all attributes of Turtle are valid for score.
    def __init__(self):
        super().__init__()  # inheritance.
        with open('score.txt') as read_score:
            high_score = read_score.read()
            self.high_score = int(high_score)
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(-60, 170)
        self.clear()
        self.update()

    def update(self):
        self.clear()
        self.write(f"                      Score: {self.score}", move=False, align='left', font=FONT)
        self.write(f"High score: {self.high_score}", move=False, align='right', font=FONT)

    def increase_score(self):
        self.score += 1
        # When score up update.
        self.update()

    def reset_score(self):
        """function to reset score when snack dies."""
        if self.high_score < self.score:
            self.high_score = self.score
        with open('score.txt', 'w') as score:  # mode 'w' mean erase previous first then write.
            content = score.write(f'{self.high_score}')
        self.score = 0
