from tkinter import *
import datetime
import _2_my_people
import _3_add_people
import _4_about_us

date = datetime.datetime.now().date()

class Application:
    def __init__(self, master):
        self.master = master

        # Frames
        self.top = Frame(self.master, height=150, bg='white')
        self.top.pack(fill=X)
        self.bottom = Frame(self.master, height=500, bg='#adff2f')
        self.bottom.pack(fill=X)

        # Heading, image and date
        self.top_image = PhotoImage(file='icons/book.png')
        self.top_image_lbl = Label(self.top, image=self.top_image, bg='white')
        self.top_image_lbl.place(x=120, y=10)

        self.heading = Label(self.top, text='My Address Book APP', font='arial 15 bold',
                             fg='#ffa500', bg='white')
        self.heading.place(x=260, y=60)

        self.date_lbl = Label(self.top, text="Today's date " + str(date), font='arial 12 bold',
                              fg='#ffa500', bg='white')
        self.date_lbl.place(x=450, y=5)

        # First button (My People)
        self.btn1_icon = PhotoImage(file='icons/man.png')
        self.btn1 = Button(self.bottom, width=140, height=35, text='   My People   ', font='arial 12 bold',
                           command=self.open_my_people)
        self.btn1.config(image=self.btn1_icon, compound=LEFT)
        self.btn1.place(x=250, y=10)

        # Second button (Add People)
        self.btn2_icon = PhotoImage(file='icons/add.png')
        self.btn2 = Button(self.bottom, width=140, height=35, text='   Add People ', font='arial 12 bold',
                           command=self.func_add_people)
        self.btn2.config(image=self.btn2_icon, compound=LEFT)
        self.btn2.place(x=250, y=70)

        # Third button (About Us)
        self.btn3_icon = PhotoImage(file='icons/info.png')
        self.btn3 = Button(self.bottom, width=140, height=35, text='     About Us    ', font='arial 12 bold',
                           command=_4_about_us.main)
        self.btn3.config(image=self.btn3_icon, compound=LEFT)
        self.btn3.place(x=250, y=130)

    def open_my_people(self):
        _2_my_people.MyPeople()

    def func_add_people(self):
        _3_add_people.AddPeople()


def main():
    root = Tk()
    app = Application(root)
    root.title('Address Book App')
    root.geometry('650x550+350+250')
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()
