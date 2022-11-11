from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry('600x600+350+350')

textbox = Text(root, width=60, height=20, wrap='word')
textbox.grid(row=0, column=0)

sb = ttk.Scrollbar(root, orient='vertical', command=textbox.yview)
sb.grid(row=0, column=1, sticky=N+S)

textbox.config(yscrollcommand=sb.set)

root.mainloop()
