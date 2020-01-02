#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 22, 2019 12:31:44 AM EET  platform: Windows NT

import sys
from tkinter import PhotoImage, messagebox, StringVar
import sqlite3
import change_customer_support
from datetime import datetime

dbase = "Service_book.db"
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


# Να πάρουμε Φωτοτυπικά και πελάτη
def get_copiers_data():
    copiers = []
    customers_list = []

    conn = sqlite3.connect(dbase)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Πελάτες WHERE Κατάσταση =1")
    customers = cursor.fetchall()
    for n in range(len(customers)):
        if customers[n][1] != "" and customers[n][1] is not None:
            customers_list.append(customers[n][1])
    cursor.close()
    conn.close()
    return sorted(customers_list)


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    change_customer_support.set_Tk_var()
    top = add_copier_window(root)
    change_customer_support.init(root, top)
    root.mainloop()


w = None


def create_add_copier_window(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    change_customer_support.set_Tk_var()
    top = add_copier_window(w)
    change_customer_support.init(w, top, *args, **kwargs)
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
        self.style.map('TNotebook.Tab', background=[('selected', "#999933"), ('active', "#33994d")])
        self.style.map('TNotebook.Tab', foreground=[('selected', "white"), ('active', "white")])

        self.customers_list = get_copiers_data()
        self.copiers = []
        self.top = top
        top.geometry("505x524+444+228")
        top.minsize(120, 1)
        top.maxsize(1604, 881)
        top.resizable(1, 1)
        top.title("Αλλαγή πελάτη")
        top.configure(background="#f6f6ee")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.bind('<Escape>', self.quit)
        top.focus()

        self.old_customer_label = tk.Label(top)
        self.old_customer_label.place(relx=0.025, rely=0.095, height=31, relwidth=0.230)
        self.old_customer_label.configure(activebackground="#f9f9f9")
        self.old_customer_label.configure(activeforeground="black")
        self.old_customer_label.configure(background="#808000")
        self.old_customer_label.configure(disabledforeground="#a3a3a3")
        self.old_customer_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.old_customer_label.configure(foreground="#ffffff")
        self.old_customer_label.configure(highlightbackground="#d9d9d9")
        self.old_customer_label.configure(highlightcolor="black")
        self.old_customer_label.configure(relief="groove")
        self.old_customer_label.configure(text='''Από πελάτη''')

        # self.get_copiers_btn = tk.Button(top)
        # self.get_copiers_btn.place(relx=0.885, rely=0.095, height=30, relwidth=0.060)
        # self.get_copiers_btn.configure(background="#006291")
        # self.get_copiers_btn_btn_img1 = PhotoImage(file="icons/reload.png")
        # self.get_copiers_btn.configure(image=self.get_copiers_btn_btn_img1)
        # self.get_copiers_btn.configure(command=self.get_copier)

        self.new_customer_label = tk.Label(top)
        self.new_customer_label.place(relx=0.025, rely=0.324, height=31, relwidth=0.230)
        self.new_customer_label.configure(activebackground="#f9f9f9")
        self.new_customer_label.configure(activeforeground="black")
        self.new_customer_label.configure(background="#808000")
        self.new_customer_label.configure(disabledforeground="#a3a3a3")
        self.new_customer_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.new_customer_label.configure(foreground="#ffffff")
        self.new_customer_label.configure(highlightbackground="#d9d9d9")
        self.new_customer_label.configure(highlightcolor="black")
        self.new_customer_label.configure(relief="groove")
        self.new_customer_label.configure(text='''Πρός πελάτη''')

        # self.start_counter_label = tk.Label(top)
        # self.start_counter_label.place(relx=0.025, rely=0.401, height=31, relwidth=0.230)
        # self.start_counter_label.configure(activebackground="#f9f9f9")
        # self.start_counter_label.configure(activeforeground="black")
        # self.start_counter_label.configure(background="#808000")
        # self.start_counter_label.configure(disabledforeground="#a3a3a3")
        # self.start_counter_label.configure(font="-family {Calibri} -size 10 -weight bold")
        # self.start_counter_label.configure(foreground="#ffffff")
        # self.start_counter_label.configure(highlightbackground="#d9d9d9")
        # self.start_counter_label.configure(highlightcolor="black")
        # self.start_counter_label.configure(relief="groove")
        # self.start_counter_label.configure(text='''Μετρητής έναρξης''')

        # self.notes_label = tk.Label(top)
        # self.notes_label.place(relx=0.025, rely=0.573, height=31, relwidth=0.940)
        # self.notes_label.configure(activebackground="#f9f9f9")
        # self.notes_label.configure(activeforeground="black")
        # self.notes_label.configure(background="#6b6b6b")
        # self.notes_label.configure(disabledforeground="#a3a3a3")
        # self.notes_label.configure(font="-family {Calibri} -size 10 -weight bold")
        # self.notes_label.configure(foreground="#ffffff")
        # self.notes_label.configure(highlightbackground="#d9d9d9")
        # self.notes_label.configure(highlightcolor="black")
        # self.notes_label.configure(relief="groove")
        # self.notes_label.configure(text='''Σημειώσεις''')

        # self.serial_label = tk.Label(top)
        # self.serial_label.place(relx=0.025, rely=0.248, height=31, relwidth=0.230)
        # self.serial_label.configure(activebackground="#f9f9f9")
        # self.serial_label.configure(activeforeground="black")
        # self.serial_label.configure(background="#808000")
        # self.serial_label.configure(disabledforeground="#a3a3a3")
        # self.serial_label.configure(font="-family {Calibri} -size 10 -weight bold")
        # self.serial_label.configure(foreground="#ffffff")
        # self.serial_label.configure(highlightbackground="#d9d9d9")
        # self.serial_label.configure(highlightcolor="black")
        # self.serial_label.configure(relief="groove")
        # self.serial_label.configure(text='''Serial''')

        self.customer_copiers_label = tk.Label(top)
        self.customer_copiers_label.place(relx=0.025, rely=0.172, height=31, relwidth=0.230)
        self.customer_copiers_label.configure(activebackground="#f9f9f9")
        self.customer_copiers_label.configure(activeforeground="black")
        self.customer_copiers_label.configure(background="#808000")
        self.customer_copiers_label.configure(disabledforeground="#a3a3a3")
        self.customer_copiers_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.customer_copiers_label.configure(foreground="#ffffff")
        self.customer_copiers_label.configure(highlightbackground="#d9d9d9")
        self.customer_copiers_label.configure(highlightcolor="black")
        self.customer_copiers_label.configure(relief="groove")
        self.customer_copiers_label.configure(text='''Φωτοτυπικό''')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.025, rely=0.400, relwidth=0.840)

        # self.serial = StringVar()
        # self.selial_entry = tk.Entry(top)
        # self.selial_entry.place(relx=0.27, rely=0.248, height=30, relwidth=0.593)
        # self.selial_entry.configure(textvariable=self.serial)
        # self.selial_entry.configure(background="white")
        # self.selial_entry.configure(disabledforeground="#a3a3a3")
        # self.selial_entry.configure(font="TkFixedFont")
        # self.selial_entry.configure(foreground="#000000")
        # self.selial_entry.configure(highlightbackground="#d9d9d9")
        # self.selial_entry.configure(highlightcolor="black")
        # self.selial_entry.configure(insertbackground="black")
        # self.selial_entry.configure(selectbackground="#c4c4c4")
        # self.selial_entry.configure(selectforeground="black")

        # self.notes = StringVar()
        # self.notes_scrolledtext = ScrolledText(top)
        # self.notes_scrolledtext.place(relx=0.025, rely=0.649, relheight=0.25, relwidth=0.941)
        # self.notes_scrolledtext.insert('1.0', self.notes.get())
        # self.notes_scrolledtext.configure(background="white")
        # self.notes_scrolledtext.configure(font="TkTextFont")
        # self.notes_scrolledtext.configure(foreground="black")
        # self.notes_scrolledtext.configure(highlightbackground="#d9d9d9")
        # self.notes_scrolledtext.configure(highlightcolor="black")
        # self.notes_scrolledtext.configure(insertbackground="black")
        # self.notes_scrolledtext.configure(insertborderwidth="3")
        # self.notes_scrolledtext.configure(selectbackground="#c4c4c4")
        # self.notes_scrolledtext.configure(selectforeground="black")
        # self.notes_scrolledtext.configure(wrap="none")

        self.copiers_combobox = ttk.Combobox(top)
        self.copiers_combobox.place(relx=0.27, rely=0.172, relheight=0.057, relwidth=0.593)
        self.copiers_combobox.configure(values="")
        self.copiers_combobox.configure(takefocus="")
        # self.copiers_combobox.configure(state="readonly")



        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.025, rely=0.019, height=31, relwidth=0.840)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#006291")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Calibri} -size 12 -weight bold")
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(relief="groove")
        self.Label2.configure(text='''Μεταφορά φωτοτυπικού''')

        # self.start = StringVar()
        # self.start_entry = tk.Entry(top)
        # self.start_entry.place(relx=0.27, rely=0.324, height=30, relwidth=0.593)
        # self.start_entry.configure(textvariable=self.start)
        # self.start_entry.configure(background="white")
        # self.start_entry.configure(disabledforeground="#a3a3a3")
        # self.start_entry.configure(font="TkFixedFont")
        # self.start_entry.configure(foreground="#000000")
        # self.start_entry.configure(insertbackground="black")

        # self.start_counter = StringVar()
        # self.start_counter_entry = tk.Entry(top)
        # self.start_counter_entry.place(relx=0.27, rely=0.401, height=30, relwidth=0.593)
        # self.start_counter_entry.configure(textvariable=self.start_counter)
        # self.start_counter_entry.configure(background="white")
        # self.start_counter_entry.configure(disabledforeground="#a3a3a3")
        # self.start_counter_entry.configure(font="TkFixedFont")
        # self.start_counter_entry.configure(foreground="#000000")
        # self.start_counter_entry.configure(insertbackground="black")

        # self.all_copiers_label = tk.Label(top)
        # self.all_copiers_label.place(relx=0.025, rely=0.248, height=29, relwidth=0.230)
        # self.all_copiers_label.configure(background="#808000")
        # self.all_copiers_label.configure(disabledforeground="#a3a3a3")
        # self.all_copiers_label.configure(font="-family {Calibri} -size 10 -weight bold")
        # self.all_copiers_label.configure(foreground="#ffffff")
        # self.all_copiers_label.configure(relief="groove")
        # self.all_copiers_label.configure(text='''Ολα τα φωτοτυπικά''')

        self.customer_combobox = ttk.Combobox(top)
        self.customer_combobox.place(relx=0.27, rely=0.095, relheight=0.059, relwidth=0.593)
        self.customer_combobox.configure(values=self.customers_list)
        self.customer_combobox.configure(takefocus="")
        self.customer_combobox.bind("<<ComboboxSelected>>", self.get_copier)

        self.new_customer_combobox = ttk.Combobox(top)
        self.new_customer_combobox.place(relx=0.27, rely=0.324, relheight=0.059, relwidth=0.593)
        self.new_customer_combobox.configure(values=self.customers_list)
        self.new_customer_combobox.configure(takefocus="")

        self.notes_label = tk.Label(top)
        self.notes_label.place(relx=0.025, rely=0.430, height=31, relwidth=0.840)
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
        self.notes_scrolledtext.place(relx=0.025, rely=0.500, relheight=0.25, relwidth=0.840)
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
        self.save_btn.place(relx=0.300, rely=0.800, height=34, width=147)
        self.save_btn.configure(activebackground="#ececec")
        self.save_btn.configure(activeforeground="#000000")
        self.save_btn.configure(background="#808000")
        self.save_btn.configure(disabledforeground="#a3a3a3")
        self.save_btn.configure(font="-family {Calibri} -size 11 -weight bold")
        self.save_btn.configure(foreground="#ffffff")
        self.save_btn.configure(highlightbackground="#d9d9d9")
        self.save_btn.configure(highlightcolor="black")
        self.save_btn.configure(pady="0")
        self.save_btn.configure(text='''Αποθήκευση''')
        self.save_btn.configure(command=self.add_copier)

    def quit(self, event):
        self.top.destroy()

    def get_copier(self, event=None):
        # να πάρουμε το id του πελάτη απο το ονομα του
        old_customer = self.customer_combobox.get()
        self.copiers_combobox.set(value="")

        con = sqlite3.connect(dbase)
        cursor = con.cursor()
        cursor.execute("SELECT ID FROM Πελάτες WHERE  Επωνυμία_Επιχείρησης =?", (old_customer,))
        old_customer_id = cursor.fetchall()  # ==> [(4,)] αρα θέλουμε το customer_id[0][0]
        old_customer_id = old_customer_id[0][0]

        # Εμφάνιση φωτοτυπικών σύμφονα με το customer_id
        cursor.execute("SELECT * FROM Φωτοτυπικά WHERE Πελάτη_ID = ? AND Κατάσταση = 1 ", (old_customer_id,))
        copiers = cursor.fetchall()
        for copier in copiers:
            self.copiers.append(copier)
        cursor.close()
        con.close()


        self.copiers_combobox.configure(values=copiers)


    def add_copier(self):
        today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        selected_copier_index = self.copiers_combobox.current()  # index απο την λίστα φωτοτυπικών του πελάτη

        try:
            copier_id = self.copiers[selected_copier_index][0]

        except IndexError as error:  # αν δεν επιλεξουμε Φωτοτυπικό
            messagebox.showwarning("Προσοχή ", "Παρακαλώ \n Επιλεξτε  Φωτοτυπικό")
            self.top.focus()
            return

        new_customer_name = self.new_customer_combobox.get()

        if not new_customer_name:
            messagebox.showwarning("Προσοχή", "Παρακαλώ επιλέξτε νέο πελάτη")
            self.top.focus()
            return
        con = sqlite3.connect(dbase)
        cursor = con.cursor()
        cursor.execute("SELECT ID FROM Πελάτες WHERE Επωνυμία_Επιχείρησης =?", (new_customer_name,))
        new_customer = cursor.fetchall()
        new_customer_id = new_customer[0][0]

        # ενημέρωση το πεδίο Πελάτη_ID του φωτοτυπικού με το ID του νέου πελάτη
        # ("UPDATE Service  SET " + edited_culumns + " WHERE ID=? ", (tuple(data_to_add)))
        cursor.execute("UPDATE Φωτοτυπικά SET Πελάτη_ID =? WHERE ID=? ", (new_customer_id, copier_id,))
        con.commit()
        con.close()

        # Ενημέρωση Copiers_Log στορικού μεταφοράς Φωοτυπικού
        # Δημιουργία culumns για τO Copiers_Log
        con = sqlite3.connect(dbase)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Copiers_Log")
        headers = list(map(lambda x: x[0], cursor.description))
        culumns = ", ".join(headers)
        values = []
        for head in headers:
            if head == "ID":
                values.append("Null")
            else:
                values.append("?")
        values = ", ".join(values)

        # self.customer_combobox.get() => παλιός πελάτης
        data = [copier_id, self.copiers_combobox.get(), today, self.customer_combobox.get(),
                self.new_customer_combobox.get(), self.notes_scrolledtext.get('1.0', 'end-1c')]

        sql_insert = "INSERT INTO Copiers_Log (" + culumns + ")" + "VALUES(" + values + ");"
        cursor.execute(sql_insert, tuple(data))
        con.commit()
        con.close()

        # Να πάρουμε τις σημειώσεις για να προσθέσουμε το πότε αλλαξε πελάτη το φωτοτυπικό
        old_customer = self.customer_combobox.get()
        notes = self.notes_scrolledtext.get("1.0", "end-1c")
        con = sqlite3.connect(dbase)
        cursor = con.cursor()
        cursor.execute("SELECT Σημειώσεις FROM Φωτοτυπικά WHERE ID=?", (copier_id,))
        old_notes = cursor.fetchall()

        data_for_copiers_notes = old_notes[0][0] + "\n" + today + " Μεταφορά απο " + str(
            old_customer) + " στο(ν) " + new_customer_name + " " + notes
        cursor.execute("UPDATE Φωτοτυπικά SET  Σημειώσεις =? WHERE ID =?", (data_for_copiers_notes, copier_id))
        con.commit()
        con.close()
        messagebox.showwarning("Επιτυχής μεταφορά", f"To {self.copiers_combobox.get()} μεταφέρθηκε επιτυχώς στον πελάτη"
                                                    f" {self.new_customer_combobox.get()}")

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
