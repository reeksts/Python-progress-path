from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox


show_status_bar = True
show_toolbar = True
font_family = 'Arial'
font_size = 12
text_changed = False
url = ''


class FindDialog(Toplevel):
    def __init__(self, parent, *args, **kwargs):
        Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.geometry('450x200+200+200')
        self.title('Find')
        self.resizable(False, False)

        self.txt_find = Label(self, text='Find: ')
        self.txt_find.place(x=20,y=20)
        self.txt_replace = Label(self, text='Replace: ')
        self.txt_replace.place(x=20, y=60)

        self.entry_find = Entry(self, width=30)
        self.entry_find.place(x=100, y=20)
        self.entry_replace = Entry(self, width=30)
        self.entry_replace.place(x=100, y=60)

        self.button_find = Button(self, text='Find', command=self.parent.find_words)
        self.button_find.place(x=200, y=90)
        self.button_replace = Button(self, text='Replace', command=self.parent.replace_words)
        self.button_replace.place(x=240, y=90)




class MainMenu(Menu):
    def __init__(self, parent, *args, **kwargs):
        Menu.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        #### File Menu ####
        self.file = Menu(self, tearoff=0)
        self.add_cascade(label='File', menu=self.file)
        self.new_icon = PhotoImage(file='icons/new.png')
        self.file.add_command(label='New', image=self.new_icon, compound=LEFT, accelerator='Ctrl+N',
                              command=self.parent.new_file)
        self.open_icon = PhotoImage(file='icons/open.png')
        self.file.add_command(label='Open', image=self.open_icon, compound=LEFT, accelerator='Ctrl+O',
                              command=self.parent.open_file)
        self.save_icon = PhotoImage(file='icons/save_icon.png')
        self.file.add_command(label='Save', image=self.save_icon, compound=LEFT, accelerator='Ctrl+S',
                              command=self.parent.save_file)
        self.file.add_command(label='Save as', accelerator='Ctrl+Alt+S',
                              command=self.parent.save_as_file)
        self.exit_icon = PhotoImage(file='icons/exit.png')
        self.file.add_command(label='Exit', image=self.exit_icon, compound=LEFT,
                              command=self.parent.exit_func)

        #### Edit Menu ####
        self.edit = Menu(self, tearoff=0)
        self.add_cascade(label='Edit', menu=self.edit)
        self.edit.add_command(label='Copy', accelerator='Ctrl+C',
                              command=lambda: self.parent.texteditor.event_generate('<Control c>'))
        self.edit.add_command(label='Paste', accelerator='Ctrl+V',
                              command=lambda: self.parent.texteditor.event_generate('<Control v>'))
        self.edit.add_command(label='Cut', accelerator='Ctrl+X',
                              command=lambda: self.parent.texteditor.event_generate('<Control x>'))
        self.edit.add_command(label='Clear All', accelerator='Ctrl+Alt+C',
                              command=lambda: self.parent.texteditor.delete(1.0, END))
        self.edit.add_command(label='Find', accelerator='Ctrl+F', command=self.parent.find)

        #### View Menu ####
        global show_status_bar
        global show_toolbar
        self.view = Menu(self, tearoff=0)
        self.add_cascade(label='View', menu=self.view)
        self.view.add_checkbutton(onvalue=True, offvalue=False, label='Toolbar', variable=show_toolbar,
                                  command=self.parent.hide_toolbar)
        self.view.add_checkbutton(onvalue=True, offvalue=False, label='Statusbar', variable=show_status_bar,
                                  command=self.parent.hide_status_bar)


        #### Themes Menu ####
        self.themes = Menu(self, tearoff=0)
        self.add_cascade(label='Themes', menu=self.themes)
        self.color_list = {'Default': '#000000.#FFFFFF',
                           'Tomatoe': '#ffff00.#ff6347',
                           'LimeGreen': '#fffff0.#32cd32',
                           'Magenta': '#fffafa.#ff00ff',
                           'RoyalBlue': '#ffffbb.#4169e1',
                           'MediumBlue': '#d1e7e0.#0000cd',
                           'Dracula': '#ffffff.#000000'}

        self.theme_choice = StringVar()
        for i in sorted(self.color_list):
            self.themes.add_radiobutton(label=i, variable=self.theme_choice,
                                        command=self.change_theme)

        #### About Menu ####
        self.about = Menu(self, tearoff=0)
        self.add_cascade(label='About', command=self.parent.about_message)

    def change_theme(self):
        selected_theme = self.theme_choice.get()
        fg_bg_color = self.color_list.get(selected_theme)
        foreground_color,background_color = fg_bg_color.split('.')
        self.parent.texteditor.config(background=background_color)
        self.parent.texteditor.config(foreground=foreground_color)


