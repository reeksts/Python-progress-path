import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)
style.theme_use("clam")

style.map("CustomButton.TButton",
          foreground=[("pressed", "red"), ("active", "white")],
          background=[("pressed", "!disabled", "black"), ("active", "black")],
          font=[("pressed", ("TkDefaultFont", 11))])

name = ttk.Label(root, text="Hello World!")
entry = ttk.Entry(root, width=15)
button = ttk.Button(root, text="Press me", style="CustomButton.TButton")
name.pack()
entry.pack()
button.pack()


root.mainloop()
