from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('600x600+350+350')

listbox = Listbox(root, width=40, height=50, selectmode=MULTIPLE)
listbox.pack(pady=25)
listbox.insert(0, 'Python')
listbox.insert(1, 'C++')
listbox.insert(2, 'C#')
listbox.insert(3, 'PHP')


def print_me():
    selected_item = listbox.curselection()
    for item in selected_item:
        print(listbox.get(item))

def delete_me():
    selected_item = listbox.curselection()
    for item in selected_item:
        listbox.delete(item)

button1 = Button(root, text = 'Print', command=print_me)
button1.place(x=300, y=300)
button2 = Button(root, text = 'Delete', command=delete_me)
button2.place(x=350, y=300)






                     
root.mainloop()
