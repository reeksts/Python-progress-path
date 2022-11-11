import tkinter as tk
from tkinter import ttk


def greet():
    print("Hello, World!")

root = tk.Tk()

greet_button = ttk.Button(root, text='greet', command=greet)
greet_button.pack(side='left', fill='both', expand=True)

quit_button = ttk.Button(root, text='quit', command=root.destroy)
quit_button.pack(side='left')

root.mainloop()
