from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizeInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20 , pady=20, bg=THEME_COLOR)



        self.canvas = Canvas(width=300, height=250,bg="white")
        self.quetion_text = self.canvas.create_text(150,125,width=280,text="hello",font=("Arial",20,"italic"),fill=THEME_COLOR )
        self.canvas.grid(column= 0,row=1,pady=50,columnspan=2)

        self.label = Label()
        self.label.config(text="Score:0", fg="white", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)

        self.image = PhotoImage(file="images/false.png")
        self.button_1 = Button(image=self.image, bg=THEME_COLOR, highlightthickness=0,command=self.ans_false)
        self.button_1.grid(column=1, row=2)

        self.image_2 = PhotoImage(file="images/true.png")
        self.button_2 = Button(image=self.image_2, bg=THEME_COLOR, highlightthickness=0,command=self.ans_true)
        self.button_2.grid(column=0, row=2)


        self.get_next_question()



        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quetion_text,text=q_text)
        else:
            self.canvas.itemconfig(self.quetion_text,text="You've reached end of the quiz.")
            self.button_1.config(state="disabled")
            self.button_2.config(state="disabled")
    def ans_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def ans_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)

