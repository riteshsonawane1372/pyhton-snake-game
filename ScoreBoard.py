
from tkinter import CENTER
from turtle import Turtle


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.goto(0,270)
        self.score=0
        self.updateScore()
       
        self.hideturtle()

    def updateScore(self):
         self.write(f"Score :{self.score}",align="right",font=("Arial",24,"normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over ",align="right",font=("Arial",24,"normal"))


    def increase_score(self):
        self.score=self.score+10
        self.clear()
        self.updateScore()
        