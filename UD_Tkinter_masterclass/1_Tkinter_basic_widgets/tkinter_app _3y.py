from tkinter import *

root = Tk()
root.geometry('450x450+650+350')


title = Label (root, text='Place Geomtry Manager', font=(('Verdana'), 15))
name_txt = Label(root, text='Name :')
password_txt = Label(root, text='Password :')
name_input = Entry(root, width=30)
pass_input = Entry(root, width=30)
button1 = Button(root, text='Save')
button2 = Button(root, text='Click me', bg='red')

title.place(x=100, y=20)
name_txt.place(x=20, y=80)
name_input.place(x=100, y=80)
password_txt.place(x=20, y=110)
pass_input.place(x=100, y=110)
button1.place(x=250, y=140)
button2.place(relx=0.5, rely=0.5, anchor='center')
                     
root.mainloop()
