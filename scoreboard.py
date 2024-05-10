from turtle import Turtle

NORMAL_FONT = ("Courier", 10, "bold")
BOLD_FONT = ("Arial", 20, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(200, 300)
        self.score = 0
        self.write_score()

    def increment_score(self):
        self.score += 1
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(arg=f"Score : {self.score}/37", font=NORMAL_FONT)

    def final_score(self):
        self.goto(0, 0)
        self.write(arg=f"Game Over, Your final score is {self.score}", align="center", font=BOLD_FONT)
        self.goto(0, -30)
        if self.score < 15:
            self.write(arg="Poor!", align="center", font=BOLD_FONT)
        elif self.score < 30:
            self.write(arg="You are good. Try again.", align="center", font=BOLD_FONT)
        elif self.score < 37:
            self.write(arg="You are very close in getting all correct. Keep trying.", align="center", font=BOLD_FONT)

    def finished_early(self, time_left):
        self.goto(0, -50)
        self.write(arg=f"You finished {time_left} seconds earlier.", align="center", font=NORMAL_FONT)
        self.goto(0, -70)
        self.write(arg="Brilliant!", align="center", font=NORMAL_FONT)
