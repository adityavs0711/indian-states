import turtle
from scoreboard import Scoreboard
from states import StatesDatabase
from timer import Timer
import time

screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.bgpic("map_of_india.gif")

scoreboard = Scoreboard()
states_database = StatesDatabase()
clock = Timer()

answered = []

while scoreboard.score < 37 and clock.end_time > time.time():
    user_answer = screen.textinput(title="Guess!", prompt="What is the name of another state/UT?").title()
    clock.show_timer()
    if user_answer not in answered:
        if states_database.match_state(user_answer):
            states_database.write_state_name(user_answer)
            scoreboard.increment_score()
            answered.append(user_answer)

scoreboard.final_score()
if clock.end_time - time.time() > 0:
    scoreboard.finished_early(round(clock.end_time - time.time()))

screen.mainloop()
