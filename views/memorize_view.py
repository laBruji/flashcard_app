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
BUTTON_FONT = "Chalkboard"
BUTTON_FONT_SIZE = 16

# TODO: make sure a file is selected before entering this mode
# TODO: add check box to mark a word as learned
# TODO: change logic that shows the cards

class MemorizeView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=BACKGROUND_COLOR)
        self.master = master
        self.index = 0

        self.flashcard_label = tk.Label(
            self,
            font=(FONT_FAMILY, FONT_SIZE_H1),
            foreground=PRIMARY_COLOR,
            background=BACKGROUND_COLOR,
        )
        self.flashcard_label.pack(pady=100)

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
