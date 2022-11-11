from tkinter import *
from tkinter import messagebox
import sqlite3

con = sqlite3.connect('library.db')
cur = con.cursor()


class AddBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x750+550+200')
        self.title('Add Book')
        self.resizable(False, False)

        ############### Frames ###############
        # top frame
        self.top_frame = Frame(self, height=150, bg='white')
        self.top_frame.pack(fill=X)

        # bottom frame
        self.bottom_frame = Frame(self, height=600, bg='#fcc324')
        self.bottom_frame.pack(fill=X)

        # heading, image
        self.top_image = PhotoImage(file = 'icons/addbook.png')
        self.top_image_label = Label(self.top_frame, image=self.top_image, bg='white')
        self.top_image_label.place(x=120, y=10)
        self.heading = Label(self.top_frame, text='   Add Book   ', font='arial 22 bold', fg='#003f8a', bg='white')
        self.heading.place(x=290, y=60)

        ############### ENTRIES AND LABELS ###############

        # name
        self.label_name = Label(self.bottom_frame, text='Name :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_name.place(x=40, y=40)
        self.entry_name = Entry(self.bottom_frame, width=30, bd=4)
        self.entry_name.insert(0, 'Please enter book name')
        self.entry_name.place(x=150, y=45)

        # author
        self.label_author = Label(self.bottom_frame, text='Author :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_author.place(x=40, y=80)
        self.entry_author = Entry(self.bottom_frame, width=30, bd=4)
        self.entry_author.insert(0, 'Please enter author name')
        self.entry_author.place(x=150, y=85)

        # page
        self.label_page = Label(self.bottom_frame, text='Page :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_page.place(x=40, y=120)
        self.entry_page = Entry(self.bottom_frame, width=30, bd=4)
        self.entry_page.insert(0, 'Please enter page size')
        self.entry_page.place(x=150, y=125)

        # language
        self.label_language = Label(self.bottom_frame, text='Languegae :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_language.place(x=40, y=160)
        self.entry_language = Entry(self.bottom_frame, width=30, bd=4)
        self.entry_language.insert(0, 'Please enter language')
        self.entry_language.place(x=150, y=165)

        # button
        self.button = Button(self.bottom_frame, text='Add Book', command=self.addbook)
        self.button.place(x=270, y=200)

    def addbook(self):
        name = self.entry_name.get()
        author = self.entry_author.get()
        page = self.entry_page.get()
        language = self.entry_language.get()
        if (name and author and page and language !=''):
            try:
                query = "INSERT INTO 'books' (book_name, book_author, book_page, book_language) VALUES(?, ?, ?, ?)"
                cur.execute(query, (name, author, page, language))
                con.commit()
                messagebox.showinfo('Success', 'Successfully added to database', icon='info')
            except:
                messagebox.showerror('Error', 'Cannot add to database', icon='warning')
        else:
            messagebox.showerror('Error', 'Fields cannot be empty', icon='warning')

