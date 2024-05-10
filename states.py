import pandas
from turtle import Turtle

FONT = ("Courier", 10, "bold")


class StatesDatabase(Turtle):

    def __init__(self):
        super().__init__()
        self.states_db = pandas.read_csv("States Coordinates.csv")
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.resizemode(rmode="user")
        self.color("red", "green")

    def match_state(self, state):
        if state in self.states_db.states.to_list():
            return True

    def write_state_name(self, state):
        x_cor = self.states_db[self.states_db.states == state].x.to_list()[0]
        print(x_cor)
        y_cor = self.states_db[self.states_db.states == state].y.to_list()[0]
        print(y_cor)
        self.goto(x_cor, y_cor)
        self.write(arg=state, font=FONT, align="center")
