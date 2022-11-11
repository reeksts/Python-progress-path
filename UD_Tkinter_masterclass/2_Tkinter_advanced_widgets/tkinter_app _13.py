from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry('600x600+350+350')

treeview = ttk.Treeview(root)
treeview.pack()

icon = PhotoImage(file='icon2.png')

def callback(event):
    item = treeview.identify('item', event.x, event.y)
    print('You clicked on {}'.format(treeview.item(item, 'text')))

treeview.insert('', '0','item1', text='First item', image=icon)
treeview.insert('', '1','item2', text='Second item')
treeview.insert('', '2','item3', text='Third item')
treeview.insert('', '3','item4', text='4th item')
treeview.move('item3', 'item1', 'end')

treeview.bind('<Double-1>', callback)

root.mainloop()
