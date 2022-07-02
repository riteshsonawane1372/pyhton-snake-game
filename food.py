#Whenever the food touches the food class the food moves top the random location 

import random
from turtle import Turtle

score =10

class Food(Turtle,):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("green")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        self.goto(x,y) # Giving random location 

    def refreshLocation(self):
        x=random.randint(-280,280)
        y=random.randint(-280,280)
        self.goto(x,y)
