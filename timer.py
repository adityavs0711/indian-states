from turtle import Turtle
import time

TIME_LIMIT = 300
FONT = ("Courier", 20, "bold")


class Timer(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(200, 250)
        self.current_time = round(time.time())
        self.end_time = self.current_time + TIME_LIMIT
        self.show_timer()

    def show_timer(self):
        self.clear()
        self.write(arg=f"Time left = {self.end_time - round(time.time())}")
