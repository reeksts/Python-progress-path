from tkinter import *
from tkinter import ttk
import sqlite3
import _2_add_book
import _3_add_member
import _4_give_Book
from tkinter import messagebox

con = sqlite3.connect('library.db')
cur = con.cursor()


class Main(object):
    def __init__(self, master):
        self.master = master

        def display_books(self):
            books = cur.execute("SELECT * FROM books").fetchall()

            self.list_books.delete(0, END)
            count = 0
            for book in books:
                self.list_books.insert(count, str(book[0]) + '-' + book[1])
                count += 1

            def book_info(event):
                value = str(self.list_books.get(self.list_books.curselection()))
                id = value.split('-')[0]
                book = cur.execute('SELECT * FROM books WHERE book_id=?', (id,))
                book_info = book.fetchall()
                self.list_details.delete(0, END)
                self.list_details.insert(0, 'Book name : ' + book_info[0][1])
                self.list_details.insert(1, 'Author : ' + book_info[0][2])
                self.list_details.insert(2, 'Page : ' + book_info[0][3])
                self.list_details.insert(3, 'Languegae : ' + book_info[0][4])
                if book_info[0][5] == 0:
                    self.list_details.insert(4, 'Status : Available')
                else:
                    self.list_details.insert(4, 'Status : Not Available')

            def double_click(event):
                global given_id
                value = str(self.list_books.get(self.list_books.curselection()))
                given_id = value.split('-')[0]
                give_book = GiveBook()


            self.list_books.bind('<<ListboxSelect>>', book_info)
            self.tabs.bind('<<NotebookTabChanged>>', display_statistics)
            #self.tabs.bind('<ButtonRelease-1>', display_books)
            self.list_books.bind('<Double-Button-1>', double_click)

        def display_statistics(event):
            count_books = cur.execute("SELECT count(book_id) FROM books").fetchall()
            count_members = cur.execute("SELECT count(member_id) FROM members").fetchall()
            taken_books = cur.execute("SELECT count(book_status) FROM books WHERE book_status=1").fetchall()
            self.label_book_count.config(text='Total books in library: ' + str(count_books[0][0]))
            self.label_member_count.config(text='Total member: ' + str(count_members[0][0]))
            self.label_taken_count.config(text='Taken books: ' + str(taken_books[0][0]))
            display_books(self)

        ############### Frames And Buttons ###############
        # main frame
        self.main_frame = Frame(self.master)
        self.main_frame.pack()

        # top frame
        self.top_frame = Frame(self.main_frame, width=1350, height=70, bg='#f8f8f8',
                               relief=SUNKEN, borderwidth=2)
        self.top_frame.pack(fill=X)

        # center frame
        self.center_frame = Frame(self.main_frame, width=100, height=680)
        self.center_frame.pack()

        # center left frame
        self.center_left_frame = Frame(self.center_frame, width=900, height=680, bg='#e0f0f0',
                                  relief=SUNKEN, borderwidth=2)
        self.center_left_frame.pack(side=LEFT)

        # center right frame
        self.center_right_frame = Frame(self.center_frame, width=450, height=680, bg='#e0f0f0',
                                       relief=SUNKEN, borderwidth=2)
        self.center_right_frame.pack()

        #serach bar
        self.search_bar = LabelFrame(self.center_right_frame, width=450, height=10, text='Search Box',
                                    bg='#9bc9ff')
        self.search_bar.pack(fill=X)
        self.label_search = Label(self.search_bar, text='Search :', font='arial 14 bold', bg='#9bc9ff', fg='white')
        self.label_search.grid(row=0, column=0, padx=20, pady=20)
        self.search_entry = Entry(self.search_bar, width=30, bd=5)
        self.search_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        self.button_search = Button(self.search_bar, text='Search', font='arial 12', bg='#fcc324', fg='white',
                                    command=self.search_books)
        self.button_search.grid(row=0, column=4, padx=20, pady=10)

        # listbar
        self.list_bar = LabelFrame(self.center_right_frame, width=450, height=400, text='List Box',
                                   bg='#fcc324')
        self.list_bar.pack(fill=BOTH)
        self.label_list = Label(self.list_bar, text='Sort By', font='arial 16 bold', bg='#fcc324', fg='#2488ff')
        self.label_list.grid(row=0, column=2)
        self.list_choice = IntVar()
        self.radiob1 = Radiobutton(self.list_bar, text='All Books', var=self.list_choice, val=1, bg='#fcc324')
        self.radiob1.grid(row=1, column=0)
        self.radiob2 = Radiobutton(self.list_bar, text='In Library', var=self.list_choice, val=2, bg='#fcc324')
        self.radiob2.grid(row=1, column=1)
        self.radiob3 = Radiobutton(self.list_bar, text='Borrowed books', var=self.list_choice, val=3, bg='#fcc324')
        self.radiob3.grid(row=1, column=2)
        self.button_list = Button(self.list_bar, text='List Books', bg='#2488ff', fg='white', font='arial 12',
                                  command=self.list_books)
        self.button_list.grid(row=1, column=3, padx=40, pady=10)

        # title and image
        self.image_bar = Frame(self.center_right_frame, width=440, height=350)
        self.image_bar.pack(fill=BOTH)
        self.title_right = Label(self.image_bar, text='Welcome to our Library', font='arial 16 bold')
        self.title_right.grid(row=0)
        self.image_library = PhotoImage(file='icons/library.png')
        self.image = Label(self.image_bar, image=self.image_library)
        self.image.grid(row=1)

        ############### Tool bar ###############
        # add book button
        self.iconbook = PhotoImage(file='icons/add_book.png')
        self.button_book = Button(self.top_frame, text='Add Book', image=self.iconbook, compound=LEFT,
                                  font='arial 12 bold', bg='#A2D69C', bd=3, command=self.add_book)
        self.button_book.pack(side=LEFT, padx=10)

        # add member button
        self.iconmember = PhotoImage(file='icons/users.png')
        self.button_members = Button(self.top_frame, text='Add Member', image=self.iconmember, compound=LEFT,
                                     font='arial 12 bold', bg='#A2D69C', bd=3, command=self.add_member)
        self.button_members.pack(side=LEFT, padx=(0,10))

        # add give button
        self.icongive = PhotoImage(file='icons/givebook.png')
        self.button_give = Button(self.top_frame, text='Give Book', image=self.icongive, compound=LEFT,
                                  font='arial 12 bold', bg='#A2D69C', bd=3, command=self.give_Book)
        self.button_give.pack(side=LEFT, padx=(0, 10))

        ############### Tab1 ###############

        self.tabs = ttk.Notebook(self.center_left_frame, width=900, height=680)
        self.tabs.pack()
        self.tab1_icon = PhotoImage(file='icons/books.png')
        self.tab2_icon = PhotoImage(file='icons/members.png')
        self.tab1 = ttk.Frame(self.tabs)
        self.tab2 = ttk.Frame(self.tabs)
        self.tabs.add(self.tab1, text='Library Management', image=self.tab1_icon, compound=LEFT)
        self.tabs.add(self.tab2, text='Statistics', image=self.tab2_icon, compound=LEFT)


        # list books
        self.list_books = Listbox(self.tab1, width=40, height=30, bd=5, font='arial 12 bold')
        self.list_books.grid(row=0, column=0, padx=(10, 0), pady=10, sticky=N)
        self.sb = Scrollbar(self.tab1, orient=VERTICAL, command=self.list_books.yview)
        self.list_books.config(yscrollcommand=self.sb.set)
        self.sb.grid(row=0, column=0, sticky=N+S+E)

        # list details
        self.list_details = Listbox(self.tab1, width=80, height=30, bd=5, font='arial 12 bold')
        self.list_details.grid(row=0, column=1, padx=(10,0), pady=10, sticky=N)

        ############### Tab2 ###############

        #statistics
        self.label_book_count = Label(self.tab2, text='dfdfd', pady=20, font='arial 14 bold')
        self.label_book_count.grid(row=0)
        self.label_member_count = Label(self.tab2, text='dfdf', pady=20, font='arial 14 bold')
        self.label_member_count.grid(row=1, sticky=W)
        self.label_taken_count = Label(self.tab2, text='ddffdd', pady=20, font='arial 14 bold')
        self.label_taken_count.grid(row=2, sticky=W)

        # functions
        display_books(self)
        display_statistics(self)


    def add_book(self):
        add = _2_add_book.AddBook()

    def add_member(self):
        member = _3_add_member.AddMember()

    def search_books(self):
        value = self.search_entry.get()
        search = cur.execute("SELECT * FROM books WHERE book_name LIKE ?", ('%'+value+'%', )).fetchall()
        self.list_books.delete(0, END)
        count = 0
        for book in search:
            self.list_books.insert(count, str(book[0]) + '-' + book[1])
            count += 1

    def list_books(self):
        value = self.list_choice.get()
        if value == 1:
            all_books = cur.execute("SELECT * FROM books").fetchall()
            self.list_books.delete(0, END)
            self.list_details.delete(0, END)
            count = 0
            for book in all_books:
                self.list_books.insert(count, str(book[0]) + '-' + book[1])
                count += 1
        elif value == 2:
            books_in_library = cur.execute("SELECT * FROM books WHERE book_status =?", (0,)).fetchall()
            self.list_books.delete(0, END)
            self.list_details.delete(0, END)
            count = 0
            for book in books_in_library:
                self.list_books.insert(count, str(book[0]) + '-' + book[1])
                count += 1
        else:
            taken_books = cur.execute("SELECT * from books WHERE book_status =?", (1,)).fetchall()
            self.list_books.delete(0, END)
            self.list_details.delete(0, END)
            count = 0
            for book in taken_books:
                self.list_books.insert(count, str(book[0]) + '-' + book[1])
                count += 1

    def give_Book(self):
        give_book = _4_give_Book.GiveBook()


