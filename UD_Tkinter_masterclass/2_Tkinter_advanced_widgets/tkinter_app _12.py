from tkinter import *
from tkinter import filedialog, colorchooser


root = Tk()
root.geometry('600x600+350+350')

text_editor = Text(root, width=25, height=15, wrap=WORD)
text_editor.pack()

def open_file():
    file_name = filedialog.askopenfilename(initialdir='/', title='Select a file',
                                           filetypes = (('Txt Files', '.txt'),('All file','*.*')))
    content = open(file_name).read()
    text_editor.insert(END, content)

def save_file():
    my_file = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    if my_file is None:
        return
    content = text_editor.get(1.0, 'end-1c')
    my_file.write(content)

def change_color():
    color = colorchooser.askcolor()
    print(color)
    text_editor.configure(fg=color[1])

button1 = Button(root, text='Open', command=open_file)
button1.pack(side=LEFT, padx=(170, 20))

button2 = Button(root, text='Save', command=save_file)
button2.pack(side=LEFT)

button3 = Button(root, text='Color', command=change_color)
button3.pack(side=LEFT)
                     
root.mainloop()
