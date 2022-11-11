import tkinter as tk
from tkinter import ttk
import tkinter.font as font

root = tk.Tk()
style = ttk.Style(root)
print(font.families())

warningLabelFont = font.Font(family="Helvetica", size=14, weight="bold")

name = ttk.Label(root, text="Hello World!", font=warningLabelFont)
entry = ttk.Entry(root, width=15)
button = ttk.Button(root, text="Press me")
name.pack()
entry.pack()
button.pack()


root.mainloop()