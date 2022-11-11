from tkinter import *
from tkinter import ttk
from tkinter import messagebox


root = Tk()
root.geometry('600x700')

chvar = IntVar()

def callback():
    print('Your name : '+entry1.get())
    print('Your password : '+entry2.get())
    if chvar.get() ==1:
        print('Remember me selected')
    else:
        print('Not selected')
    print(gender.get())
    print(months.get())
    print(year.get())
        
entry1 = ttk.Entry(root, width=30)
entry2 = ttk.Entry(root, width=30)
entry1.insert(0, 'Please enter your name')
entry2.insert(0, 'Please enter your password')
button = ttk.Button(root, text='Enter')
cbox = Checkbutton(root, text='Remember Me',
                   variable=chvar, font='Arial 16')

lbltitle = ttk.Label(text='Our Title', font=(('Arial'),22))
lblname = ttk.Label(text='Your Name: ')
lblpass = ttk.Label(text='Your Password: ')

lbltitle.grid(row=0, column=0, columnspan=2)
lblname.grid(row=1, column=0, sticky=W)
lblpass.grid(row=2, column=0)
entry1.grid(row=1, column=1)
entry2.grid(row=2, column=1)
button.grid(row=3, column=1, sticky=E+W, pady=5)
cbox.grid(row=4, column=0, sticky=E, columnspan=2)

chvar.set(0)

button.config(command=callback)



# RADIO BUTTON
gender = StringVar()
radiobutton1 = ttk.Radiobutton(root, text='male', value='male', var=gender)
radiobutton2 = ttk.Radiobutton(root, text='female', value='female', var=gender)
radiobutton1.grid(row=5, column=0)
radiobutton2.grid(row=5, column=1)



#COMBO BOX
numbers = []
for i in range(0,10):
    numbers.append(i)

months = StringVar()
comboBox = ttk.Combobox(root, textvariable = months,
                        state = 'readonly',
                        values= ('Jan', 'Feb', 'Mar', 'Apr'))
comboBox.grid(row=6, column=0)


#SPIN BOX - only in tk
year = StringVar()
spinbox = Spinbox(root,from_=1990, to=2018, textvariable=year,
                  state = 'readonly')
spinbox.grid(row=6, column=1)


#MESSAGE BOX
def callback1():
    mbox = messagebox.askquestion('Delete', 'Are you sure?', icon='warning')
    if mbox == 'yes':
        print('Deleted')
    else:
        print('Not deleted')
def callback2():
    messagebox.showinfo('Success', 'Well Done')
    print('You clicked OK')

button1=ttk.Button(root, text='Delete', command=callback1)
button1.grid(row=7, column=0, pady=25, padx=25)
button2=ttk.Button(root, text='Info', command=callback2)
button2.grid(row=7, column=1, pady=25, padx=25)



#TEXT EDITOR - only in tkinter
def callback3 ():
    result = textEditor.get(1.0, END)
    print(result)


textEditor = Text(root, width=30, height=10, font=(('Times'), 15), wrap=WORD)
textEditor.grid(row=8, column=0, pady=20, padx=30)

button3 = Button(root, text='Save', width=10, height=1, command=callback3)
button3.grid(row=9, column=0)
textEditor.insert(INSERT, 'Hello I am a tkinter widget')
textEditor.config(state='disabled')
textEditor.config(state='normal')


                     
root.mainloop()
