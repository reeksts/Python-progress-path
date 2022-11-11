from tkinter import *

root = Tk()
root.title('Using Images')
root.geometry('600x600+350+350')

lbl_text = Label(root, text = 'using Images', font = (('Times'),18))
lbl_text.pack()

logo = PhotoImage(file = 'icon.png')
lbl_image = Label(root, image=logo)
lbl_image.pack()


                     
root.mainloop()
