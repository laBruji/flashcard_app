import tkinter as tk
from tkinter import ttk
from flashcard import Flashcard
from utils.file_operations import read_flashcards_from

from views.memorize_view import MemorizeView
from views.main_view import MainView
from views.quiz_view import QuizView

BACKGROUND_COLOR = "#F5F5F5"
COLOR_1 = "#3498DB"
COLOR_2 = "#2980B9"
FONT_FAMILY = "Times New Roman"
FONT_SIZE_HEADING = 48
FONT_SIZE_BUTTON = 16


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.flashcards = []
        self.title("Vocab Practice")
        self.geometry("500x300")
        self.config(padx=10, pady=10, bg=BACKGROUND_COLOR)

        self.main_view = MainView(self)
        self.main_view.pack(fill="both", expand=True)

    def show_memorize_view(self):
        self.main_view.pack_forget()
        self.memorize_view = MemorizeView(self)
        self.memorize_view.pack(fill="both", expand=True)

    def show_quiz_view(self):
        self.main_view.pack_forget()
        self.quiz_view = QuizView(self)
        self.quiz_view.pack(fill="both", expand=True)

    def show_main_view(self):
        self.memorize_view.pack_forget()
        self.quiz_view.pack_forget()
        self.main_view.pack(fill="both", expand=True)

    def read_flashcards_from(self, file):
        self.flashcards = read_flashcards_from(file)
