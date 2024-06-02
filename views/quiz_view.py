import random
import tkinter as tk
from tkinter import ttk

# Define color constants
PRIMARY_COLOR = "#720026"
SECONDARY_COLOR = "#450017"
BACKGROUND_COLOR = "#F0F0F0"
TEXT_COLOR_DARK = "#737374"
TEXT_COLOR_LIGHT = "#FFFFFF"

# Define font constants
FONT_FAMILY = "Chalkduster"
FONT_SIZE_H1 = 96
FONT_SIZE_H2 = 36
BUTTON_FONT = "Chalkboard"
BUTTON_FONT_SIZE = 16

# TODO
# smaller space for user entry
# label saying whether it was correct is not showing up
# update all the logic

class QuizView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=PRIMARY_COLOR)
        self.master = master
        self.index = 0
        self.score = 0

        self.question_label = tk.Label(
            self,
            font=(FONT_FAMILY, FONT_SIZE_H2),
            foreground=BACKGROUND_COLOR,
            background=PRIMARY_COLOR,
        )
        self.question_label.pack(pady=100)

        self.answer_entry = tk.Entry(
            self, 
            font=(BUTTON_FONT, FONT_SIZE_H2),
            background=BACKGROUND_COLOR,
            foreground=PRIMARY_COLOR)
        self.answer_entry.pack()

        self.result_label = tk.Label(
            self,
            text="",
            foreground=BACKGROUND_COLOR,
            background=PRIMARY_COLOR,
            font=(BUTTON_FONT, BUTTON_FONT_SIZE),
        )
        self.result_label.pack(pady=(25, 15))

        self.submit_button = ttk.Button(
            self, text="Check", style="TButton", command=self.check_answer
        )
        self.submit_button.pack(pady=10)

        self.back_button = ttk.Button(
            self,
            text="Back to Main",
            style="TButton",
            command=master.show_main_view,
        )
        self.back_button.pack(pady=10)

        self.show_question()

    def show_question(self):
        if self.master.flashcards:
            flashcard = self.master.flashcards[self.index]
            self.question_label.config(
                text=f"How do you write '{flashcard.translation}'?"
            )

    def check_answer(self):
        if self.master.flashcards:
            flashcard = self.master.flashcards[self.index]
            user_input = self.answer_entry.get()
            
            if user_input == flashcard.target_lang:
                self.result_label.config(text="Correct!")
                self.score += 1
            else:
                self.result_label.config(
                    text=f"Incorrect. The correct answer is {flashcard.target_lang}."
                )
            self.next_question()

    def next_question(self):
        if self.master.flashcards:
            self.index = (self.index + 1) % len(self.master.flashcards)
            self.result_label.config(text="")
            self.show_question()
            self.answer_entry.delete(
                0, tk.END
            ) 
