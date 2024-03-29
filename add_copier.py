#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 22, 2019 12:31:44 AM EET  platform: Windows NT
import platform
import add_copier_support
import sys
from tkinter import PhotoImage, messagebox, StringVar
import sqlite3
from settings import dbase, demo, root_logger  # settings

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


# Να πάρουμε Εταιρεία και μοντέλο φωτοτυπικού
def get_copiers_data():
    company_list = []
    model_list = []
    customers_list = []
    conn = sqlite3.connect(dbase)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Companies")
    copiers_data = cursor.fetchall()
    for n in range(len(copiers_data)):
        if copiers_data[n][1] != "" and copiers_data[n][1] is not None:
            company_list.append(copiers_data[n][1])
        if copiers_data[n][2] != "" and copiers_data[n][2] is not None:
            model_list.append(copiers_data[n][2])

    cursor.execute("SELECT * FROM Πελάτες")
    customers = cursor.fetchall()
    for n in range(len(customers)):
        if customers[n][1] != "" and customers[n][1] is not None:
            customers_list.append(customers[n][1])
    cursor.close()
    conn.close()

    return sorted(company_list), sorted(model_list), sorted(customers_list)


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    add_copier_support.set_Tk_var()
    top = add_copier_window(root)
    add_copier_support.init(root, top)
    root.mainloop()


w = None
customer_id = None
rt = None


