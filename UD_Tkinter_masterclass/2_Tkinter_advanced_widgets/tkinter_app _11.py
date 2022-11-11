from tkinter import *
from tkinter import ttk
from ttkthemes import themed_tk as tk

root = tk.ThemedTk()
root.get_themes()
root.set_theme('aquativo')
root.geometry('600x600+350+350')

# themes can be aplied only when using ttk module

text_name = ttk.Label(root, text='Name :').grid(row=0, column=0, pady=20)
text_surname = ttk.Label(root, text = 'Surname :').grid(row=1, column=0, pady=20)
text_msg = ttk.Label(root, text = 'Message :').grid(row=3, column=1)

name_input = ttk.Entry(root, width=30)
name_input.grid(row=0, column=1)
name_input.insert(0, 'Please enter your name')
surname_input = ttk.Entry(root, width=30)
surname_input.grid(row=1, column=1)
surname_input.insert(0, 'Please Enter Your name')

radiobutton1 = ttk.Radiobutton(root, text='male', value='male')
radiobutton1.grid(row=2, column=1, sticky=E, pady=15)
radiobutton2 = ttk.Radiobutton(root, text='female', value='female')
radiobutton2.grid(row=2, column=1)

msg_text = Text(root, width=25, height=10, wrap=WORD)
msg_text.grid(row=4, column=1)

button1 = ttk.Button(root, text='Send')
button1.grid(row=5, column=1, sticky=W)
button2 = ttk.Button(root, text='Clear')
button2.grid(row=5, column=1, sticky=E)
                     
root.mainloop()
