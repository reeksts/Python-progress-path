from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('library.db')
cur = con.cursor()


class AddMember(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x750+550+200')
        self.title('Add Member')
        self.resizable(False, False)

        ############### Frames ###############
        # top frame
        self.top_frame = Frame(self, height=150, bg='white')
        self.top_frame.pack(fill=X)

        # bottom frame
        self.bottom_frame = Frame(self, height=600, bg='#fcc324')
        self.bottom_frame.pack(fill=X)

        # heading, image
        self.top_image = PhotoImage(file = 'icons/addperson.png')
        self.top_image_label = Label(self.top_frame, image=self.top_image, bg='white')
        self.top_image_label.place(x=120, y=10)
        self.heading = Label(self.top_frame, text='   Add Person   ', font='arial 22 bold', fg='#003f8a', bg='white')
        self.heading.place(x=290, y=60)

        ############### ENTRIES AND LABELS ###############

        # member name
        self.label_name = Label(self.bottom_frame, text='Name :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_name.place(x=40, y=40)
        self.entry_name = Entry(self.bottom_frame, width=30, bd=4)
        self.entry_name.insert(0, 'Please enter name')
        self.entry_name.place(x=150, y=45)

        # phone
        self.label_phone = Label(self.bottom_frame, text='Phone :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_phone.place(x=40, y=80)
        self.entry_phone = Entry(self.bottom_frame, width=30, bd=4)
        self.entry_phone.insert(0, 'Please enter phone number')
        self.entry_phone.place(x=150, y=85)

        # button
        self.button = Button(self.bottom_frame, text='Add Member', command=self.add_member)
        self.button.place(x=270, y=120)

    def add_member(self):
        name = self.entry_name.get()
        phone = self.entry_phone.get()
        if (name and phone !=''):
            try:
                query = "INSERT INTO 'members' (member_name, member_phone) VALUES(?, ?)"
                cur.execute(query, (name, phone))
                con.commit()
                messagebox.showinfo('Success', 'Successfully added to database', icon='info')
            except:
                messagebox.showerror('Error', 'Cannot add to database', icon='warning')
        else:
            messagebox.showerror('Error', 'Fields cannot be empty', icon='warning')