class GiveBook(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry('650x750+550+200')
        self.title('Lend Book')
        self.resizable(False, False)
        global given_id
        self.book_id = int(given_id)
        query = "SELECT * FROM books"
        books = cur.execute(query).fetchall()
        book_list = []
        for book in books:
            book_list.append(str(book[0]) + '-' + book[1])
        print(book_list)

        query2 = "SELECT * FROM members"
        members = cur.execute(query2).fetchall()
        member_list = []
        for member in members:
            member_list.append(str(member[0]) + '-' + member[1])

        ############### Frames ###############
        # top frame
        self.top_frame = Frame(self, height=150, bg='white')
        self.top_frame.pack(fill=X)

        # bottom frame
        self.bottom_frame = Frame(self, height=600, bg='#fcc324')
        self.bottom_frame.pack(fill=X)

        # heading, image
        self.top_image = PhotoImage(file='icons/addperson.png')
        self.top_image_label = Label(self.top_frame, image=self.top_image, bg='white')
        self.top_image_label.place(x=120, y=10)
        self.heading = Label(self.top_frame, text='   Add Person   ', font='arial 22 bold', fg='#003f8a', bg='white')
        self.heading.place(x=290, y=60)

        ############### ENTRIES AND LABELS ###############

        # book name
        self.book_name = StringVar()
        self.label_name = Label(self.bottom_frame, text='Book :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_name.place(x=40, y=40)
        self.combo_name = ttk.Combobox(self.bottom_frame, textvariable=self.book_name)
        self.combo_name['values'] = book_list
        self.combo_name.current(self.book_id-1)
        self.combo_name.place(x=150, y=45)

        # member name
        self.member_name = StringVar()
        self.label_phone = Label(self.bottom_frame, text='Member :', font='arial 15 bold', fg='white', bg='#fcc324')
        self.label_phone.place(x=40, y=80)
        self.combo_member = ttk.Combobox(self.bottom_frame, textvariable=self.member_name)
        self.combo_member['values'] = member_list
        self.combo_member.place(x=150, y=85)

        # button
        self.button = Button(self.bottom_frame, text='Lend book', command=self.lend_book)
        self.button.place(x=225, y=120)

    def lend_book(self):
        book_name = self.book_name.get()
        member_name = self.member_name.get()

        if (book_name and member_name !=''):
            try:
                query = "INSERT INTO 'borrows' (bbook_id, bmember_id) VALUES(?,?)"
                cur.execute(query, (book_name, member_name))
                con.commit()
                messagebox.showinfo('Success', 'Fully Added to Database', icon='info')
                cur.execute("UPDATE books SET book_status =? WHERE book_id =?", (1, self.book_id))
                con.commit()
            except:
                messagebox.showerror('Error', 'Cannot add to database')
        else:
            messagebox.showerror('Error', 'Fields cannot be empty', icon='warning')

def main():
    root = Tk()
    app = Main(root)
    root.title('Library Management System')
    root.geometry('1350x750+350+200')
    root.iconbitmap('icons/icon.ico')
    root.mainloop()


if __name__ == '__main__':
    main()
