from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry('600x600+350+350')

canvas = Canvas(root, width=650, height=550)
canvas.pack()

##line1 = canvas.create_line(100, 250, 360, 25)
##canvas.itemconfigure(line1, fill='red', width=10)

##line2 = canvas.create_line(25,50,150,150,250,140,25,50, fill='red', width=5)
##text = canvas.create_text(150, 30, text='Hello Python', font='times 15 bold')

rectangle = canvas.create_rectangle(150,150,250,200, fill='green', width=5)

oval = canvas.create_oval(350,350,250,200)

arc = canvas.create_arc(120,20,30,80, fill='red', width=3, start=0, extent=145)

icon = PhotoImage(file='person_icon.png')
image = canvas.create_image(150,200,image=icon)
canvas.lift(rectangle)

root.mainloop()
