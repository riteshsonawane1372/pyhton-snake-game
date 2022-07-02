from turtle import Screen
import time
from SnakeClass import *
from food import *
from ScoreBoard import *

#? Setting up the screen 
my_Screen=Screen()
food_obj=Food()
scorebrd= scoreboard()



my_Screen.setup(width=600,height=600)
my_Screen.bgcolor("black")
my_Screen.title("Snake Game")
my_Screen.tracer(0)


# Creating an SNake obj

snake_obj= Snake()

# Creating Food Class 



snake_obj.create_Snake()

my_Screen.listen()
my_Screen.onkey(snake_obj.up,"Up")
my_Screen.onkey(snake_obj.right,"Right")
my_Screen.onkey(snake_obj.left,"Left")
my_Screen.onkey(snake_obj.down,"Down")







game_on=True

while game_on:
    my_Screen.update()
    time.sleep(0.08)
    snake_obj.move()

    # Detect Collision Using the distance in turtle 

    if(snake_obj.segement[0].distance(food_obj)<15):
        food_obj.refreshLocation()
        snake_obj.extend()
        scorebrd.increase_score()
    
    for segment in snake_obj.segement:

        if segment==snake_obj.segement[0]:
            pass

        elif(snake_obj.segement[0].distance(segment)<10):
            
            scorebrd.game_over()
            game_on=False

    # Detect Collision with the wall 
    if(snake_obj.segement[0].xcor()>280 or 
        snake_obj.segement[0].xcor()< -280 or
        snake_obj.segement[0].ycor()>280 or 
        snake_obj.segement[0].ycor()<-280):
        game_on=False
        scorebrd.game_over()
        
        
      



    





my_Screen.exitonclick()







