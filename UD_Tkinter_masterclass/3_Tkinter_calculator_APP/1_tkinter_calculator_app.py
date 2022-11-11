from tkinter import *
root = Tk()
root.title('Calculator App')
root.geometry('380x550+850+200')
root.resizable(False, False)

###############   FUNCTIONS   ################################


def enterNumber(x):
    if entry_box.get() == 'O':
        entry_box.delete(0, END)
        entry_box.insert(0, str(x))
    else:
        length = len(entry_box.get())
        entry_box.insert(length, str(x))


def enterOperator(x):
    if entry_box.get() != 'O':
        length = len(entry_box.get())
        entry_box.insert(length, btn_operator[x]['text'])


def funcClear():
    entry_box.delete(0, END)
    entry_box.insert(0, 'O')

result = 0
result_list = []


def funcOperator():
    content = entry_box.get()
    result = eval(content)
    entry_box.delete(0, END)
    entry_box.insert(0, str(result))

    result_list.append(content)
    result_list.reverse()
    status_bar.config(text='History : ' + '| '.join(result_list[:5]), font='verdana 11 bold')
    

def funcDelete():
    length = len(entry_box.get())
    entry_box.delete(length-1, END)
    if length == 1:
        entry_box.insert(0, 'O')




###############   ENTRY BOX   ##########################################################################################

entry_box = Entry(font='verdana 14 bold', width=22, bd=10, justify=RIGHT, bg='#e6e6fa')
entry_box.place(x=20, y=10)
entry_box.insert(0, 'O')




###############   NUMBER BUTTONS   #####################################################################################
btn_numbers = []
for i in range(10):
    btn_numbers.append(Button(width=4, text=str(i), font='times 15 bold', bd=5,
                              command=lambda x=i: enterNumber(x)))
btn_text = 1
for i in range (3):
    for j in range (3):
        btn_numbers[btn_text].place(x=25+j*90, y=70+i*70)
        btn_text += 1




###############   OPERATOR BUTTONS   ###################################################################################

btn_operator = []

for i in range(4):
    btn_operator.append(Button(width=4, font='times 15 bold', bd=5, command=lambda x=i: enterOperator(x)))

btn_operator[0]['text'] = '+'
btn_operator[1]['text'] = '-'
btn_operator[2]['text'] = '*'
btn_operator[3]['text'] = '/'

for i in range(4):
    btn_operator[i].place(x=290, y=70+i*70)




###############   OTHER BUTTONS   ######################################################################################

btn_zero = Button(width=19, text='0', font='times 15 bold', bd=5, command=lambda x=0: enterNumber(0))
btn_zero.place(x=25, y=280)

btn_clear = Button(width=4, text='C', font='times 15 bold', bd=5, command=funcClear)
btn_clear.place(x=25, y=340)

btn_dot = Button(width=4, text='.', font='times 15 bold', bd=5, command=lambda x='.': enterNumber(x))
btn_dot.place(x=110, y=340)

btn_equal = Button(width=4, text='=', font='times 15 bold', bd=5, command=funcOperator)
btn_equal.place(x=200, y=340)

btn_equal = Button(width=4, text='=', font='times 15 bold', bd=5, command=funcOperator)
btn_equal.place(x=200, y=340)

icon = PhotoImage(file='arrow.png')
btn_delete = Button(width=50, height=35, bd=5, command=funcDelete, image=icon)
btn_delete.place(x=290, y=340)

status_bar = Label(text='History : ', relief=SUNKEN, height=3, anchor=W, font='verdana 11 bold')
status_bar.pack(side=BOTTOM, fill=X)

                  
root.mainloop()
