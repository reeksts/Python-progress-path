from tkinter import *

root = Tk()
root.title('Frames')
root.geometry('650x650+650+350')

frame = Frame(root, height=300, width=300, bg='red', bd='7', relief=SUNKEN)
frame.pack(fill=X)

button1 = Button(frame, text='Button1')
button1.pack(side=LEFT, padx=20, pady=50)
button2 = Button(frame, text='Button2')
button2.pack(side=LEFT, padx=20)

searchBar = LabelFrame(root, text='Search Box', padx=20, pady=20, bg='#fcd45d')
lbl = Label(searchBar,text='Search')
lbl.pack(side=LEFT, padx=10)
searchBar.pack(side=TOP)
entry = Entry(searchBar)
entry.pack(side=LEFT, padx=10)
button3 = Button(searchBar, text='Search')
button3.pack(side=LEFT, padx=10)

                     
root.mainloop()
