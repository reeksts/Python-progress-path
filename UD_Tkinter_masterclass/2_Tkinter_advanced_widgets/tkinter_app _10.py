from tkinter import *
from tkinter import messagebox


root = Tk()
root.title('Menu bar')
root.geometry('600x600+350+350')

menuBar = Menu(root)
root.config(menu=menuBar)

file = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label = 'File', menu=file)
file.add_command(label = 'New')
file.add_separator()
file.add_command(label = 'Open')
file.add_command(label = 'Save')
icon = PhotoImage(file='icon2.png')

def funcExit():
    mbox = messagebox.askquestion('Exit', 'Are you sure?', icon='warning')
    if mbox == 'yes':
        root.destroy()
        
    

file.add_command(label = 'Exit', image = icon, compound = LEFT, command=funcExit)

edit = Menu(menuBar)
menuBar.add_cascade(label = 'Edit', menu=edit)

about = Menu(menuBar)
menuBar.add_cascade(label = 'About', menu=about)


                     
root.mainloop()
