from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry('500x450')


def callback():
    label.config(text = 'You clicked me')

def callback2():
    val1=entry1.get()
    val2=entry2.get()
    print('Your name is : '+val1)
    print('Your password is : '+val2)


label = Label(root, text='Heloo Python')
##label['text'] = 'Hello Tkinter'
label.config(text='Hello Tkinter', fg='red')
label.config(font='Times 15')
label.config(bg='yellow')
label.config(text='Hello Python I love you so much')
label.config(wraplength='150')
label.config(justify='right')
##label.config(justify=RIGHT)
label.pack()

def callback():
    label.config(text = 'You clicked me', fg='red', bg='black')

button1 = Button(root, text='Click Me', command=callback)
button1['state'] = 'disabled'
button1['state'] = 'normal'
button2 = ttk.Button(root, text='Click Me')
button1.pack()
button2.pack()

entry1 = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)
entry1.insert(10,'Please enter your name')
entry2.config(show='*')
button3 = ttk.Button(root, text='REAAADYYYY', command=callback2)
button3.pack()
entry1.pack()
entry2.pack()
entry1.state(['disabled'])
entry1.state(['!disabled'])
entry1.state(['readonly'])



root.mainloop()