class TextEditor(Text):
    def __init__(self, parent, *args, **kwargs):
        Text.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config(wrap='word', relief=FLAT)
        self.pack(expand=YES, fill=BOTH)
        #xscrollbar = Scrollbar(self, orient=HORIZONTAL)
        #xscrollbar.pack(side=BOTTOM, fill=X)
        #xscrollbar.config(command=self.xview)
        #yscrollbar = Scrollbar(self, orient=VERTICAL)
        #yscrollbar.pack(side=RIGHT, fill=Y)
        #xscrollbar.config(command=self.yview)
        scroll_bar = Scrollbar(self, bd=5, relief=SUNKEN)
        self.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self.yview)
        scroll_bar.pack(side=RIGHT, fill=Y)
        self.focus()
        self.configure(font=('arial 12'))
        self.bind('<<Modified>>', self.parent.changed)


class StatusBar(Label):
    def __init__(self, parent, *args, **kwargs):
        Label.__init__(self, parent, *args, **kwargs)
        self.pack(side=BOTTOM)
        self.config(text='Status Bar')


class ToolBar(Label):
    def __init__(self, parent, *args, **kwargs):
        Label.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(side=TOP, fill=X)


        #########################################################################################
        self.cb_font = ttk.Combobox(self)
        self.cb_font_size = ttk.Combobox(self)
        self.cb_font.pack(side=LEFT, padx=(5,10))
        self.cb_font_size.pack(side=LEFT)

        #########################################################################################
        self.bold_icon = PhotoImage(file='icons/bold.png')
        self.button_bold = Button(self, image=self.bold_icon, command=self.parent.change_bold)
        self.button_bold.pack(side=LEFT, padx=5)

        self.italic_icon = PhotoImage(file='icons/italic.png')
        self.button_italic = Button(self, image=self.italic_icon, command=self.parent.change_italic)
        self.button_italic.pack(side=LEFT, padx=5)

        self.underline_icon = PhotoImage(file='icons/under_line.png')
        self.button_underline = Button(self, image=self.underline_icon, command=self.parent.change_underline)
        self.button_underline.pack(side=LEFT, padx=5)

        self.font_color_icon = PhotoImage(file='icons/color.png')
        self.button_font_color = Button(self, image=self.font_color_icon, command=self.parent.change_font_color)
        self.button_font_color.pack(side=LEFT, padx=5)

        self.align_left_icon = PhotoImage(file='icons/alignleft.png')
        self.button_align_left = Button(self, image=self.align_left_icon, command=self.parent.align_left)
        self.button_align_left.pack(side=LEFT, padx=5)

        self.align_center_icon = PhotoImage(file='icons/aligncenter.png')
        self.button_align_center = Button(self, image=self.align_center_icon, command=self.parent.align_center)
        self.button_align_center.pack(side=LEFT, padx=5)

        self.align_right_icon = PhotoImage(file='icons/alignright.png')
        self.button_align_right = Button(self, image=self.align_right_icon, command=self.parent.align_right)
        self.button_align_right.pack(side=LEFT, padx=5)

        #########################################################################################
        fonts = font.families()
        font_list = []
        font_size_list = []

        for i in range(8,80):
            font_size_list.append(i)
        for i in fonts:
            font_list.append(i)

        self.font_var = StringVar()
        self.cb_font.config(value=font_list, textvariable=self.font_var)
        self.cb_font.current(0)

        self.cb_font_size.config(value=font_size_list)
        self.cb_font_size.current(4)

        self.cb_font.bind('<<ComboboxSelected>>', self.parent.get_font)
        self.cb_font_size.bind('<<ComboboxSelected>>', self.parent.get_font_size)


