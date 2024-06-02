import tkinter as tk
from utils.file_operations import read_flashcards_from

from views.main_view import MainView
from views.memorize_view import MemorizeView
from views.quiz_view import QuizView


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.flashcards = []
        self.title("Vocab Practice")
        self.geometry("800x600")
        self.main_view = MainView(self)
        self.main_view.pack(fill="both", expand=True)

    def read_flashcards_from(self, file):
        self.flashcards = read_flashcards_from(file)

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
