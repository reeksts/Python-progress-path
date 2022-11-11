from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('600x600+350+350')

icon = PhotoImage(file = 'icon.png')

tabs = ttk.Notebook()
tabs.pack(fill=BOTH, expand=True)
tab1 = ttk.Frame(tabs)
tab2 = ttk.Frame(tabs)
tabs.add(tab1, text = 'First Tab')
tabs.add(tab2, text = 'Second Tab', image=icon, compound=LEFT)

lbl = ttk.Label(tab1, text = 'Hello')
lbl.place(x=200, y=200)

button = ttk.Button(tab2, text = 'Click Me')
button.place(x=250, y=250)

                     
root.mainloop()
