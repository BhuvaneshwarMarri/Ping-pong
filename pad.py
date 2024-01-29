from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,posx,posy,length,width):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=length,stretch_wid=width)
        self.goto(posx,posy)
    
    def up(self):
        self.sety(self.ycor()+30)
        
    
    def down(self):
        self.sety(self.ycor()-30)