import tkinter as tk
from tkinter import ttk, filedialog

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

class MainView(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg=BACKGROUND_COLOR)
        self.master = master
        style = ttk.Style(master)
        style.theme_use("clam")

        # Heading 1
        h1 = tk.Label(
            self,
            text="Flashcards",
            foreground=PRIMARY_COLOR,
            background=BACKGROUND_COLOR,
            font=(FONT_FAMILY, FONT_SIZE_H1),
        )
        h1.pack(pady=(125, 0))

        # Button style for memorize and quiz modes
        style.configure(
            "TButton",
            font=(BUTTON_FONT, BUTTON_FONT_SIZE),
            foreground=TEXT_COLOR_LIGHT,
            background=PRIMARY_COLOR,
            bordercolor=BACKGROUND_COLOR,
        )

        # Map button style for hover and active states
        style.map(
            "TButton",
            foreground=[("active", TEXT_COLOR_DARK), ("hover", TEXT_COLOR_DARK)],
            background=[("active", SECONDARY_COLOR), ("hover", SECONDARY_COLOR)],
        )

        button_frame = tk.Frame(self, background=BACKGROUND_COLOR)
        button_frame.pack()

        self.memorize_button = ttk.Button(
            button_frame,
            text="Memorize",
            style="TButton",
            command=master.show_memorize_view,
        )
        self.memorize_button.grid(row=0, column=0, padx=30, pady=10)

        self.quiz_button = ttk.Button(
            button_frame,
            text="Quiz",
            style="TButton",
            command=master.show_quiz_view,
        )
        self.quiz_button.grid(row=0, column=1, padx=30, pady=10)

        # Upload file button
        self.upload_button = ttk.Button(
            self,
            text="Upload File",
            style="TButton",
            command=self.upload_file,
        )
        self.upload_button.pack(side="left", padx=30, pady=30, anchor="sw")

        # TODO put this label closer to the upload button
        self.file_label = tk.Label(
            self,
            text="No file selected",
            foreground=TEXT_COLOR_DARK,
            background=BACKGROUND_COLOR,
            font=("Times New Roman", BUTTON_FONT_SIZE),
        )
        self.file_label.pack(side="left", pady=35, anchor="sw")

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
            self.upload_button.config(text="Load new file")
