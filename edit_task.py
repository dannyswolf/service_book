#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 22, 2019 12:31:44 AM EET  platform: Windows NT


import sys
from tkinter import PhotoImage, messagebox, StringVar, IntVar
import sqlite3
import os
import logging
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

import add_copier_support

# -------------ΔΗΜΗΟΥΡΓΕΙΑ LOG FILE------------------
today = datetime.today().strftime("%d %m %Y")
log_dir = "logs" + "\\" + today + "\\"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
else:
    pass

log_file_name = "Service Book " + datetime.now().strftime("%d %m %Y") + ".log"
log_file = os.path.join(log_dir, log_file_name)

# log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)  # or whatever
handler = logging.FileHandler(log_file, 'a', 'utf-8')  # or whatever
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # or whatever
handler.setFormatter(formatter)  # Pass handler as a parameter, not assign
root_logger.addHandler(handler)
sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info





def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    add_copier_support.set_Tk_var()
    top = edit_task_window(root)
    add_copier_support.init(root, top)
    root.mainloop()


w = None

selected_calendar_id = None


def create_edit_task_window(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt, selected_calendar_id
    rt = root
    w = tk.Toplevel(root)
    selected_calendar_id = args[0]
    add_copier_support.set_Tk_var()
    top = edit_task_window(w)
    add_copier_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_edit_task_window():
    global w
    w.destroy()
    w = None


class edit_task_window:
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

        # self.company_list, self.model_list, self.customers_list = get_copiers_data()
        self.selected_calendar_id = selected_calendar_id

        self.customer_id = ""
        self.copiers = []  # Τα φωτοτυπικά του επιλεγμένου πελάτη
        self.selected_copier = ""  # το επιλεγμένο φωτοτυπικό
        self.selected_serial = ""
        self.copier_id = ""
        self.urgent = ""
        self.columns = None
        self.top = top
        top.geometry("505x524+444+228")
        top.minsize(120, 1)
        top.maxsize(1604, 881)
        top.resizable(1, 1)
        top.title("Επεξεργασία εργασίας")
        top.configure(background="#f6f6ee")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.bind('<Escape>', self.quit)
        top.focus()

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
        self.Label2.configure(text='''Επεξεργασία εγρασίας''')

        self.date_label = tk.Label(top)
        self.date_label.place(relx=0.025, rely=0.095, height=31, relwidth=0.230)
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
        self.today = datetime.today().strftime("%d/%m/%Y")
        self.date = StringVar(self.top, value=today)
        self.start_date_entry = tk.Entry(top)
        self.start_date_entry.place(relx=0.27, rely=0.095, height=31, relwidth=0.593)
        self.start_date_entry.configure(textvariable=self.date)
        self.start_date_entry.configure(background="white")
        self.start_date_entry.configure(disabledforeground="#a3a3a3")
        self.start_date_entry.configure(font="TkFixedFont")
        self.start_date_entry.configure(foreground="#000000")
        self.start_date_entry.configure(insertbackground="black")
        self.start_date_entry.configure(state="readonly")

        self.customer_label = tk.Label(top)
        self.customer_label.place(relx=0.025, rely=0.172, height=29, relwidth=0.230)
        self.customer_label.configure(activebackground="#f9f9f9")
        self.customer_label.configure(activeforeground="black")
        self.customer_label.configure(background="#6b6b6b")
        self.customer_label.configure(disabledforeground="#a3a3a3")
        self.customer_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.customer_label.configure(foreground="#ffffff")
        self.customer_label.configure(highlightbackground="#d9d9d9")
        self.customer_label.configure(highlightcolor="black")
        self.customer_label.configure(relief="groove")
        self.customer_label.configure(text='''Πελάτης''')
        self.customer_combobox = ttk.Combobox(top)
        self.customer_combobox.place(relx=0.27, rely=0.172, relheight=0.057, relwidth=0.593)
        self.customer_combobox.configure(takefocus="")
        self.customer_combobox.configure(state="readonly")

        self.customer_copiers_label = tk.Label(top)
        self.customer_copiers_label.place(relx=0.025, rely=0.248, height=31, relwidth=0.230)
        self.customer_copiers_label.configure(activebackground="#f9f9f9")
        self.customer_copiers_label.configure(activeforeground="black")
        self.customer_copiers_label.configure(background="#6b6b6b")
        self.customer_copiers_label.configure(disabledforeground="#a3a3a3")
        self.customer_copiers_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.customer_copiers_label.configure(foreground="#ffffff")
        self.customer_copiers_label.configure(highlightbackground="#d9d9d9")
        self.customer_copiers_label.configure(highlightcolor="black")
        self.customer_copiers_label.configure(relief="groove")
        self.customer_copiers_label.configure(text='''Φωτοτυπικό''')
        self.copiers_combobox = ttk.Combobox(top)
        self.copiers_combobox.place(relx=0.27, rely=0.248, relheight=0.057, relwidth=0.593)
        self.copiers_combobox.configure(values="")
        self.copiers_combobox.configure(takefocus="")
        self.copiers_combobox.configure(state="readonly")

        self.purpose_label = tk.Label(top)
        self.purpose_label.place(relx=0.025, rely=0.324, height=31, relwidth=0.230)
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
        # self.purpose = StringVar()
        self.purpose_entry = tk.Entry(top)
        self.purpose_entry.place(relx=0.27, rely=0.324, height=30, relwidth=0.593)
        # self.purpose_entry.configure(textvariable=self.purpose)
        self.purpose_entry.configure(background="white")
        self.purpose_entry.configure(disabledforeground="#a3a3a3")
        self.purpose_entry.configure(font="TkFixedFont")
        self.purpose_entry.configure(foreground="#000000")
        self.purpose_entry.configure(insertbackground="black")

        self.technician_label = tk.Label(top)
        self.technician_label.place(relx=0.025, rely=0.401, height=31, relwidth=0.230)
        self.technician_label.configure(activebackground="#f9f9f9")
        self.technician_label.configure(activeforeground="black")
        self.technician_label.configure(background="#6b6b6b")
        self.technician_label.configure(disabledforeground="#a3a3a3")
        self.technician_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.technician_label.configure(foreground="#ffffff")
        self.technician_label.configure(highlightbackground="#d9d9d9")
        self.technician_label.configure(highlightcolor="black")
        self.technician_label.configure(relief="groove")
        self.technician_label.configure(text='''Τεχνικός''')
        self.technician = StringVar()
        self.technician_entry = tk.Entry(top)
        self.technician_entry.place(relx=0.27, rely=0.401, height=30, relwidth=0.593)
        self.technician_entry.configure(textvariable=self.technician)
        self.technician_entry.configure(background="white")
        self.technician_entry.configure(disabledforeground="#a3a3a3")
        self.technician_entry.configure(font="TkFixedFont")
        self.technician_entry.configure(foreground="#000000")
        self.technician_entry.configure(insertbackground="black")

        self.compl_date_label = tk.Label(top)
        self.compl_date_label.place(relx=0.025, rely=0.477, height=31, relwidth=0.230)
        self.compl_date_label.configure(activebackground="#f9f9f9")
        self.compl_date_label.configure(activeforeground="black")
        self.compl_date_label.configure(background="#6b6b6b")
        self.compl_date_label.configure(disabledforeground="#a3a3a3")
        self.compl_date_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.compl_date_label.configure(foreground="#ffffff")
        self.compl_date_label.configure(highlightbackground="#d9d9d9")
        self.compl_date_label.configure(highlightcolor="black")
        self.compl_date_label.configure(relief="groove")
        self.compl_date_label.configure(text='''Ημ_Ολοκλ''')
        self.compl_date_entry = tk.Entry(top)
        self.compl_date_entry.place(relx=0.27, rely=0.477, height=30, relwidth=0.593)
        self.compl_date_entry.configure(background="white")
        self.compl_date_entry.configure(disabledforeground="#a3a3a3")
        self.compl_date_entry.configure(font="TkFixedFont")
        self.compl_date_entry.configure(foreground="#000000")
        self.compl_date_entry.configure(insertbackground="black")

        self.completed_label = tk.Label(top)
        self.completed_label.place(relx=0.025, rely=0.555, height=31, relwidth=0.230)
        self.completed_label.configure(activebackground="#f9f9f9")
        self.completed_label.configure(activeforeground="black")
        self.completed_label.configure(background="#6b6b6b")
        self.completed_label.configure(disabledforeground="#a3a3a3")
        self.completed_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.completed_label.configure(foreground="#ffffff")
        self.completed_label.configure(highlightbackground="#d9d9d9")
        self.completed_label.configure(highlightcolor="black")
        self.completed_label.configure(relief="groove")
        self.completed_label.configure(text='''Ολοκληρώθηκε;''')
        self.completed_var = IntVar()
        self.completed_Checkbutton1 = tk.Checkbutton(top)
        self.completed_Checkbutton1.place(relx=0.27, rely=0.555, height=31, relwidth=0.102)
        self.completed_Checkbutton1.configure(activebackground="#ececec")
        self.completed_Checkbutton1.configure(activeforeground="#000000")
        self.completed_Checkbutton1.configure(background="#6b6b6b")
        self.completed_Checkbutton1.configure(foreground="#000000")
        self.completed_Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.completed_Checkbutton1.configure(highlightcolor="black")
        self.completed_Checkbutton1.configure(justify='left')
        self.completed_Checkbutton1.configure(text='''Ναι''')
        self.completed_Checkbutton1.configure(variable=self.completed_var)

        self.dte_label = tk.Label(top)
        self.dte_label.place(relx=0.450, rely=0.555, height=31, relwidth=0.230)
        self.dte_label.configure(activebackground="#f9f9f9")
        self.dte_label.configure(activeforeground="black")
        self.dte_label.configure(background="#6b6b6b")
        self.dte_label.configure(disabledforeground="#a3a3a3")
        self.dte_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.dte_label.configure(foreground="#ffffff")
        self.dte_label.configure(highlightbackground="#d9d9d9")
        self.dte_label.configure(highlightcolor="black")
        self.dte_label.configure(relief="groove")
        self.dte_label.configure(text='''Δελτ.Τεχν.Εξυπ.''')
        self.dte = StringVar()
        self.dte_entry = tk.Entry(top)
        self.dte_entry.place(relx=0.685, rely=0.555, height=30, relwidth=0.150)
        self.dte_entry.configure(textvariable=self.dte)
        self.dte_entry.configure(background="white")
        self.dte_entry.configure(disabledforeground="#a3a3a3")
        self.dte_entry.configure(font="TkFixedFont")
        self.dte_entry.configure(foreground="#000000")
        self.dte_entry.configure(insertbackground="black")

        self.notes_label = tk.Label(top)
        self.notes_label.place(relx=0.025, rely=0.640, height=31, relwidth=0.940)
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

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.025, rely=0.630, relwidth=0.938)

        self.notes_scrolledtext = ScrolledText(top)
        self.notes_scrolledtext.place(relx=0.025, rely=0.710, relheight=0.2, relwidth=0.941)
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
        self.notes = StringVar()

        self.get_data()

    # Να πάρουμε Δεδομένα
    def get_data(self):
        con = sqlite3.connect(dbase)
        c = con.cursor()
        c.execute("SELECT * FROM Calendar;")
        self.columns = list(map(lambda x: x[0], c.description))
        con.close()

        conn = sqlite3.connect(dbase)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Calendar WHERE ID =?", (self.selected_calendar_id,))
        data = cursor.fetchall()
        date = StringVar(self.top, value=data[0][1])
        self.start_date_entry.configure(textvariable=date)
        customer_combobox = StringVar(w, value=data[0][2])
        self.customer_combobox.set(customer_combobox.get())
        copier = StringVar(w, value=data[0][3])
        self.copiers_combobox.set(copier.get())
        purpose = StringVar(w, value=data[0][4])
        self.purpose_entry.configure(textvariable=purpose)
        technician = StringVar(w, value=data[0][5])
        self.technician_entry.configure(textvariable=technician)
        compl_date = StringVar(w, value=data[0][6])
        self.compl_date_entry.configure(textvariable=compl_date)
        urgent = StringVar(w, value=data[0][7])
        self.urgent = urgent.get()
        notes = StringVar(w, value=data[0][8])
        self.notes_scrolledtext.insert('1.0', notes.get())
        self.copier_id = data[0][9]
        dte = StringVar(w, value=data[0][10])
        self.dte_entry.configure(textvariable=dte)

        cursor.close()
        conn.close()

        def add_to_db():
            edited_columns = []
            for column in self.columns:
                if column != "ID":
                    edited_columns.append(column + "=?")
            edited_columns = ",".join(edited_columns)

            completed = self.completed_var.get()

            # Demo
            con = sqlite3.connect(dbase)
            c = con.cursor()
            c.execute("SELECT *  FROM Calendar ;")
            tasks = c.fetchall()
            c.close()
            con.close()
            if len(tasks) > 5:
                messagebox.showerror("Demo",
                                     "Λυπούμαστε η εκδοση αυτή είναι demo και δεν μπορείτε να προσθέσεται νέες εργασίες")

                self.top.focus()
                return

            conn = sqlite3.connect(dbase)
            cursor = conn.cursor()
            # Δημιουργία culumns για της εργασίες
            cursor.execute("SELECT * FROM Calendar")
            headers = list(map(lambda x: x[0], cursor.description))
            culumns = ", ".join(headers)
            values = []
            for head in headers:
                if head == "ID":
                    values.append("Null")
                else:
                    values.append("?")
            values = ", ".join(values)

            if completed:  # Αν ολοκληρόθηκε

                if len(compl_date.get()) != 10:  # Ελεγχος ημερομηνίας ολοκλήροσης
                    messagebox.showwarning("Προσοχή", "Η ημερομηνία ολοκλήρωσης πρέπει να έχει την μορφή ΄01/01/2020΄")
                    self.top.focus()
                    return

                data = [date.get(), customer_combobox.get(), copier.get(), purpose.get(), technician.get(),
                        compl_date.get(), urgent.get(), self.notes_scrolledtext.get('1.0', 'end-1c'),
                        self.copier_id, dte.get(), 0, self.selected_calendar_id]  # Το  0 => ανενεργό δλδ ολοκληρόθηκε
            else:

                data = [date.get(), customer_combobox.get(), copier.get(), purpose.get(), technician.get(),
                        compl_date.get(), urgent.get(), self.notes_scrolledtext.get('1.0', 'end-1c'),
                        self.copier_id, dte.get(), 1, self.selected_calendar_id]  # Το  1 => ενενεργό δλδ δεν ολοκληρόθηκε

            cursor.execute("UPDATE Calendar  SET " + edited_columns + " WHERE ID=? ", (tuple(data,)))
            conn.commit()
            conn.close()
            messagebox.showinfo("Info", f"H εργασία αποθηκεύτηκε επιτυχώς στον πελάτη {self.customer_combobox.get()}")
            self.top.destroy()
            return None

        self.save_btn = tk.Button(w)
        self.save_btn.place(relx=0.296, rely=0.916, height=34, width=147)
        self.save_btn.configure(activebackground="#ececec")
        self.save_btn.configure(activeforeground="#000000")
        self.save_btn.configure(background="#6b6b6b")
        self.save_btn.configure(disabledforeground="#a3a3a3")
        self.save_btn.configure(font="-family {Calibri} -size 11 -weight bold")
        self.save_btn.configure(foreground="#ffffff")
        self.save_btn.configure(highlightbackground="#d9d9d9")
        self.save_btn.configure(highlightcolor="black")
        self.save_btn.configure(pady="0")
        self.save_btn.configure(text='''Αποθήκευση''')
        self.save_btn.configure(command=add_to_db)


    def quit(self, event):
        self.top.destroy()

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
