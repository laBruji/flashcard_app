from random import random
import tkinter as tk
from tkinter import ttk


class QuizView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=master.cget("bg"))
        self.master = master
        self.index = 0
        self.score = 0

        self.question_label = tk.Label(
            self,
            font=("Times New Roman", 24),
            background=master.cget("bg"),
        )
        self.question_label.pack(pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = ttk.Button(
                self,
                style="TButton",
                command=lambda idx=i: self.check_answer(idx),
            )
            btn.pack(pady=5)
            self.option_buttons.append(btn)

        self.result_label = tk.Label(
            self,
            font=("Times New Roman", 16),
            background=master.cget("bg"),
        )
        self.result_label.pack(pady=20)

        self.next_button = ttk.Button(
            self,
            text="Next",
            style="TButton",
            command=self.next_question,
        )
        self.next_button.pack(pady=10)

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
                text=f"What is the translation of '{flashcard.target_lang}'?"
            )

            # Generate options
            correct_option = flashcard.translation
            options = [correct_option] + [
                fc.translation for fc in self.master.flashcards if fc != flashcard
            ][:3]
            random.shuffle(options)

            for i, option in enumerate(options):
                self.option_buttons[i].config(text=option)

    def check_answer(self, idx):
        if self.master.flashcards:
            flashcard = self.master.flashcards[self.index]
            selected_option = self.option_buttons[idx].cget("text")
            if selected_option == flashcard.translation:
                self.result_label.config(text="Correct!")
                self.score += 1
            else:
                self.result_label.config(
                    text=f"Incorrect. The correct answer is {flashcard.translation}."
                )

    def next_question(self):
        if self.master.flashcards:
            self.index = (self.index + 1) % len(self.master.flashcards)
            self.result_label.config(text="")
            self.show_question()
