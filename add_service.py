#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 16, 2019 11:26:05 PM EET  platform: Windows NT
"""
V0.3.2 Προσθήκη αυτόματης ημερωμηνίας

"""
import sys
import sqlite3
from tkinter import StringVar, messagebox, PhotoImage
import add_service_window_support
import platform
from datetime import datetime

dbase = "Service_book.db"
selected_copier_id = None

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


def get_service_data():
    purpose_list = []
    actions_list = []
    conn = sqlite3.connect(dbase)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Service_data")
    service_data = cursor.fetchall()
    cursor.close()
    conn.close()
    for n in range(len(service_data)):
        if service_data[n][1] != "" and service_data[n][1] is not None:
            purpose_list.append(service_data[n][1])
        if service_data[n][2] != "" and service_data[n][2] is not None:
            actions_list.append(service_data[n][2])
    return sorted(purpose_list), sorted(actions_list)


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    add_service_window_support.set_Tk_var()
    top = add_service_window(root)
    add_service_window_support.init(root, top)
    root.mainloop()


w = None


def create_add_service_window(root, *args, **kwargs):
    """
    Starting point when module is imported by another program.
    :param root:
    :param args:
    :param kwargs:
    :return:
    """
    global w, w_win, rt, selected_copier_id
    selected_copier_id = args[0]  # εδώ περνουμε το selected_copier_id απο το service_book_colors.py
    rt = root
    w = tk.Toplevel(root)
    add_service_window_support.set_Tk_var()
    top = add_service_window(w)
    add_service_window_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_add_service_window():
    global w
    w.destroy()
    w = None


