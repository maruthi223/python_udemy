self.window = tkinter.Tk()
        self.window.title('QUIZ GAME')
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.label = tkinter.Label(text="Score",font=('Arial',20),bg=THEME_COLOR,fg='white')
        self.label.config(padx=20,pady=20)
        self.label.grid(row=0,column=1)

        self.canvas = tkinter.Canvas(width=300, height=250,bg='white')
        self.canvas.grid(row=1,column=0,columnspan=2)

        self.wrong = tkinter.PhotoImage(file='false.png') 
        self.button1 = tkinter.Button(image=self.wrong)
        self.button1.grid(row=2,column=0)

        self.right = tkinter.PhotoImage(file='true.png') 
        self.button = tkinter.Button(image=self.right)
        self.button.grid(row=2,column=1)
        self.window.mainloop()