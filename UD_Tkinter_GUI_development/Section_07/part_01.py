import tkinter as tk
from tkinter import ttk

root = tk.Tk()
style = ttk.Style(root)
print(style.theme_names())
print(style.theme_use())

name = ttk.Label()
entry = ttk.Entry()
name.pack()

print(name["style"])
print(name.winfo_class())

style.configure("TLabel", font=("Segoe UI", 20))


root.mainloop()