def create_add_copier_window(root, *args, **kwargs):
    """Starting point when module is imported by another program."""
    global w, w_win, rt, customer_id
    rt = root

    try:
        customer_id = args[0]  # Αν έχουμε επιλέξει πελάτη
    except IndexError:
        customer_id = 0
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

        self.company_list, self.model_list, self.customers_list = get_copiers_data()
        self.customer_id = customer_id
        self.top = top
        top.geometry("505x524+444+228")
        top.minsize(120, 1)
        top.maxsize(2604, 2881)
        top.resizable(1, 1)
        top.title("Προσθήκη μηχανήματος")
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
        self.Label2.configure(text='''Προσθήκη μηχανήματος''')

        self.company_label = tk.Label(top)
        self.company_label.place(relx=0.025, rely=0.095, height=31, relwidth=0.230)
        self.company_label.configure(activebackground="#f9f9f9")
        self.company_label.configure(activeforeground="black")
        self.company_label.configure(background="#6b6b6b")
        self.company_label.configure(disabledforeground="#a3a3a3")
        self.company_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.company_label.configure(foreground="#ffffff")
        self.company_label.configure(highlightbackground="#d9d9d9")
        self.company_label.configure(highlightcolor="black")
        self.company_label.configure(relief="groove")
        self.company_label.configure(text='''Εταιρεία''')
        self.company_combobox = ttk.Combobox(top)
        self.company_combobox.place(relx=0.27, rely=0.095, relheight=0.059, relwidth=0.593)
        self.company_combobox.configure(values=self.company_list)
        self.company_combobox.configure(takefocus="")
        self.company_combobox.bind('<<ComboboxSelected>>', self.company_callback)

        self.model_label = tk.Label(top)
        self.model_label.place(relx=0.025, rely=0.172, height=29, relwidth=0.230)
        self.model_label.configure(background="#6b6b6b")
        self.model_label.configure(disabledforeground="#a3a3a3")
        self.model_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.model_label.configure(foreground="#ffffff")
        self.model_label.configure(relief="groove")
        self.model_label.configure(text='''Μοντέλο''')
        self.model_combobox = ttk.Combobox(top)
        self.model_combobox.place(relx=0.27, rely=0.172, relheight=0.053, relwidth=0.593)
        self.model_combobox.configure(values=self.model_list)
        self.model_combobox.configure(takefocus="")

        self.serial_label = tk.Label(top)
        self.serial_label.place(relx=0.025, rely=0.248, height=31, relwidth=0.230)
        self.serial_label.configure(activebackground="#f9f9f9")
        self.serial_label.configure(activeforeground="black")
        self.serial_label.configure(background="#6b6b6b")
        self.serial_label.configure(disabledforeground="#a3a3a3")
        self.serial_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.serial_label.configure(foreground="#ffffff")
        self.serial_label.configure(highlightbackground="#d9d9d9")
        self.serial_label.configure(highlightcolor="black")
        self.serial_label.configure(relief="groove")
        self.serial_label.configure(text='''Serial''')
        self.serial = StringVar()
        self.serial.trace('w', self.check_serial)
        self.serial_entry = tk.Entry(top)
        self.serial_entry.place(relx=0.27, rely=0.248, height=30, relwidth=0.593)
        self.serial_entry.configure(textvariable=self.serial)
        self.serial_entry.configure(background="white")
        self.serial_entry.configure(disabledforeground="#a3a3a3")
        self.serial_entry.configure(font="TkFixedFont")
        self.serial_entry.configure(foreground="#000000")
        self.serial_entry.configure(highlightbackground="#d9d9d9")
        self.serial_entry.configure(highlightcolor="black")
        self.serial_entry.configure(insertbackground="black")
        self.serial_entry.configure(selectbackground="#c4c4c4")
        self.serial_entry.configure(selectforeground="black")
        self.serial_warning = ttk.Label(top)
        self.serial_warning_img = PhotoImage(file="icons/lamp.png")
        self.serial_warning.configure(background="#f6f6ee")
        self.serial_warning.configure(image=self.serial_warning_img)
        self.serial_warning.configure(compound='top')

        self.start_label = tk.Label(top)
        self.start_label.place(relx=0.025, rely=0.324, height=31, relwidth=0.230)
        self.start_label.configure(activebackground="#f9f9f9")
        self.start_label.configure(activeforeground="black")
        self.start_label.configure(background="#6b6b6b")
        self.start_label.configure(disabledforeground="#a3a3a3")
        self.start_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.start_label.configure(foreground="#ffffff")
        self.start_label.configure(highlightbackground="#d9d9d9")
        self.start_label.configure(highlightcolor="black")
        self.start_label.configure(relief="groove")
        self.start_label.configure(text='''Εναρξη''')
        self.start = StringVar()
        self.start_entry = tk.Entry(top)
        self.start_entry.place(relx=0.27, rely=0.324, height=30, relwidth=0.593)
        self.start_entry.configure(textvariable=self.start)
        self.start_entry.configure(background="white")
        self.start_entry.configure(disabledforeground="#a3a3a3")
        self.start_entry.configure(font="TkFixedFont")
        self.start_entry.configure(foreground="#000000")
        self.start_entry.configure(insertbackground="black")

        self.start_counter_label = tk.Label(top)
        self.start_counter_label.place(relx=0.025, rely=0.401, height=31, relwidth=0.230)
        self.start_counter_label.configure(activebackground="#f9f9f9")
        self.start_counter_label.configure(activeforeground="black")
        self.start_counter_label.configure(background="#6b6b6b")
        self.start_counter_label.configure(disabledforeground="#a3a3a3")
        self.start_counter_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.start_counter_label.configure(foreground="#ffffff")
        self.start_counter_label.configure(highlightbackground="#d9d9d9")
        self.start_counter_label.configure(highlightcolor="black")
        self.start_counter_label.configure(relief="groove")
        self.start_counter_label.configure(text='''Μετρητής έναρξης''')
        self.start_counter = StringVar()
        self.start_counter_entry = tk.Entry(top)
        self.start_counter_entry.place(relx=0.27, rely=0.401, height=30, relwidth=0.593)
        self.start_counter_entry.configure(textvariable=self.start_counter)
        self.start_counter_entry.configure(background="white")
        self.start_counter_entry.configure(disabledforeground="#a3a3a3")
        self.start_counter_entry.configure(font="TkFixedFont")
        self.start_counter_entry.configure(foreground="#000000")
        self.start_counter_entry.configure(insertbackground="black")

        self.customer_label = tk.Label(top)
        self.customer_label.place(relx=0.025, rely=0.477, height=31, relwidth=0.230)
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
        self.customer = StringVar()
        self.customer_combobox = ttk.Combobox(top)
        self.customer_combobox.place(relx=0.27, rely=0.477, relheight=0.057, relwidth=0.593)
        # self.purpose_combobox.configure(textvariable=edit_service_window_support.combobox)
        self.customer_combobox.configure(takefocus="")
        self.customer_combobox.configure(state="readonly")


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


        self.get_customer()

        self.save_btn = tk.Button(top)
        self.save_btn.place(relx=0.296, rely=0.916, height=34, width=147)
        self.save_btn.configure(activebackground="#ececec")
        self.save_btn.configure(activeforeground="#000000")
        self.save_btn.configure(background="#4f8c23")
        self.save_btn.configure(disabledforeground="#a3a3a3")
        self.save_btn.configure(font="-family {Calibri} -size 11 -weight bold")
        self.save_btn.configure(foreground="#ffffff")
        self.save_btn.configure(highlightbackground="#d9d9d9")
        self.save_btn.configure(highlightcolor="black")
        self.save_btn.configure(pady="0")
        self.save_btn.configure(text='''Αποθήκευση''')
        self.save_btn.configure(command=self.add_copier)

        self.add_copier_company_btn = tk.Button(top)
        self.add_copier_company_btn.place(relx=0.885, rely=0.095, height=30, relwidth=0.060)
        self.add_copier_company_btn.configure(background="#006291")
        self.add_copier_company_btn_img1 = PhotoImage(file="icons/add_to_service_data1.png")
        self.add_copier_company_btn.configure(image=self.add_copier_company_btn_img1)
        self.add_copier_company_btn.configure(command=lambda: (self.add_company("Eταιρεία")))

        self.add_model_btn = tk.Button(top)
        self.add_model_btn.place(relx=0.885, rely=0.172, height=30, relwidth=0.060)
        self.add_model_btn.configure(background="#006291")
        self.add_model_img = PhotoImage(file="icons/add_to_service_data2.png")
        self.add_model_btn.configure(image=self.add_model_img)
        self.add_model_btn.configure(command=lambda: (self.add_company("Μοντέλο")))

    def company_callback(self, event=None):
        pass
        # print("File add_copier.py Line 323 Επιλεγμένη εταιρεία", self.company_combobox.get())

    def get_customer(self):
        if self.customer_id:
            con = sqlite3.connect(dbase)
            cur = con.cursor()
            cur.execute("SELECT Επωνυμία_Επιχείρησης FROM Πελάτες WHERE ID =?", (self.customer_id,))
            data = cur.fetchall()
            customer_name = data[0][0]
            self.customer = StringVar(w, value=customer_name)
            self.customer_combobox.set(value=self.customer.get())
        else:
            self.customer_combobox.configure(values=self.customers_list)

    def quit(self, event):
        rt.focus()
        self.top.destroy()

    def add_company(self, company):
        if company == "Eταιρεία":
            if self.company_combobox.get() != "" and self.company_combobox.get() in self.company_list:
                messagebox.showinfo("Προσοχή", f"Το {self.company_combobox.get()} υπάρχει στην λίστα")
                self.top.focus()
                return None
            elif self.company_combobox.get() != "":
                self.company_list.append(self.company_combobox.get())
                self.company_combobox.configure(values=self.company_list)
                conn = sqlite3.connect(dbase)
                cursor = conn.cursor()
                # "INSERT INTO  " + table + "(" + culumns + ")" + "VALUES(NULL, ?, ?, ?, ?, ?, ?, ?);"
                # INSERT INTO artists (name)VALUES('Bud Powell');
                sql = "INSERT INTO Companies (Εταιρεία)VALUES(?);"
                cursor.execute(sql, (self.company_combobox.get(),))
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Info", f"H εταιρεία {self.company_combobox.get()} προστέθηκε επιτυχώς")
                self.top.focus()
        elif company == "Μοντέλο":
            if self.model_combobox.get() != "" and self.model_combobox.get() in self.model_list:
                messagebox.showinfo("Προσοχή", f"Το {self.model_combobox.get()} υπάρχει στην λίστα")
                self.top.focus()
                return None
            elif self.model_combobox.get() != "":
                self.model_list.append(self.model_combobox.get())
                self.model_combobox.configure(values=self.model_list)
                conn = sqlite3.connect(dbase)
                cursor = conn.cursor()
                sql = "INSERT INTO Companies(Μοντέλο)VALUES(?);"
                cursor.execute(sql, (self.model_combobox.get(),))
                conn.commit()
                cursor.close()
                conn.close()
                messagebox.showinfo("Info", f"Το μοντέλο {self.model_combobox.get()} Προστέθηκε επιτυχώς")
                self.top.focus()

    def add_copier(self):

        # Demo
        if demo:
            con = sqlite3.connect(dbase)
            c = con.cursor()
            c.execute("SELECT *  FROM Φωτοτυπικά ;")
            copiers = c.fetchall()
            c.close()
            con.close()
            if len(copiers) > 5:
                messagebox.showerror("Demo",
                                    "Λυπούμαστε η εκδοση αυτή είναι demo και δεν μπορείτε να προσθέσεται νέα μηχανήματα")

                self.top.focus()
                return

        # πρέπει πρώτα να πάρουμε το  ID του πελάτη για να το ορίσουμε στο φωτοτυπικό
        conn = sqlite3.connect(dbase)
        cursor = conn.cursor()
        cursor.execute("SELECT ID FROM Πελάτες WHERE Επωνυμία_Επιχείρησης =?", (self.customer_combobox.get(),))

        customer_id = cursor.fetchall()

        # Δημιουργία culumns για τα φωτοτυπικά
        cursor.execute("SELECT * FROM Φωτοτυπικά")
        headers = list(map(lambda x: x[0], cursor.description))
        culumns = ", ".join(headers)
        values = []
        for head in headers:
            if head == "ID" or head == "id" or head == "Id":
                values.append("Null")
            else:
                values.append("?")
        values = ", ".join(values)

        # Ελεγχος αν εχουμε σημπληρώσει τα απαρέτητα πεδία
        if self.company_combobox.get() == "" or self.model_combobox.get() == "" or self.serial.get() == "":
            messagebox.showwarning("Προσοχή", "Παρακαλώ Επιλέξτε \n1.Eταιρεία, \n2.Mοντέλο "
                                              "\n3.Eισάγεται σειριακό αριθμό \n4.Επιλέξτε πελάτη")
            self.top.focus()
            return
        try:
            data = [self.company_combobox.get() + " " + self.model_combobox.get(), self.serial.get().replace(" ", "_"),
                    self.start.get(), self.start_counter.get(), customer_id[0][0],
                    self.notes_scrolledtext.get('1.0', 'end-1c'), 1]  # Το 1 είναι ενεργό φωτοτυπικό 0 ανενεργό

        except IndexError as error:  # βγάζει error το customer_id[0][0] αν δεν επιλεξουμε πελάτη
            messagebox.showwarning("Προσοχή", "Παρακαλώ \n4.Επιλέξτε πελάτη")
            self.top.focus()
            return

        sql_insert = "INSERT INTO Φωτοτυπικά (" + culumns + ")" + "VALUES(" + values + ");"

        try:
            cursor.execute(sql_insert, tuple(data))
        except sqlite3.IntegrityError as error:
            messagebox.showerror("Σφάλμα", f"{error}\n\nΟ σειριακός αριθμος {self.serial.get()} υπάρχει")
            self.top.focus()
            return
        conn.commit()
        conn.close()
        messagebox.showinfo("Info", f"Το  {data[0]} προστέθηκε επιτυχώς στον πελάτη {self.customer_combobox.get()}")
        rt.focus()
        self.top.destroy()

    # Ελεγχος αν το τηλ υπάρχει
    def check_serial(self, name, index, mode):
        self.serial_warning.place_forget()
        all_serials = []
        con = sqlite3.connect(dbase)
        c = con.cursor()
        c.execute("SELECT Serial FROM Φωτοτυπικά;")
        serials = c.fetchall()
        con.close()

        for serial in serials:
            all_serials.append(serial[0].replace(" ", "_"))

        if self.serial_entry.get().replace(" ", "_") in all_serials:
            self.serial_entry.configure(foreground="red")
            # self.serial_entry.place(relx=0.27, rely=0.248, height=30, relwidth=0.593)
            self.serial_warning.place(relx=0.885, rely=0.248, relheight=0.060, relwidth=0.060)
        else:
            self.serial_entry.configure(foreground="green")
            self.serial_warning.place_forget()


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
