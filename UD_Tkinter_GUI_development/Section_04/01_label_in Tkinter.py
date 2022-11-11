import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
    

root = tk.Tk()
root.geometry("600x400")
root.resizable(False, False)
root.title("Widget Examples")

image = Image.open("logo.png").resize((64,64))
photo = ImageTk.PhotoImage(image)

greeting = tk.StringVar()

label = ttk.Label(root, textvariable=greeting, image=photo, padding=5, compound='right')
label.pack()


greeting.set("babamm")

root.mainloop()