class MainApplication(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.pack(fill=BOTH, expand=True)


        # Creatign Widgets
        self.main_menu = MainMenu(self)
        self.toolbar = ToolBar(self)
        self.texteditor = TextEditor(self)
        self.statusbar = StatusBar(self)


        # Parent menu configuration
        self.parent.config(menu=self.main_menu)

    def about_message(self, *args):
        messagebox.showinfo('About', 'This is our about page\nhave a question\ncontact us karlis@gmail.com')

    def new_file(self, *args):
        global url
        try:
            url=''
            self.texteditor.delete(1.0, END)
        except:
            pass

    def open_file(self, *args):
        global url
        url = filedialog.askopenfilename(initialdir='/', title='Select a file to open',
                                         filetypes=(('Text file', '*.txt'),('All Files', '*.*')))
        try:
            with open(url, 'r') as file:
                self.texteditor.delete('1.0', END)
                self.texteditor.insert('1.0', file.read())
        except:
            return
        self.parent.title('Now Editing - ' + str(url.split('/')[-1]))

    def save_file(self, *args):
        global url
        try:
            if url != '':
                content = str(self.texteditor.get(1.0, END))
                with open(url, 'w', encoding='utf-8') as file:
                    file.write(content)
            else:
                url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                               filetypes=(('Text file','*.txt'),('All files', '*.*')))
                content2 = str(self.texteditor.get(1.0, END))
                url.write(content2)
                url.close()
        except:
            return

    def save_as_file(self, *args):
        global url
        try:
            content = str(self.texteditor.get(1.0, END))
            url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                           filetypes=(('Text file', '*.txt'), ('All files', '*.*')))
            url.write(content)
            url.close()
            self.parent.title('Now Editing - ' + str(url.split('/')[-1]))
        except:
            return

    def exit_func(self, *args):
        global url, text_changed
        try:
            if text_changed == True:
                mbox = messagebox.askyesnocancel('Warning', 'Do you want to save the file?')
                if mbox is True:
                    if url != '':
                        content = self.texteditor.get(1.0, END)
                        with open(url, 'w', encoding='utf-8') as file:
                            file.write(content)
                            self.parent.destroy()
                    else:
                        content2 = str(self.texteditor.get(1.0, END))
                        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                           filetypes=(('Text file', '*.txt'), ('All files', '*.*')))
                        url.write(content2)
                        url.close()
                if mbox is False:
                    self.parent.destroy()
            else:
                self.parent.destroy()
        except:
            return


    def changed(self, *args):
        global text_changed
        flag = self.texteditor.edit_modified()
        text_changed = True
        print(flag)
        if flag:
            words = len(self.texteditor.get(1.0, 'end-1c').split())
            letters = len(self.texteditor.get(1.0, 'end-1c'))
            self.statusbar.config(text='Characters' + str(letters) + 'Words: ' + str(words))
        self.texteditor.edit_modified(False)

    def get_font(self, *args):
        global font_family
        font_family = self.toolbar.cb_font.get()
        self.texteditor.config(font=(font_family, font_size))

    def get_font_size(self, *args):
        global font_size
        font_size = self.toolbar.cb_font_size.get()
        self.texteditor.config(font=(font_family, font_size))

    def change_bold(self, *args):
        text_prop = font.Font(font=self.texteditor['font'])
        if text_prop.actual('weight') == 'normal':
            self.texteditor.config(font=(font_family, font_size, 'bold'))
        elif text_prop.actual('weight') == 'bold':
            self.texteditor.config(font=(font_family, font_size, 'normal'))

    def change_italic(self, *args):
        text_prop = font.Font(font=self.texteditor['font'])
        if text_prop.actual('slant') == 'roman':
            self.texteditor.config(font=(font_family, font_size, 'italic'))
        elif text_prop.actual('slant') == 'italic':
            self.texteditor.config(font=(font_family, font_size, 'roman'))

    def change_underline(self, *args):
        text_prop = font.Font(font=self.texteditor['font'])
        if text_prop.actual('underline') == 0:
            self.texteditor.config(font=(font_family, font_size, 'underline'))
        elif text_prop.actual('underline') == 1:
            self.texteditor.config(font=(font_family, font_size, 'normal'))

    def change_font_color(self, *args):
        color = colorchooser.askcolor()
        self.texteditor.config(fg=color[1])

    def align_left(self, *args):
        content = self.texteditor.get(1.0, END)
        self.texteditor.tag_config('left', justify=LEFT)
        self.texteditor.delete(1.0, END)
        self.texteditor.insert(INSERT, content, 'left')

    def align_center(self, *args):
        content = self.texteditor.get(1.0, END)
        self.texteditor.tag_config('center', justify=CENTER)
        self.texteditor.delete(1.0, END)
        self.texteditor.insert(INSERT, content, 'center')

    def align_right(self, *args):
        content = self.texteditor.get(1.0, END)
        self.texteditor.tag_config('right', justify=RIGHT)
        self.texteditor.delete(1.0, END)
        self.texteditor.insert(INSERT, content, 'right')

    def find(self, *args):
        self.find = FindDialog(parent=self)

    def find_words(self, *args):
        word = self.find.entry_find.get()
        print(word)
        self.texteditor.tag_remove('match', '1.0', END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = self.texteditor.search(word, start_pos, stopindex=END)
                if not start_pos:
                    break
                end_pos = '{}+{}c'.format(start_pos, len(word))
                self.texteditor.tag_add('match', start_pos, end_pos)
                matches += 1
                start_pos = end_pos
                self.texteditor.tag_config('match', foreground='red', background='yellow')

    def replace_words(self, *args):
        replace_text = self.find.entry_replace.get()
        word = self.find.entry_find.get()
        content = self.texteditor.get(1.0, END)
        new_value = content.replace(word, replace_text)
        self.texteditor.delete(1.0, END)
        self.texteditor.insert(1.0, new_value)

    def hide_toolbar(self, *args):
        global show_toolbar
        if show_toolbar:
            self.toolbar.pack_forget()
            show_toolbar = False
        else:
            self.texteditor.pack_forget()
            self.statusbar.pack_forget()
            self.toolbar.pack(side=TOP, fill=X)
            self.texteditor.pack(expand=YES, fill=BOTH)
            self.statusbar.pack(side=BOTTOM)
            show_toolbar = True

    def hide_status_bar(self, *args):
        global show_status_bar
        if show_status_bar:
            self.statusbar.pack_forget()
            show_status_bar = False
        else:
            self.statusbar.pack()
            show_status_bar = True


if __name__ == '__main__':
    root = Tk()
    root.title('Text Editor')
    instance = MainApplication(root).pack(side=TOP, fill=BOTH, expand=True)
    root.iconbitmap('icons/icon.ico')
    root.geometry('700x600+30+30')
    #root.geometry('1250x850')
    root.mainloop()
