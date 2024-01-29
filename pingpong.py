#import statements
from turtle import Screen
from pad import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Screen setup
s = Screen()
s.bgcolor("black")
s.setup(width=800,height=600)
s.title("ping pong")
s.tracer(0)
def nothing():
    # paddle=Turtle()
    # paddle.shape("square")
    # paddle.color("white")
    # paddle.shapesize(stretch_wid=5, stretch_len=1)
    # paddle.penup()
    # paddle.goto(350,0)
    # def goup():
    #     paddle.sety(paddle.ycor()+20)
    # def godown():
    #     paddle.sety(paddle.ycor()-20)
    # s.listen()
    # s.onkeypress(goup,"Up")
    # s.onkeypress(godown,"Down")
    pass


#Objects initialization
pad1=Paddle(350,0,1,5)
pad2=Paddle(-350,0,1,5)
ball=Ball()
score=Scoreboard()

#Events
s.listen()
s.onkeypress(pad1.up,"Up")
s.onkeypress(pad1.down,"Down")
s.onkeypress(pad2.up,"w")
s.onkeypress(pad2.down,"s")


#Game start
game_on=True
while game_on:
    #Update the screen
    time.sleep(ball.velocity)
    s.update()
    ball.move()
    
    #If ball hits upper boundaries
    if ball.ycor() >= 290 or ball.ycor() <=-290:
        ball.bounce_y()
    
    #If the ball hits the paddles
    if (ball.distance(pad1) < 50 and ball.xcor()>320) or (ball.distance(pad2) < 50 and ball.xcor()<-320):
        ball.bounce_x()
    
    #If the ball passes the horizontal boundaries
    if ball.xcor() > 380 :
        ball.reset_position()
        score.lpoint()
    if ball.xcor() < -380 :
        ball.reset_position()
        score.rpoint()
    
    
    
s.exitonclick()