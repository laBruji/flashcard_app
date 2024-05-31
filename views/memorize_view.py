import tkinter as tk
from tkinter import ttk

class MemorizeView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=master.cget("bg"))
        self.master = master
        self.index = 0

        self.flashcard_label = tk.Label(
            self,
            font=("Times New Roman", 48),
            background=master.cget("bg"),
        )
        self.flashcard_label.pack(pady=50)

        self.flip_button = ttk.Button(
            self,
            text="Flip",
            style="TButton",
            command=self.flip_flashcard,
        )
        self.flip_button.pack(pady=10)

        self.next_button = ttk.Button(
            self,
            text="Next",
            style="TButton",
            command=self.next_flashcard,
        )
        self.next_button.pack(pady=10)

        self.back_button = ttk.Button(
            self,
            text="Back to Main",
            style="TButton",
            command=master.show_main_view,
        )
        self.back_button.pack(pady=10)

        self.show_flashcard()

    def show_flashcard(self):
        if self.master.flashcards:
            flashcard = self.master.flashcards[self.index]
            self.flashcard_label.config(text=flashcard.target_lang)

    def flip_flashcard(self):
        if self.master.flashcards:
            flashcard = self.master.flashcards[self.index]
            current_text = self.flashcard_label.cget("text")
            if current_text == flashcard.target_lang:
                self.flashcard_label.config(text=flashcard.translation)
            else:
                self.flashcard_label.config(text=flashcard.target_lang)

    def next_flashcard(self):
        if self.master.flashcards:
            self.index = (self.index + 1) % len(self.master.flashcards)
            self.show_flashcard()
