import tkinter as tk
import random
import time

colors = ["red", "green", "blue"]
pattern = []

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Flash")
        self.root.geometry("400x300")
        self.user_pattern = []

        self.label = tk.Label(root, text="Watch and Repeat!", font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.box_frame = tk.Frame(root)
        self.box_frame.pack()

        self.buttons = []
        for color in colors:
            btn = tk.Button(self.box_frame, bg=color, width=10, height=2,
                            command=lambda c=color: self.user_click(c), state="disabled")
            btn.pack(side=tk.LEFT, padx=10)
            self.buttons.append(btn)

        self.start_btn = tk.Button(root, text="Start Game", command=self.show_pattern)
        self.start_btn.pack(pady=20)

        self.result = tk.Label(root, text="", font=("Helvetica", 14))
        self.result.pack(pady=10)

    def show_pattern(self):
        self.result.config(text="")
        self.user_pattern = []
        self.start_btn.config(state="disabled")

        global pattern
        pattern = random.choices(colors, k=3)

        for i, color in enumerate(pattern):
            self.root.after(i * 700, lambda c=color: self.flash(c))
        self.root.after(2200, self.enable_buttons)

    def flash(self, color):
        for btn in self.buttons:
            if btn["bg"] == color:
                original = btn["bg"]
                btn.config(bg="white")
                self.root.after(300, lambda b=btn, c=original: b.config(bg=c))

    def enable_buttons(self):
        for btn in self.buttons:
            btn.config(state="normal")

    def user_click(self, color):
        self.user_pattern.append(color)
        if len(self.user_pattern) == 3:
            self.check_result()

    def check_result(self):
        for btn in self.buttons:
            btn.config(state="disabled")

        if self.user_pattern == pattern:
            self.result.config(text="✅ Correct! Great memory!", fg="green")
        else:
            self.result.config(text=f"❌ Oops! It was {pattern}", fg="red")

        self.start_btn.config(state="normal")

# Run game
root = tk.Tk()
game = MemoryGame(root)
root.mainloop()
