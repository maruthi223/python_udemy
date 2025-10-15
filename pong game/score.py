import turtle

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
       
        self.color('white')
        self.hideturtle()
        self.penup()
        self.lscore = 0
        self.rscore = 0
        self.update()
    def update(self):
        self.clear()
        self.goto(-100,250)
        self.write(self.lscore,align='center',font=('roboto','24','normal'))
        self.goto(100,250)
        self.write(self.rscore,align='center',font=('roboto','24','normal'))
    def ls(self):
        self.lscore +=1
    def rs(self):
        self.rscore +=1