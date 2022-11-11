import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)

style.configure("CustomEntryStyle.TEntry", padding=20)

name = ttk.Label(root, text="Hello World!")
name.pack()
entry = ttk.Entry(root, width=15)
entry["style"] = "CustomEntryStyle.TEntry"
entry.pack()


root.mainloop()
