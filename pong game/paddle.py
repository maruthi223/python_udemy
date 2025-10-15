import turtle

class Paddle(turtle.Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.x = x
        self.y = y
        self.shape("square")
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(self.x,self.y)
    
    def goup(self):
        y = self.ycor() + 20
        self.goto(self.xcor(),y)
    def godown(self):
        y = self.ycor() - 20
        self.goto(self.xcor(),y)