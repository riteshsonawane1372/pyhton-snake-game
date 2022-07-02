from turtle import Turtle,Screen, right 
# IN python the const is name in all caps 

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
RIGHT=0
LEFT=180
DOWN=270
UP=90


class Snake:
    def __init__(self):
        self.segement=[]
        self.create_Snake()
        self.move()

    def create_Snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)
       
    
    def move(self):
        for k in range(len(self.segement)-1,0,-1): # k her is the position 
            new_x=self.segement[k-1].xcor()
            new_y=self.segement[k-1].ycor()
            self.segement[k].goto(new_x,new_y)

        self.segement[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.segement[0].heading()!=DOWN:
         self.segement[0].setheading(UP)
    
    def right(self):
        if self.segement[0].heading()!=LEFT:
            self.segement[0].setheading(RIGHT)
    
    def down(self):
        if self.segement[0].heading()!=UP:
         self.segement[0].setheading(DOWN)

    def left (self):
        if self.segement[0].heading()!=RIGHT:
            self.segement[0].setheading(LEFT)

    def add_segment(self,position):
         for i in STARTING_POSITION:
            control_1 = Turtle()
            control_1.shape("square")
            control_1.color("white")
            control_1.penup()
            control_1.goto(i)
            self.segement.append(control_1)
         

    def extend(self):
        self.goto()
        self.add_segment(self.segement[-1].position())
    

# Now you can create a new snake class 