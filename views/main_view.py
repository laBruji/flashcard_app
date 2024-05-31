import tkinter as tk
from tkinter import ttk, filedialog


class MainView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=master.cget("bg"))
        self.master = master

        welcome_heading = tk.Label(
            self,
            text="Welcome!",
            foreground="#2980B9",
            background=master.cget("bg"),
            font=("Times New Roman", 48),
        )
        welcome_heading.pack(pady=20)

        style = ttk.Style(master)
        style.theme_use("default")

        style.configure(
            "TButton",
            font=("Times New Roman", 16),
            foreground="#3498DB",
            background=master.cget("bg"),
        )

        style.map(
            "TButton",
            foreground=[("active", "#2980B9")],
        )

        button_frame = tk.Frame(self, background=master.cget("bg"))
        button_frame.pack(pady=30)

        memorize_button = ttk.Button(
            button_frame,
            text="Memorize",
            style="TButton",
            command=master.show_memorize_view,
        )
        memorize_button.grid(row=0, column=0, padx=30, pady=10)

        quiz_button = ttk.Button(
            button_frame,
            text="Quiz Yourself!",
            style="TButton",
            command=master.show_quiz_view,
        )
        quiz_button.grid(row=0, column=1, padx=30, pady=10)

        upload_button = ttk.Button(
            self,
            text="Upload File",
            style="TButton",
            command=self.upload_file,
        )
        upload_button.pack(side="left", padx=30, pady=10, anchor="sw")

        self.file_label = tk.Label(
            self,
            text="No file selected",
            foreground="#2980B9",
            background=master.cget("bg"),
            font=("Times New Roman", 16),
        )
        self.file_label.pack(side="left", pady=15, anchor="sw")

        self.remove_button = ttk.Button(
            self,
            text="X",
            style="TButton",
            padding=0,
            command=self.remove_file,
        )
        self.remove_button.pack_forget()

    def upload_file(self):
        file_path = filedialog.askopenfilename(
            initialdir=".",
            title="Select a File",
            filetypes=(("Text files", "*.txt"), ("all files", "*.*")),
        )
        if file_path:
            self.master.read_flashcards_from(file_path)
            self.file_label.config(
                text=f"Loaded {len(self.master.flashcards)} words from {file_path.split('/')[-1]}"
            )
            self.remove_button.pack(side="left", pady=15, anchor="sw")

    def remove_file(self):
        self.file_label.config(text="No file selected")
        self.remove_button.pack_forget()
        self.master.flashcards = []
