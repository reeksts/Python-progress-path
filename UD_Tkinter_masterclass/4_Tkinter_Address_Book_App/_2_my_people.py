from tkinter import *
import sqlite3
import _3_add_people
from tkinter import messagebox

con = sqlite3.connect('database.db')
cur = con.cursor()


class MyPeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x650+620+200')
        self.title('My People')
        self.resizable(False, False)

        ##### Frames ###################################################################################################
        self.top_frame = Frame(self, height=150, bg='white')
        self.top_frame.pack(fill=X)
        self.bottom_frame = Frame(self, height=500, bg='#fcc324')
        self.bottom_frame.pack(fill=X)

        ###### Heading and image #######################################################################################
        self.top_image = PhotoImage(file='icons/person_icon.png')
        self.top_image_lbl = Label(self.top_frame, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)

        self.heading = Label(self.top_frame, text='My Persons', font='arial 15 bold',
                             fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)

        ##### Scrollbar ################################################################################################
        self.sb = Scrollbar(self.bottom_frame, orient=VERTICAL)

        ##### Listbox ##################################################################################################
        self.listbox = Listbox(self.bottom_frame, width=60, height=31)
        self.listbox.grid(row=0, column=0, padx=(40, 0))
        self.sb.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=1, sticky=N+S)

        persons = cur.execute('SELECT * FROM persons').fetchall()
                #count=0
                #for person in persons:
                #    self.listbox.insert(count, str(person[0]) + '-' + person[1] + ' ' + person[2])
                #    count += 1
        for i in range(len(persons)):
            self.listbox.insert(i, str(persons[i][0]) + '-' + persons[i][1] + ' ' + persons[i][2])

        ##### Buttons ##################################################################################################
        self.button1 = Button(self.bottom_frame, text='Add', width=12, font='Sans 12 bold',
                              command=self.func_add_people)
        self.button1.grid(row=0, column=2, sticky=N, padx=10, pady=10)

        self.button2 = Button(self.bottom_frame, text='Update', width=12, font='Sans 12 bold',
                              comman=self.func_update_people)
        self.button2.grid(row=0, column=2, sticky=N, padx=10, pady=50)

        self.button3 = Button(self.bottom_frame, text='Display', width=12, font='Sans 12 bold',
                              command=self.func_display_person)
        self.button3.grid(row=0, column=2, sticky=N, padx=10, pady=90)

        self.button4 = Button(self.bottom_frame, text='Delete', width=12, font='Sans 12 bold',
                              command=self.func_delete_person)
        self.button4.grid(row=0, column=2, sticky=N, padx=10, pady=130)

    def func_add_people(self):
        add = _3_add_people.AddPeople()
        self.destroy()

    def func_update_people(self):
        global person_id
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split('-')[0]
        update_page = Update()
        self.destroy()

    def func_display_person(self):
        global person_id
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split('-')[0]
        display_window = Display()
        self.destroy()

    def func_delete_person(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split('-')[0]

        mbox = messagebox.askquestion('Warning', 'Are you sure to delete this person', icon='warning')

        if mbox == 'yes':
            try:
                cur.execute('DELETE FROM persons WHERE person_id=?', (person_id,))
                con.commit()
                messagebox.showinfo('Success', 'Person has been deleted')
                self.destroy()
            except:
                messagebox.showinfo('Info', 'Person has not been deleted')

class Update(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x750+620+200')
        self.title('Update Person')
        self.resizable(False, False)

        #get person from database
        global person_id

        person = cur.execute('SELECT * FROM persons WHERE person_id =?', (person_id,))
        person_info = person.fetchall()
        self.person_id = person_info[0][0]
        self.person_name = person_info[0][1]
        self.person_surname = person_info[0][2]
        self.person_email = person_info[0][3]
        self.person_phone = person_info[0][4]
        self.person_address = person_info[0][5]

        # Frames
        self.top_frame = Frame(self, height=150, bg='white')
        self.top_frame.pack(fill=X)
        self.bottom_frame = Frame(self, height=600, bg='#fcc324')
        self.bottom_frame.pack(fill=X)

        # Heading and image
        self.top_image = PhotoImage(file='icons/addperson.png')
        self.top_image_lbl = Label(self.top_frame, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)

        self.heading = Label(self.top_frame, text='Update Person', font='arial 15 bold',
                             fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)

        # Labels and entries
        # name
        self.label1 = Label(self.bottom_frame, text='Name', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label1.place(x=40, y=40)
        self.entry1 = Entry(self.bottom_frame, width=30, bd=4)
        self.entry1.insert(0, self.person_name)
        self.entry1.place(x=150, y=45)

        # surname
        self.label2 = Label(self.bottom_frame, text='Surname', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label2.place(x=40, y=80)
        self.entry2 = Entry(self.bottom_frame, width=30, bd=4)
        self.entry2.insert(0, self.person_surname)
        self.entry2.place(x=150, y=85)

        # email
        self.label3 = Label(self.bottom_frame, text='E-mail', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label3.place(x=40, y=120)
        self.entry3 = Entry(self.bottom_frame, width=30, bd=4)
        self.entry3.insert(0, self.person_email)
        self.entry3.place(x=150, y=125)

        # phone number
        self.label4 = Label(self.bottom_frame, text='Phone', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label4.place(x=40, y=160)
        self.entry4 = Entry(self.bottom_frame, width=30, bd=4)
        self.entry4.insert(0, self.person_phone)
        self.entry4.place(x=150, y=165)

        # address
        self.label5 = Label(self.bottom_frame, text='Address', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label5.place(x=40, y=300)
        self.entry5 = Text(self.bottom_frame, width=23, height=15, wrap=WORD)
        self.entry5.insert('1.0', self.person_address)
        self.entry5.place(x=150, y=200)

        # button
        self.button1 = Button(self.bottom_frame, text='Update Person',
                              command=self.update_person)
        self.button1.place(x=270, y=460)

    def update_person(self):
        person_id = self.person_id
        name = self.entry1.get()
        surname = self.entry2.get()
        email = self.entry3.get()
        phone = self.entry4.get()
        address = self.entry5.get(1.0, 'end-1c')

        try:
            query = "UPDATE 'persons' set person_name=?, person_surname =?, person_email=?, person_phone=?, person_address=? WHERE person_id=?"
            cur.execute(query,(name, surname, email, phone, address, person_id))
            con.commit()
            messagebox.showinfo('Success', 'Person has been updated')
            self.destroy()
        except:
            messagebox.showinfo('Warnign', 'Person has not been updated', icon='warning')

class Display(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x750+620+200')
        self.title('Display Person')
        self.resizable(False, False)

        # get person from database
        global person_id

        person = cur.execute('SELECT * FROM persons WHERE person_id =?', (person_id,))
        person_info = person.fetchall()
        self.person_id = person_info[0][0]
        self.person_name = person_info[0][1]
        self.person_surname = person_info[0][2]
        self.person_email = person_info[0][3]
        self.person_phone = person_info[0][4]
        self.person_address = person_info[0][5]

        # Frames
        self.top_frame = Frame(self, height=150, bg='white')
        self.top_frame.pack(fill=X)
        self.bottom_frame = Frame(self, height=600, bg='#fcc324')
        self.bottom_frame.pack(fill=X)

        # Heading and image
        self.top_image = PhotoImage(file='icons/addperson.png')
        self.top_image_lbl = Label(self.top_frame, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)

        self.heading = Label(self.top_frame, text='Add Person', font='arial 15 bold',
                             fg='#003f8a', bg='white')
        self.heading.place(x=260, y=60)

        # Labels and entries
        # name
        self.label1 = Label(self.bottom_frame, text='Name', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label1.place(x=40, y=40)
        self.entry1 = Entry(self.bottom_frame, width=30, bd=4)
        self.entry1.insert(0, self.person_name)
        self.entry1.config(state='disabled')
        self.entry1.place(x=150, y=45)

        # surname
        self.label2 = Label(self.bottom_frame, text='Surname', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label2.place(x=40, y=80)
        self.entry2 = Entry(self.bottom_frame, width=30, bd=4)
        self.entry2.insert(0, self.person_surname)
        self.entry2.config(state='disabled')
        self.entry2.place(x=150, y=85)

        # email
        self.label3 = Label(self.bottom_frame, text='E-mail', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label3.place(x=40, y=120)
        self.entry3 = Entry(self.bottom_frame, width=30, bd=4)
        self.entry3.insert(0, self.person_email)
        self.entry3.config(state='disabled')
        self.entry3.place(x=150, y=125)

        # phone number
        self.label4 = Label(self.bottom_frame, text='Phone', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label4.place(x=40, y=160)
        self.entry4 = Entry(self.bottom_frame, width=30, bd=4)
        self.entry4.insert(0, self.person_phone)
        self.entry4.config(state='disabled')
        self.entry4.place(x=150, y=165)

        # address
        self.label5 = Label(self.bottom_frame, text='Address', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label5.place(x=40, y=300)
        self.entry5 = Text(self.bottom_frame, width=23, height=15, wrap=WORD)
        self.entry5.insert(1.0, self.person_address)
        self.entry5.config(state='disabled')
        self.entry5.place(x=150, y=200)
