from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="score: 0", padx=20, pady=20, bg=THEME_COLOR, highlightthickness=0, fg="white",
                                 font=("Arial", 14, "normal"))
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="Question", font=("Arial", 14, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=(50, 25))

        correct_image = PhotoImage(file="./images/true.png")
        self.correct_button = Button(image=correct_image, bg=THEME_COLOR, pady=20, highlightthickness=0,
                                     command=self.check_true)
        self.correct_button.grid(column=0, row=2)

        false_image = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_image, bg=THEME_COLOR, padx=20, pady=20, highlightthickness=0,
                                   command=self.check_false)
        self.false_button.grid(column=1, row=2, pady=20)

        self.quiz_brain = quiz_brain
        self.display_next_question()

        self.window.mainloop()

    def display_next_question(self):
        self.canvas.itemconfig(self.question_text, text=self.quiz_brain.next_question())

    def check_true(self):
        self.update_score("true")
        self.display_next_question()

    def check_false(self):
        self.update_score("false")
        self.display_next_question()

    def update_score(self, user_answer: str):
        if self.quiz_brain.check_answer(user_answer):
            self.window.config(bg="green")
            self.window.after(250, func=self.change_back_bg)
        else:
            self.window.config(bg="red")
            self.window.after(250, func=self.change_back_bg)

        self.score_label.config(text=f"score: {self.quiz_brain.get_score()}")

        if self.quiz_brain.still_has_questions():
            return
        else:
            self.correct_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def change_back_bg(self):
        self.window.config(bg=THEME_COLOR)

