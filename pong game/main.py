from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)


r_paddle = Paddle(350,0)
l_paddle = Paddle(-350,0)
b = Ball()
s = Score()

i=0.005
screen.listen()
screen.onkey(r_paddle.goup,"Up")
screen.onkey(r_paddle.godown,"Down")
screen.onkey(l_paddle.goup,"w")
screen.onkey(l_paddle.godown,"s")
is_on = True
while is_on:
    time.sleep(b.move_speed)
    screen.update()
    b.move()
    if b.ycor()>280 or b.ycor()<-280:
        b.bounce_y()

    if b.distance(r_paddle) < 50 and b.xcor()>320:
        b.bounce_x()

    if b.distance(l_paddle) < 50 and b.xcor()<-320:
        b.bounce_x()

    if b.xcor() > 380: 
        b.regame()
        s.ls()
        s.update()
    
    if b.xcor() < -380:
        b.regame()
        s.rs()
        s.update()
screen.exitonclick()
