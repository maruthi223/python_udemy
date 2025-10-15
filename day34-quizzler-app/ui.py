THEME_COLOR = "#375362"

import tkinter
from quiz_brain import QuizBrain

class Quizui:

    def __init__(self,quizq:QuizBrain):
        self.quiz = quizq
        
        self.window = tkinter.Tk()
        self.window.title('QUIZ GAME')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.label = tkinter.Label(text=f"Score : {self.quiz.score}",font=('Arial',14),bg=THEME_COLOR,fg='white')
        self.label.grid(row=0,column=1)

        self.canvas = tkinter.Canvas(width=300, height=250,bg='white')
        self.question = self.canvas.create_text(150,125,width=280,text='question',font=('Arial',20,'italic'))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        wrong = tkinter.PhotoImage(file='false.png') 
        self.button1 = tkinter.Button(image=wrong,highlightthickness=0,command=self.false_press)
        self.button1.grid(row=2,column=1)

        right = tkinter.PhotoImage(file='true.png') 
        self.button = tkinter.Button(image=right,highlightthickness=0,command=self.true_press)
        self.button.grid(row=2,column=0)
        self.quiz_question()
        self.window.mainloop()

    def quiz_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.label.config(text=f'Score:{self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question,text=q_text)
        else:
            self.canvas.itemconfig(self.question,text = 'you have reached max questionns')
            self.button.config(state='disabled')
            self.button1.config(state='disabled')
    def true_press(self):
        self.feedback(self.quiz.check_answer('true'))

    def false_press(self):
        self.feedback(self.quiz.check_answer('false'))

    def feedback(self,answer):
        if answer:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.quiz_question)