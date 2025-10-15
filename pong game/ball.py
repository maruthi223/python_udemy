import turtle

class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape("circle")
        self.penup()
        self.ny = 10
        self.nx = 10
        self.move_speed = 0.1

    def move(self):
        x = self.xcor()+self.nx
        y= self.ycor()+self.ny
        self.goto(x,y)

    def bounce_y(self): 
        self.ny *=-1
    def bounce_x(self):
        self.nx *=-1
        self.move_speed * 0.9
    def regame(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()