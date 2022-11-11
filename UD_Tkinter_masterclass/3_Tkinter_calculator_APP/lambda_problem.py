from tkinter import *

root = Tk()
root.title('Calculator App')
root.geometry('380x550+850+200')
root.resizable(False, False)

def enterNumber(x):
    if entry_box.get() == 'O':
        entry_box.delete(0, END)
        entry_box.insert(0, str(x))
    else:
        length = len(entry_box.get())
        entry_box.insert(length, str(x))

entry_box = Entry(font='verdana 14 bold', width=22, bd=10, justify=RIGHT, bg='#e6e6fa')
entry_box.place(x=20, y=10)
entry_box.insert(0, 'O')

btn_numbers = []
for i in range(10):
    btn_numbers.append(Button(width=4, text=str(i), font='times 15 bold', bd=5,
                              command=lambda x=i: enterNumber(x)))
btn_text = 1
for i in range (3):
    for j in range (3):
        btn_numbers[btn_text].place(x=25+j*90, y=70+i*70)
        btn_text += 1


root.mainloop()