class add_service_window():

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        # Αρχικοποιηση του selected_service_id σαν self.selected_service_id
        self.selected_copier_id = selected_copier_id

        self.purpose_list, self.actions_list = get_service_data()
        self.culumns = None
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font11 = "-family Calibri -size 10 -weight bold -slant roman " \
                 "-underline 0 -overstrike 0"
        font13 = "-family Calibri -size 11 -weight bold -slant roman " \
                 "-underline 0 -overstrike 0"
        font9 = "-family Calibri -size 12 -weight bold -slant roman " \
                "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])
        self.top = top
        top.geometry("655x650+443+54")
        top.minsize(120, 1)
        top.maxsize(1604, 881)
        top.resizable(1, 1)
        top.title("Προσθήκη ιστορικού συντήρησης")
        top.configure(background="#006291")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.focus()
        top.bind('<Escape>', self.quit)

        self.date_label = tk.Label(top)
        self.date_label.place(relx=0.025, rely=0.290, height=31, relwidth=0.250)
        self.date_label.configure(activebackground="#f9f9f9")
        self.date_label.configure(activeforeground="black")
        self.date_label.configure(background="#6b6b6b")
        self.date_label.configure(disabledforeground="#a3a3a3")
        self.date_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.date_label.configure(foreground="#ffffff")
        self.date_label.configure(highlightbackground="#d9d9d9")
        self.date_label.configure(highlightcolor="black")
        self.date_label.configure(relief="groove")
        self.date_label.configure(text='''Ημερομηνία''')

        self.purpose_label = tk.Label(top)
        self.purpose_label.place(relx=0.025, rely=0.394, height=31, relwidth=0.250)
        self.purpose_label.configure(activebackground="#f9f9f9")
        self.purpose_label.configure(activeforeground="black")
        self.purpose_label.configure(background="#6b6b6b")
        self.purpose_label.configure(disabledforeground="#a3a3a3")
        self.purpose_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.purpose_label.configure(foreground="#ffffff")
        self.purpose_label.configure(highlightbackground="#d9d9d9")
        self.purpose_label.configure(highlightcolor="black")
        self.purpose_label.configure(relief="groove")
        self.purpose_label.configure(text='''Σκοπός επίσκεψης''')

        self.actions_label = tk.Label(top)
        self.actions_label.place(relx=0.025, rely=0.444, height=31, relwidth=0.250)
        self.actions_label.configure(activebackground="#f9f9f9")
        self.actions_label.configure(activeforeground="black")
        self.actions_label.configure(background="#6b6b6b")
        self.actions_label.configure(disabledforeground="#a3a3a3")
        self.actions_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.actions_label.configure(foreground="#ffffff")
        self.actions_label.configure(highlightbackground="#d9d9d9")
        self.actions_label.configure(highlightcolor="black")
        self.actions_label.configure(relief="groove")
        self.actions_label.configure(text='''Ενέργειες''')

        self.notes_label = tk.Label(top)
        self.notes_label.place(relx=0.300, rely=0.550, height=31, relwidth=0.350)
        self.notes_label.configure(activebackground="#f9f9f9")
        self.notes_label.configure(activeforeground="black")
        self.notes_label.configure(background="#6b6b6b")
        self.notes_label.configure(disabledforeground="#a3a3a3")
        self.notes_label.configure(font=font11)
        self.notes_label.configure(foreground="#ffffff")
        self.notes_label.configure(highlightbackground="#d9d9d9")
        self.notes_label.configure(highlightcolor="black")
        self.notes_label.configure(relief="groove")
        self.notes_label.configure(text='''Σημειώσεις''')

        self.counter_label = tk.Label(top)
        self.counter_label.place(relx=0.025, rely=0.240, height=31, relwidth=0.250)
        self.counter_label.configure(activebackground="#f9f9f9")
        self.counter_label.configure(activeforeground="black")
        self.counter_label.configure(background="#6b6b6b")
        self.counter_label.configure(disabledforeground="#a3a3a3")
        self.counter_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.counter_label.configure(foreground="#ffffff")
        self.counter_label.configure(highlightbackground="#d9d9d9")
        self.counter_label.configure(highlightcolor="black")
        self.counter_label.configure(relief="groove")
        self.counter_label.configure(text='''Μετρητής''')

        self.next_service_label = tk.Label(top)
        self.next_service_label.place(relx=0.025, rely=0.343, height=31, relwidth=0.250)
        self.next_service_label.configure(activebackground="#f9f9f9")
        self.next_service_label.configure(activeforeground="black")
        self.next_service_label.configure(background="#6b6b6b")
        self.next_service_label.configure(disabledforeground="#a3a3a3")
        self.next_service_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.next_service_label.configure(foreground="#ffffff")
        self.next_service_label.configure(highlightbackground="#d9d9d9")
        self.next_service_label.configure(highlightcolor="black")
        self.next_service_label.configure(relief="groove")
        self.next_service_label.configure(text='''Επόμενο Service''')

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.025, rely=0.520, relwidth=0.938)


        self.date_entry = tk.Entry(top)
        self.date_entry.place(relx=0.29, rely=0.290, height=30, relwidth=0.331)
        self.date_entry.configure(background="white")
        self.date_entry.configure(disabledforeground="#a3a3a3")
        self.date_entry.configure(font="TkFixedFont")
        self.date_entry.configure(foreground="#000000")
        self.date_entry.configure(insertbackground="black")

        self.counter_entry = tk.Entry(top)
        self.counter_entry.place(relx=0.29, rely=0.240, height=30
                                 , relwidth=0.331)
        self.counter_entry.configure(background="white")
        self.counter_entry.configure(disabledforeground="#a3a3a3")
        self.counter_entry.configure(font="TkFixedFont")
        self.counter_entry.configure(foreground="#000000")
        self.counter_entry.configure(highlightbackground="#d9d9d9")
        self.counter_entry.configure(highlightcolor="black")
        self.counter_entry.configure(insertbackground="black")
        self.counter_entry.configure(selectbackground="#c4c4c4")
        self.counter_entry.configure(selectforeground="black")

        self.next_service_entry = tk.Entry(top)
        self.next_service_entry.place(relx=0.29, rely=0.343, height=30, relwidth=0.331)
        self.next_service_entry.configure(background="white")
        self.next_service_entry.configure(disabledforeground="#a3a3a3")
        self.next_service_entry.configure(font="TkFixedFont")
        self.next_service_entry.configure(foreground="#000000")
        self.next_service_entry.configure(highlightbackground="#d9d9d9")
        self.next_service_entry.configure(highlightcolor="black")
        self.next_service_entry.configure(insertbackground="black")
        self.next_service_entry.configure(selectbackground="#c4c4c4")
        self.next_service_entry.configure(selectforeground="black")

        self.notes_scrolledtext = ScrolledText(top)
        self.notes_scrolledtext.place(relx=0.025, rely=0.626, relheight=0.273
                                      , relwidth=0.941)
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

        self.purpose_combobox = ttk.Combobox(top)
        self.purpose_combobox.place(relx=0.29, rely=0.394, relheight=0.043, relwidth=0.500)

        self.purpose_combobox.configure(values=self.purpose_list)
        # self.purpose_combobox.configure(textvariable=edit_service_window_support.combobox)
        self.purpose_combobox.configure(takefocus="")

        self.add_to_service_data_btn1 = tk.Button(top)
        self.add_to_service_data_btn1.place(relx=0.810, rely=0.394, height=30, relwidth=0.060)
        self.add_to_service_data_btn1.configure(background="#006291")
        self.add_to_service_data_img1 = PhotoImage(file="icons/add_to_service_data1.png")
        self.add_to_service_data_btn1.configure(image=self.add_to_service_data_img1)
        self.add_to_service_data_btn1.configure(command=lambda: (self.add_to_service_data("Σκοπός")))

        self.actions_combobox = ttk.Combobox(top)
        self.actions_combobox.place(relx=0.29, rely=0.444, relheight=0.043, relwidth=0.500)
        self.actions_combobox.configure(values=self.actions_list)
        # self.actions_combobox.configure(textvariable=edit_service_window_support.combobox)
        self.actions_combobox.configure(takefocus="")

        self.add_to_service_data_btn2 = tk.Button(top)
        self.add_to_service_data_btn2.place(relx=0.810, rely=0.444, height=30, relwidth=0.060)
        self.add_to_service_data_btn2.configure(background="#006291")
        self.add_to_service_data_img2 = PhotoImage(file="icons/add_to_service_data2.png")
        self.add_to_service_data_btn2.configure(image=self.add_to_service_data_img2)
        self.add_to_service_data_btn2.configure(command=lambda: (self.add_to_service_data("Ενέργειες")))

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.025, rely=0.020, height=31, relwidth=0.938)
        self.Label2.configure(background="#006291")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(relief="groove")
        self.Label2.configure(text='''Προσθήκη ιστορικού''')
        self.edit()


    def quit(self, event):
        w.destroy()

    def add_to_service_data(self, column):
        # self.purpose_list, self.actions_list
        # self.purpose_combobox.get(), self.actions_combobox.get()
        if column == "Σκοπός":
            if self.purpose_combobox.get() != "" and self.purpose_combobox.get() in self.purpose_list:
                w.focus()
                messagebox.showinfo("Προσοχή", f"Το {self.purpose_combobox.get()} υπάρχει στην λίστα")
                self.top.focus()
                return None
            elif self.purpose_combobox.get() != "":
                self.purpose_list.append(self.purpose_combobox.get())
                self.purpose_combobox.configure(values=self.purpose_list)
                conn = sqlite3.connect(dbase)
                cursor = conn.cursor()
                # "INSERT INTO  " + table + "(" + culumns + ")" + "VALUES(NULL, ?, ?, ?, ?, ?, ?, ?);"
                # INSERT INTO artists (name)VALUES('Bud Powell');
                sql = "INSERT INTO Service_data (Σκοπός)VALUES(?);"
                cursor.execute(sql, (self.purpose_combobox.get(),))
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Info", f"Ο σκοπός {self.purpose_combobox.get()} προστέθηκε επιτυχώς")
                self.top.focus()
        elif column == "Ενέργειες":
            if self.actions_combobox.get() != "" and self.actions_combobox.get() in self.actions_list:
                messagebox.showinfo("Προσοχή", f"Το {self.actions_combobox.get()} υπάρχει στην λίστα")
                self.top.focus()
                return None
            elif self.actions_combobox.get() != "":
                self.actions_list.append(self.actions_combobox.get())
                self.actions_combobox.configure(values=self.actions_list)
                conn = sqlite3.connect(dbase)
                cursor = conn.cursor()
                sql = "INSERT INTO Service_data(Ενέργειες)VALUES(?);"
                cursor.execute(sql, (self.actions_combobox.get(),))
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Info", f"H ενέργεια {self.actions_combobox.get()} Προστέθηκε επιτυχώς")
                self.top.focus()

    # επεξεργασία δεδομένων
    def edit(self):
        # Εμφάνηση πελάτη
        # Πρώτα πρέπει να πάρουμε το Πελάτη_ID απο το φωτοτυπικό
        # Δευτερον το όνομα φωτοτυπικού ==> Εταιρεία (στην βαση)
        conn = sqlite3.connect(dbase)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Φωτοτυπικά WHERE ID = ?", (self.selected_copier_id,))
        selected_copier_data = cursor.fetchall()
        cursor.close()
        conn.close()
        customer_id = selected_copier_data[0][5]
        conn = sqlite3.connect(dbase)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Πελάτες WHERE ID = ?", (customer_id,))
        curtomer_data = cursor.fetchall()
        cursor.close()
        conn.close()
        # Εμφάνιση πελάτη
        self.customer_label = tk.Label(w)
        self.customer_label.place(relx=0.025, rely=0.100, height=25, relwidth=0.938)
        self.customer_label.configure(activebackground="#f9f9f9")
        self.customer_label.configure(background="brown")
        self.customer_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.customer_label.configure(foreground="#ffffff")
        self.customer_label.configure(relief="groove")
        self.customer_label.configure(text=curtomer_data[0][1])

        # Εμφάνιση Φωτοτυπικού
        self.selected_copier_label = tk.Label(w)
        self.selected_copier_label.place(relx=0.025, rely=0.150, height=25, relwidth=0.938)
        self.selected_copier_label.configure(activebackground="#f9f9f9")
        self.selected_copier_label.configure(background="#808000")
        self.selected_copier_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.selected_copier_label.configure(foreground="#ffffff")
        self.selected_copier_label.configure(relief="groove")
        self.selected_copier_label.configure(text=selected_copier_data[0][1])

        edit_conn = sqlite3.connect(dbase)
        edit_corsor = edit_conn.cursor()
        edit_corsor.execute("SELECT * FROM Service")
        self.culumns = list(map(lambda x: x[0], edit_corsor.description))
        edit_corsor.close()
        edit_conn.close()

        today = datetime.today().strftime("%d/%m/%Y")
        date = StringVar(w, value=today)
        self.date_entry.configure(textvariable=date)
        purpose_combobox = StringVar()
        self.purpose_combobox.set(purpose_combobox.get())
        action = StringVar()
        self.actions_combobox.set(action.get())
        notes = StringVar()
        self.notes_scrolledtext.insert('1.0', notes.get())
        counter = StringVar()
        self.counter_entry.configure(textvariable=counter)
        next_service = StringVar()
        self.next_service_entry.configure(textvariable=next_service)

        # Προσθήκη αλλαγών στην βαση δεδομένων
        def add_to_db():
            edited_culumns = ",".join(self.culumns)
            values_var = []
            for head in self.culumns:
                if head == "ID":
                    values_var.append("null")
                else:
                    values_var.append('?')
            values = ",".join(values_var)

            data_to_add = [date.get(), self.purpose_combobox.get(), self.actions_combobox.get(),
                           self.notes_scrolledtext.get("1.0", "end-1c"), counter.get(), next_service.get(),
                           self.selected_copier_id]
            add_conn = sqlite3.connect(dbase)
            add_cursor = add_conn.cursor()
            # ΒΑΖΟΥΜΕ ΤΟ ΠΡΩΤΟ NULL ΓΙΑ ΝΑ ΠΆΡΕΙ ΜΟΝΟ ΤΟΥ ΤΟ ID = PRIMARY KEY
            # οταν έχουμε null δεν ορίζουμε τιμή δλδ τα values ειναι +1 περισσότερα απο τα data_to_add
            # H ΣΥΝΤΑΞΗ ΕΙΝΑΙ ΑΥΤΉ
            # INSERT INTO table(column1, column2,..)VALUES(value1, value2, ...);  TA  VALUES πρεπει να είναι tuple
            # sql_insert = "INSERT INTO  " + table + "(" + culumns + ")" + "VALUES(NULL, ?, ?, ?, ?, ?, ?, ?);"
            # values είναι πόσα ? να έχει ανάλογα τα culumns
            sql_insert = "INSERT INTO  Service  (" + edited_culumns + ")" + "VALUES(" + values + ");"
            add_cursor.execute(sql_insert, tuple(data_to_add))
            add_conn.commit()
            add_conn.close()
            w.destroy()
            messagebox.showinfo('Επιτυχής ενημέρωση', "Το ιστορικό συντήρησης του φωτοτυπικού "
                                                      "{} στον πελάτη {} ενημερώθηκε ".format(
                selected_copier_data[0][1], curtomer_data[0][1]))

        self.save_btn = tk.Button(w)
        self.save_btn.place(relx=0.296, rely=0.934, height=34, width=147)
        self.save_btn.configure(activebackground="#ececec")
        self.save_btn.configure(activeforeground="#000000")
        self.save_btn.configure(background="#808000")
        self.save_btn.configure(disabledforeground="#a3a3a3")
        self.save_btn.configure(font=("Calibri", 10, "bold"))
        self.save_btn.configure(foreground="#ffffff")
        self.save_btn.configure(highlightbackground="#d9d9d9")
        self.save_btn.configure(highlightcolor="black")
        self.save_btn.configure(pady="2")
        self.save_btn.configure(text="Αποθήκευση")
        self.save_btn.configure(command=add_to_db)


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
