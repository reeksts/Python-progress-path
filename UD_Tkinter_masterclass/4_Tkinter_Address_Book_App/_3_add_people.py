from tkinter import *
import sqlite3
from tkinter import messagebox

con = sqlite3.connect('database.db')
cur = con.cursor()


class AddPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x750+550+200')
        self.title('Add People')
        self.resizable(False, False)

        ##### Frames ###################################################################################################
        self.top_frame = Frame(self, height=150, bg='white')
        self.top_frame.pack(fill=X)
        self.bottom_frame = Frame(self, height=600, bg='#fcc324')
        self.bottom_frame.pack(fill=X)

        ##### Heading and image ########################################################################################
        self.top_image = PhotoImage(file='icons/addperson.png')
        self.top_image_lbl = Label(self.top_frame, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)

        self.heading = Label(self.top_frame, text='Add Person', font='arial 15 bold',
                             fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)


        ##### Labels and entries #######################################################################################
        # name
        self.label1 = Label(self.bottom_frame, text='Name', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label1.place(x=40, y=40)
        self.entry1 = Entry(self.bottom_frame, width=30, bd=4)
        self.entry1.insert(0, 'Please enter a Name')
        self.entry1.place(x=150, y=45)

        # surname
        self.label2 = Label(self.bottom_frame, text='Surname', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label2.place(x=40, y=80)
        self.entry2 = Entry(self.bottom_frame, width=30, bd=4)
        self.entry2.insert(0, 'Please enter a Surname')
        self.entry2.place(x=150, y=85)

        # email
        self.label3 = Label(self.bottom_frame, text='E-mail', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label3.place(x=40, y=120)
        self.entry3 = Entry(self.bottom_frame, width=30, bd=4)
        self.entry3.insert(0, 'Please enter a E-mail')
        self.entry3.place(x=150, y=125)

        # phone number
        self.label4 = Label(self.bottom_frame, text='Phone', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label4.place(x=40, y=160)
        self.entry4 = Entry(self.bottom_frame, width=30, bd=4)
        self.entry4.insert(0, 'Please enter a Phone Number')
        self.entry4.place(x=150, y=165)

        # address
        self.label5 = Label(self.bottom_frame, text='Address', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label5.place(x=40, y=300)
        self.entry5 = Text(self.bottom_frame, width=23, height=15, wrap=WORD)
        self.entry5.place(x=150, y=200)

        # button
        self.button1 = Button(self.bottom_frame, text='Add Person',
                              command=self.add_person)
        self.button1.place(x=270, y=460)



    def add_person(self):
            name = self.entry1.get()
            surname = self.entry2.get()
            email = self.entry3.get()
            phone = self.entry4.get()
            address = self.entry5.get(1.0, 'end-1c')

            if(name and surname and email and phone and address !=''):
                try:
                    query = "INSERT INTO 'persons' (person_name, person_surname, person_email," \
                            "person_phone, person_address) VALUES(?, ?, ?, ?, ?)"
                    cur.execute(query, (name, surname, email, phone, address))
                    con.commit()
                    messagebox.showinfo('Success', 'Successfully added to database!', icon='info')

                except:
                    messagebox.showerror('Error', 'Cannot add to database', icon='warning')
            else:
                messagebox.showerror('Error', 'Fields cannot be empty', icon='warning')

