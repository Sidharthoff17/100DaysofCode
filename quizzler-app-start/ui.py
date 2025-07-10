from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain


class QuizzlerUI:
    def __init__(self, quiz: QuizBrain):
        self.score = 0
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx= 50, pady=50, bg = THEME_COLOR)

        #setup canvas
        self.canvas = Canvas(width=300, height=414)
        self.question_text = self.canvas.create_text(
            150, 207,
            text="Some Question:",
            width=250,
            font=("Arial", 15, "bold"),
            fill="black"
        )
        self.canvas.grid(row=0, column=0, columnspan=2, pady=20)

        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_button_pressed)
        self.true_button.image = true_img  # Prevent garbage collection
        self.true_button.grid(row=1, column=1)

        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_button_pressed)
        self.false_button.image = false_img
        self.false_button.grid(row=1, column=0)

        self.score_label = Label(text= f"Score: {self.score}", fg = "white", bg = THEME_COLOR)
        self.score_label.place(x = 200, y= -10)

        self.get_next_qn()

        self.window.mainloop()

    def get_next_qn(self):
        self.canvas.config(bg="white")  # Reset canvas color

        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text, text="You've completed the quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_button_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1

        else:
            self.canvas.config(bg="red")
        self.score_label.config(text=f"Score: {self.score}")
        self.window.after(1000, self.get_next_qn)



