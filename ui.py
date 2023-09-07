from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 12, "italic")


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz
        self.score = 0
        self.window = Tk()
        self.window.title("Quiz Game App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score_label = Label(text=f"Score: {self.score}", pady=20, padx=20, bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)
        self.canvas = Canvas(height=250, width=300)
        self.canvas.config(bg="white", highlightthickness=1)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=200,
            text="Some question gonna be here",
            fill=THEME_COLOR,
            font=FONT,
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.false_image = PhotoImage(file="./images/false.png")
        self.true_image = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=self.true_image, padx=20, pady=50, highlightthickness=0,
                                  command=self.get_check_answer_true)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=self.false_image, padx=20, pady=50, highlightthickness=0,
                                   command=self.get_check_answer_false)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        try:
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        except IndexError:
            self.canvas.itemconfig(self.question_text, text=f"All done. Game over! Score:{self.score}/{len(self.quiz.question_list)}")

    def get_check_answer_true(self):
        quiz_answer=self.quiz.check_answer()
        still_has_question = self.quiz.still_has_questions()
        if quiz_answer == "True"and still_has_question:
            self.score += 1
            self.get_next_question()
            self.score_label.config(text=f"Score: {self.score}")
        elif quiz_answer == "False":
            self.get_next_question()
    def get_check_answer_false(self):
        quiz_answer = self.quiz.check_answer()
        still_has_question=self.quiz.still_has_questions()
        if quiz_answer == "False" and still_has_question:
            self.score += 1
            self.get_next_question()
            self.score_label.config(text=f"Score: {self.score}")
        elif quiz_answer == "True":
            self.get_next_question()
