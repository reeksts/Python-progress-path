import tkinter as tk
from tkinter import ttk


def greet():
    print(f"Hello, {user_name.get() or 'World'}")

root = tk.Tk()

main = ttk.Frame(root)
main.pack(side='left')

tk.Label(main, text='Label top', bg='red').pack(side='top', expand=True, fill='both')
tk.Label(main, text='Label top', bg='red').pack(side='top', expand=True, fill='both')
tk.Label(root, text='Label left', bg='green').pack(side='top', expand=True, fill='both')

root.mainloop()
