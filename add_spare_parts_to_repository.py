#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 22, 2019 12:31:44 AM EET  platform: Windows NT

import add_copier_support
import sys
from tkinter import messagebox, StringVar, filedialog
import sqlite3
from settings import dbase, root_logger, spare_parts_db  # settings
import os
import view_images_from_repository
# -------------ΔΗΜΗΟΥΡΓΕΙΑ LOG FILE  ------------------
sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info
print(f"{100 * '*'}\n\t\t\t\t\t\t\t\t\t\tFILE {__name__}")

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    add_copier_support.set_Tk_var()
    top = add_copier_window(root)
    add_copier_support.init(root, top)
    root.mainloop()


w = None
table = None


def create_insert_spare_parts_window(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt, table
    rt = root
    table = args[0]  # Πίνακας αποθήκης ανταλλακτικών απο το service_book

    w = tk.Toplevel(root)
    add_copier_support.set_Tk_var()
    top = add_copier_window(w)
    add_copier_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_add_copier_window():
    global w
    w.destroy()
    w = None


class add_copier_window:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('clam')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', _compcolor), ('active', _ana2color)])

        # ==============================  Notebook style  =============
        self.style.map('TNotebook.Tab', background=[('selected', "#6b6b6b"), ('active', "#69ab3a")])
        self.style.map('TNotebook.Tab', foreground=[('selected', "white"), ('active', "white")])

        self.table = table
        self.files = ""
        self.len_images = ""
        self.id = ""
        self.top = top
        top.geometry("505x524+444+228")
        top.minsize(120, 1)
        top.maxsize(1604, 881)
        top.resizable(1, 1)
        top.title("Προσθήκη Ανταλλακτικού")
        top.configure(background="#f6f6ee")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.bind('<Escape>', self.quit)
        top.focus()

        self.parts_nr_label = tk.Label(top)
        self.parts_nr_label.place(relx=0.025, rely=0.095, height=31, relwidth=0.230)
        self.parts_nr_label.configure(activebackground="#f9f9f9")
        self.parts_nr_label.configure(activeforeground="black")
        self.parts_nr_label.configure(background="#6b6b6b")
        self.parts_nr_label.configure(disabledforeground="#a3a3a3")
        self.parts_nr_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.parts_nr_label.configure(foreground="#ffffff")
        self.parts_nr_label.configure(highlightbackground="#d9d9d9")
        self.parts_nr_label.configure(highlightcolor="black")
        self.parts_nr_label.configure(relief="groove")
        self.parts_nr_label.configure(text='''Part Nr''')

        self.parts_nr = StringVar()
        self.parts_nr_entry = tk.Entry(top)
        self.parts_nr_entry.place(relx=0.260, rely=0.095, height=31, relwidth=0.593)
        self.parts_nr_entry.configure(textvariable=self.parts_nr)
        self.parts_nr_entry.configure(background="white")
        self.parts_nr_entry.configure(disabledforeground="#a3a3a3")
        self.parts_nr_entry.configure(font="TkFixedFont")
        self.parts_nr_entry.configure(foreground="#000000")
        self.parts_nr_entry.configure(highlightbackground="#d9d9d9")
        self.parts_nr_entry.configure(highlightcolor="black")
        self.parts_nr_entry.configure(insertbackground="black")
        self.parts_nr_entry.configure(selectbackground="#c4c4c4")
        self.parts_nr_entry.configure(selectforeground="black")

        # self.add_parts_nr_btn = tk.Button(top)
        # self.add_parts_nr_btn.place(relx=0.885, rely=0.095, height=30, relwidth=0.060)
        # self.add_parts_nr_btn.configure(background="#006291")
        # self.add_parts_nr_btn_btn_img1 = PhotoImage(file="icons/add_to_service_data1.png")
        # self.add_parts_nr_btn.configure(image=self.add_parts_nr_btn_btn_img1)
        # self.add_parts_nr_btn.configure(command=lambda: (self.add_company("part_nr")))

        self.description_label = tk.Label(top)
        self.description_label.place(relx=0.025, rely=0.172, height=31, relwidth=0.230)
        self.description_label.configure(background="#6b6b6b")
        self.description_label.configure(disabledforeground="#a3a3a3")
        self.description_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.description_label.configure(foreground="#ffffff")
        self.description_label.configure(relief="groove")
        self.description_label.configure(text='''Περιγραφή''')
        self.description = StringVar()
        self.description_entry = tk.Entry(top)
        self.description_entry.place(relx=0.260, rely=0.172, height=31, relwidth=0.593)
        self.description_entry.configure(textvariable=self.description)
        self.description_entry.configure(background="white")
        self.description_entry.configure(disabledforeground="#a3a3a3")
        self.description_entry.configure(font="TkFixedFont")
        self.description_entry.configure(foreground="#000000")
        self.description_entry.configure(highlightbackground="#d9d9d9")
        self.description_entry.configure(highlightcolor="black")
        self.description_entry.configure(insertbackground="black")
        self.description_entry.configure(selectbackground="#c4c4c4")
        self.description_entry.configure(selectforeground="black")

        self.code_label = tk.Label(top)
        self.code_label.place(relx=0.025, rely=0.248, height=31, relwidth=0.230)
        self.code_label.configure(activebackground="#f9f9f9")
        self.code_label.configure(activeforeground="black")
        self.code_label.configure(background="#6b6b6b")
        self.code_label.configure(disabledforeground="#a3a3a3")
        self.code_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.code_label.configure(foreground="#ffffff")
        self.code_label.configure(highlightbackground="#d9d9d9")
        self.code_label.configure(highlightcolor="black")
        self.code_label.configure(relief="groove")
        self.code_label.configure(text='''Κωδικός''')
        self.code = StringVar()
        self.code.trace('w', self.check_code)
        self.code_entry = tk.Entry(top)
        self.code_entry.place(relx=0.260, rely=0.248, height=31, relwidth=0.593)
        self.code_entry.configure(textvariable=self.code)
        self.code_entry.configure(background="white")
        self.code_entry.configure(disabledforeground="#a3a3a3")
        self.code_entry.configure(font="TkFixedFont")
        self.code_entry.configure(foreground="#000000")
        self.code_entry.configure(highlightbackground="#d9d9d9")
        self.code_entry.configure(highlightcolor="black")
        self.code_entry.configure(insertbackground="black")
        self.code_entry.configure(selectbackground="#c4c4c4")
        self.code_entry.configure(selectforeground="black")
        self.code_entry_warning = ttk.Label(top)
        self.code_entry_warning_img = tk.PhotoImage(file="icons/lamp.png")
        self.code_entry_warning.configure(image=self.code_entry_warning_img)
        self.code_entry_warning.configure(compound='left')
        self.code_entry_warning.configure(background="#ffffff")

        # self.add_code_btn = tk.Button(top)
        # self.add_code_btn.place(relx=0.885, rely=0.248, height=30, relwidth=0.060)
        # self.add_code_btn.configure(background="#006291")
        # self.add_code_btn_img = PhotoImage(file="icons/add_to_service_data2.png")
        # self.add_code_btn.configure(image=self.add_code_btn_img)
        # self.add_code_btn.configure(command=lambda: (self.add_company("Κωδικός")))

        self.pieces_label = tk.Label(top)
        self.pieces_label.place(relx=0.025, rely=0.324, height=31, relwidth=0.230)
        self.pieces_label.configure(activebackground="#f9f9f9")
        self.pieces_label.configure(activeforeground="black")
        self.pieces_label.configure(background="#6b6b6b")
        self.pieces_label.configure(disabledforeground="#a3a3a3")
        self.pieces_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.pieces_label.configure(foreground="#ffffff")
        self.pieces_label.configure(highlightbackground="#d9d9d9")
        self.pieces_label.configure(highlightcolor="black")
        self.pieces_label.configure(relief="groove")
        self.pieces_label.configure(text='''Τεμάχια''')
        self.pieces = StringVar()
        self.pieces_entry = tk.Entry(top)
        self.pieces_entry.place(relx=0.260, rely=0.324, height=31, relwidth=0.593)
        self.pieces_entry.configure(textvariable=self.pieces)
        self.pieces_entry.configure(background="white")
        self.pieces_entry.configure(disabledforeground="#a3a3a3")
        self.pieces_entry.configure(font="TkFixedFont")
        self.pieces_entry.configure(foreground="#000000")
        self.pieces_entry.configure(highlightbackground="#d9d9d9")
        self.pieces_entry.configure(highlightcolor="black")
        self.pieces_entry.configure(insertbackground="black")
        self.pieces_entry.configure(selectbackground="#c4c4c4")
        self.pieces_entry.configure(selectforeground="black")

        # Προσθήκη αρχείων
        self.add_files_btn = tk.Button(top)
        self.add_files_btn.place(relx=0.025, rely=0.410, height=50, relwidth=0.350)
        self.add_files_btn.configure(activebackground="#ececec")
        self.add_files_btn.configure(activeforeground="#000000")
        self.add_files_btn.configure(background="green")
        self.add_files_btn.configure(disabledforeground="#a3a3a3")
        self.add_files_btn.configure(foreground="#ffffff")
        self.add_files_btn.configure(highlightbackground="#d9d9d9")
        self.add_files_btn.configure(highlightcolor="black")
        self.add_files_btn.configure(pady="0")
        self.add_files_btn.configure(text='''Προσθήκη αρχείων''')
        self.add_files_btn.configure(command=self.add_files)
        self.add_files_btn_img = tk.PhotoImage(file="icons/add_files.png")
        self.add_files_btn.configure(image=self.add_files_btn_img)
        self.add_files_btn.configure(compound="left")

        # Αρχεία
        self.show_files_btn = tk.Button(top)
        # self.show_files_btn.place(relx=0.420, rely=0.410, height=50, relwidth=0.350)
        self.show_files_btn.configure(activebackground="#ececec")
        self.show_files_btn.configure(activeforeground="#000000")
        self.show_files_btn.configure(background="#6b6b6b")
        self.show_files_btn.configure(disabledforeground="red")
        self.show_files_btn.configure(foreground="#ffffff")
        self.show_files_btn.configure(highlightbackground="#d9d9d9")
        self.show_files_btn.configure(highlightcolor="black")
        self.show_files_btn.configure(pady="0")
        self.show_files_btn.configure(text=f'Προβολή {self.len_images} αρχείων')

        self.show_files_btn.configure(command=self.show_files)
        self.show_files_btn_img = tk.PhotoImage(file="icons/view_files.png")
        self.show_files_btn.configure(image=self.show_files_btn_img)
        self.show_files_btn.configure(compound="left")

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.025, rely=0.553, relwidth=0.938)

        self.notes_label = tk.Label(top)
        self.notes_label.place(relx=0.025, rely=0.573, height=31, relwidth=0.940)
        self.notes_label.configure(activebackground="#f9f9f9")
        self.notes_label.configure(activeforeground="black")
        self.notes_label.configure(background="#6b6b6b")
        self.notes_label.configure(disabledforeground="#a3a3a3")
        self.notes_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.notes_label.configure(foreground="#ffffff")
        self.notes_label.configure(highlightbackground="#d9d9d9")
        self.notes_label.configure(highlightcolor="black")
        self.notes_label.configure(relief="groove")
        self.notes_label.configure(text='''Σημειώσεις''')

        self.notes = StringVar()
        self.notes_scrolledtext = ScrolledText(top)
        self.notes_scrolledtext.place(relx=0.025, rely=0.649, relheight=0.25, relwidth=0.941)
        self.notes_scrolledtext.insert('1.0', self.notes.get())
        self.notes_scrolledtext.configure(background="white")
        self.notes_scrolledtext.configure(font="TkTextFont")
        self.notes_scrolledtext.configure(foreground="black")
        self.notes_scrolledtext.configure(highlightbackground="#d9d9d9")
        self.notes_scrolledtext.configure(highlightcolor="black")
        self.notes_scrolledtext.configure(insertbackground="black")
        self.notes_scrolledtext.configure(insertborderwidth="3")
        self.notes_scrolledtext.configure(selectbackground="#c4c4c4")
        self.notes_scrolledtext.configure(selectforeground="black")
        self.notes_scrolledtext.configure(wrap="none")

        self.save_btn = tk.Button(top)
        self.save_btn.place(relx=0.296, rely=0.916, height=34, width=147)
        self.save_btn.configure(activebackground="#ececec")
        self.save_btn.configure(activeforeground="#000000")
        self.save_btn.configure(background="green")
        self.save_btn.configure(disabledforeground="#a3a3a3")
        self.save_btn.configure(font="-family {Calibri} -size 11 -weight bold")
        self.save_btn.configure(foreground="#ffffff")
        self.save_btn.configure(highlightbackground="#d9d9d9")
        self.save_btn.configure(highlightcolor="black")
        self.save_btn.configure(pady="0")
        self.save_btn.configure(text='''Εισαγωγή''')
        self.save_btn.configure(command=self.add_spare_part)

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.025, rely=0.019, height=31, relwidth=0.938)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#006291")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Calibri} -size 12 -weight bold")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(relief="groove")
        self.Label2.configure(text=f'''Εισαγωγή ανταλλακτικού {self.table}''')
        self.get_next_id()

    def quit(self, event):
        self.top.destroy()

    def get_next_id(self):
        con = sqlite3.connect(spare_parts_db)
        c = con.cursor()
        c.execute("SELECT seq FROM sqlite_sequence WHERE NAME =?", (self.table,))
        data = c.fetchall()

        next_id = data[0][0]
        self.id = str(self.table) + "_" + str(int(next_id) + 1)

    # Ελεγχος αν υπάρχουν αρχεία για προβολή
    def check_if_files_exists(self):

        con = sqlite3.connect(spare_parts_db)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Images WHERE ID =?", (self.id,))
        images = cursor.fetchall()

        self.len_images = len(images)
        self.show_files_btn.configure(text=f'Προβολή {self.len_images}\nαρχείων')
        cursor.close()
        con.close()
        if self.files:
            self.show_files_btn.place(relx=0.420, rely=0.410, height=50, relwidth=0.350)
            self.show_files_btn.configure(command=self.show_files)
        elif not images:  # αδεια λιστα δλδ δεν υπάρχουν αρχεια και απενεργοποιουμε το κουμπί προβολή αρχείων
            self.show_files_btn.place_forget()

    # Προβολή αρχείων
    def show_files(self):
        view_images_from_repository.create_Toplevel1(w, self.id, spare_parts_db)

    # Προσθήκη αρχείων
    def add_files(self):

        self.files = filedialog.askopenfilenames(initialdir=os.getcwd(), title="Επιλογή αρχείων για προσθήκη",
                                                     filetypes=[("Υπ. αρχεία", "*.jpg *.png *.pdf")])

        if self.files == "":  # αν ο χρήστης επιλεξει ακυρο

            return
        else:
            self.add_files_to_db()
            self.show_files_btn.configure(text=f'{len(self.files)} Αρχεία για προσθήκη')
            self.check_if_files_exists()

    # Προσθήκη αρχείων στην βάση
    def add_files_to_db(self):
        if self.files == "":
            return
        con = sqlite3.connect(spare_parts_db)
        cursor = con.cursor()
        cursor.execute("SELECT Filename FROM Images WHERE ID =?", (self.id,))
        # υπάρχοντα αρχεία
        images = cursor.fetchall()

        cursor.close()
        con.close()

        con = sqlite3.connect(spare_parts_db)
        cu = con.cursor()

        # Εισαγωγη αρχείων
        for img in self.files:

            base = os.path.basename(img)
            filename, ext = os.path.splitext(base)
            # Ελεγχος αν το αρχείο υπάρχει σε αυτο το προιόν
            try:
                if filename in images[0]:
                    messagebox.showerror("img!", f'Το αρχείο {filename} υπάρχει.'
                                                 f'\nΠαρακαλώ αλλάξτε όνομα ή επιλεξτε διαφορετικό αρχείο')
                    break
            except IndexError:  # Όταν δεν υπάρχουν αρχεία
                pass
            with open(img, 'rb') as f:
                file = f.read()  # Εισαγωγη αρχείων
                file_size = len(file)  # μεγεθος σε bytes

                cu.execute("INSERT INTO Images(ID, Filename, Type, File_size, File, ΚΩΔΙΚΟΣ)"
                               "VALUES(?,?,?,?,?,?)", (self.id, filename, ext, file_size, sqlite3.Binary(file),
                                                       self.code.get()))

        con.commit()
        con.close()
        self.top.focus()
        self.check_if_files_exists()


    # Ελεγχος αν το serial  υπάρχει
    def check_code(self, name, index, mode):
        self.code_entry_warning.place_forget()
        # current_copier_id = (self.copiers_treeview.set(self.copiers_treeview.selection(), '#1'))

        all_codes = []
        con = sqlite3.connect(spare_parts_db)
        c = con.cursor()
        c.execute("SELECT ΚΩΔΙΚΟΣ FROM " + self.table + ";")
        codes = c.fetchall()
        # c.execute("SELECT Serial FROM Φωτοτυπικά WHERE ID = ?", (current_copier_id,))
        # current_serial = c.fetchall()
        con.close()

        for code in codes:
            all_codes.append(code[0])

        if self.code.get() in all_codes :
            self.code_entry.configure(foreground="red")
            # self.code_entry.place(relx=0.260, rely=0.248, height=31, relwidth=0.593)
            self.code_entry_warning.place(relx=0.860, rely=0.248, relheight=0.060, relwidth=0.060)
        else:
            self.code_entry.configure(foreground="green")
            self.code_entry_warning.place_forget()

    def add_spare_part(self):
        conn = sqlite3.connect(spare_parts_db)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM " + self.table + ";")
        headers = list(map(lambda x: x[0], cursor.description))
        columns = ", ".join(headers)
        values = []
        for head in headers:
            if head == "ID" or head == "Id" or head == "id":
                values.append("Null")
            else:
                values.append("?")
        values = ", ".join(values)
        data = [self.parts_nr.get(), self.description.get(), self.code.get(),
                self.pieces.get(), self.notes_scrolledtext.get('1.0', 'end-1c')]

        sql_insert = "INSERT INTO " + self.table + "(" + columns + ")" + "VALUES(" + values + ");"
        cursor.execute(sql_insert, tuple(data))
        conn.commit()
        conn.close()
        messagebox.showinfo("Info", f"Το  {self.code.get()} προστέθηκε επιτυχώς στο {self.table}")

        self.top.destroy()
        return None


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        # self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                      | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                      + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''

        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)

    return wrapped


class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''

    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


import platform


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


if __name__ == '__main__':
    vp_start_gui()
