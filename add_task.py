#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 22, 2019 12:31:44 AM EET  platform: Windows NT

import add_copier_support
import sys
from tkinter import PhotoImage, messagebox, StringVar
import sqlite3
from datetime import datetime
import mail
import add_copier
from tkcalendar import DateEntry
from settings import dbase,  root_logger, demo, today  # settings


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


# Να πάρουμε Φωτοτυπικά και πελάτη
def get_copiers_data():
    customers_list = []

    conn = sqlite3.connect(dbase)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Πελάτες WHERE Κατάσταση =1")
    customers = cursor.fetchall()
    for n in range(len(customers)):
        if customers[n][1] != "" and customers[n][1] is not None:
            customers_list.append(customers[n][1])

    cursor.execute("SELECT * FROM Φωτοτυπικά WHERE Κατάσταση = 1")
    copiers_data = cursor.fetchall()
    serials = []
    for n in range(len(copiers_data)):
        serials.append(copiers_data[n][2])

    cursor.close()
    conn.close()
    return sorted(customers_list), serials


def get_service_id():
    con = sqlite3.connect(dbase)
    cu = con.cursor()
    # Να πάρουμε πρώτα το τελευταίο ID απο τον πίνακα sqlite_sequence το πεδία Service
    # για να προσθέσουμε τις εικόνες στο νέο service
    # νεο service_ID == τελευταίο ID απο τον πίνακα Service +1
    cu.execute("SELECT * FROM sqlite_sequence")
    names = cu.fetchall()

    for name in names:
        if name[0] == "Service":
            services_ID = name[1]

            new_service_id = int(services_ID) + 1
            cu.close()
            con.close()
            return new_service_id


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
    add_copier_support.set_Tk_var()
    top = add_task_window(root)
    add_copier_support.init(root, top)
    root.mainloop()


w = None

selected_customer = ""

def create_add_task_window(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt, selected_customer
    rt = root
    selected_customer = args[0]
    w = tk.Toplevel(root)
    add_copier_support.set_Tk_var()
    top = add_task_window(w)
    add_copier_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_add_task_window():
    global w
    w.destroy()
    w = None


class add_task_window:
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
        self.customers_list, self.serials = get_copiers_data()
        self.purpose_list, self.actions_list = get_service_data()
        self.selected_customer = selected_customer  # Επιλεγμένος πελάτης απο το service_book_colors
        self.service_id = get_service_id()
        self.customer_id = ""
        self.copiers = []  # Τα φωτοτυπικά του επιλεγμένου πελάτη
        self.selected_copier = ""  # το επιλεγμένο φωτοτυπικό
        self.selected_serial = ""
        self.copier_id = ""
        self.top = top
        top.geometry("505x524+10+10")
        top.minsize(120, 1)
        top.maxsize(1604, 881)
        top.resizable(1, 1)
        top.title("Προσθήκη εργασίας")
        top.configure(background="#f6f6ee")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.bind('<Escape>', self.quit)
        top.focus()

        self.today = datetime.strptime(today, "%d %m %Y")
        self.day = self.today.day
        self.year = self.today.year
        self.month = self.today.month

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
        self.Label2.configure(text='''Προσθήκη εγρασίας''')

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


        self.start_date = DateEntry(top, width=12, year=self.year, month=self.month, day=self.day,
                             background='gray20', selectmode='day', foreground='white', borderwidth=5, locale="el_GR",
                             font=("Calibri", 10, 'bold'), date_pattern='dd/mm/yyyy')
        self.start_date.place(relx=0.27, rely=0.095, height=31, relwidth=0.593)

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
        # self.customer = StringVar()
        self.customer_combobox = ttk.Combobox(top)
        self.customer_combobox.place(relx=0.27, rely=0.172, relheight=0.057, relwidth=0.593)
        self.customer_combobox.configure(values=self.customers_list)
        self.customer_combobox.set(value=self.selected_customer)
        self.customer_combobox.configure(takefocus="")
        self.customer_combobox.bind("<<ComboboxSelected>>", self.get_copier)
        self.customer_combobox.configure(state="readonly")
        # Ανανέωση μετα απο Προσθήκη Φωτοτυπικού
        self.refresh_task_btn = tk.Button(top)
        self.refresh_task_btn.place(relx=0.880, rely=0.172, height=30, relwidth=0.060)
        self.refresh_task_btn.configure(background="#0685c4")
        self.refresh_task_img = PhotoImage(file="icons/refresh.png")
        self.refresh_task_btn.configure(image=self.refresh_task_img)
        self.refresh_task_btn.configure(command=self.get_copier)


        self.phone_label = tk.Label(top)
        self.phone_label.place(relx=0.025, rely=0.248, height=31, relwidth=0.230)
        self.phone_label.configure(activebackground="#f9f9f9")
        self.phone_label.configure(activeforeground="black")
        self.phone_label.configure(background="#6b6b6b")
        self.phone_label.configure(disabledforeground="#a3a3a3")
        self.phone_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.phone_label.configure(foreground="#ffffff")
        self.phone_label.configure(highlightbackground="#d9d9d9")
        self.phone_label.configure(highlightcolor="black")
        self.phone_label.configure(relief="groove")
        self.phone_label.configure(text='''Τηλέφωνο''')
        self.phone = ""
        self.phone_var = StringVar(w, value=self.phone)
        self.phone_entry = tk.Entry(top)
        self.phone_entry.place(relx=0.27, rely=0.248, height=31, relwidth=0.593)
        self.phone_entry.configure(background="white")
        self.phone_entry.configure(disabledforeground="#a3a3a3")
        self.phone_entry.configure(font="TkFixedFont")
        self.phone_entry.configure(foreground="#000000")
        self.phone_entry.configure(insertbackground="black")

        self.customer_copiers_label = tk.Label(top)
        self.customer_copiers_label.place(relx=0.025, rely=0.324, height=31, relwidth=0.230)
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
        self.copier_stringvar = StringVar()
        self.copiers_combobox = ttk.Combobox(top)
        self.copiers_combobox.place(relx=0.27, rely=0.324, relheight=0.057, relwidth=0.593)
        self.copiers_combobox.set(value=self.copier_stringvar.get())
        self.copiers_combobox.configure(takefocus="")
        self.copiers_combobox.bind('<<ComboboxSelected>>', self.get_copier_id)
        self.add_copier_btn1 = tk.Button(top)
        self.add_copier_btn1.place(relx=0.880, rely=0.324, height=29, relwidth=0.060)
        self.add_copier_btn1.configure(background="#006291")
        self.add_copier_btn1_img1 = PhotoImage(file="icons/add_to_service_data1.png")
        self.add_copier_btn1.configure(image=self.add_copier_btn1_img1)
        self.add_copier_btn1.configure(command=self.add_copier)



        self.purpose_label = tk.Label(top)
        self.purpose_label.place(relx=0.025, rely=0.400, height=31, relwidth=0.230)
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
        self.purpose_combobox = ttk.Combobox(top)
        self.purpose_combobox.place(relx=0.27, rely=0.400, relheight=0.057, relwidth=0.593)
        self.purpose_combobox.configure(values=self.purpose_list)
        # self.purpose_combobox.configure(textvariable=edit_service_window_support.combobox)
        self.purpose_combobox.configure(takefocus="")
        self.add_to_service_data_btn1 = tk.Button(top)
        self.add_to_service_data_btn1.place(relx=0.880, rely=0.400, height=29, relwidth=0.060)
        self.add_to_service_data_btn1.configure(background="#006291")
        self.add_to_service_data_img1 = PhotoImage(file="icons/add_to_service_data1.png")
        self.add_to_service_data_btn1.configure(image=self.add_to_service_data_img1)
        self.add_to_service_data_btn1.configure(command=lambda: (self.add_to_service_data("Σκοπός")))

        self.technician_label = tk.Label(top)
        self.technician_label.place(relx=0.025, rely=0.480, height=31, relwidth=0.230)
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
        self.technician = StringVar(top, value="Ιορδάνης")
        self.technician_entry = tk.Entry(top)
        self.technician_entry.place(relx=0.27, rely=0.480, height=30, relwidth=0.593)
        self.technician_entry.configure(textvariable=self.technician.get())
        self.technician_entry.configure(background="white")
        self.technician_entry.configure(disabledforeground="#a3a3a3")
        self.technician_entry.configure(font="TkFixedFont")
        self.technician_entry.configure(foreground="#000000")
        self.technician_entry.configure(insertbackground="black")

        self.urgent_label = tk.Label(top)
        self.urgent_label.place(relx=0.025, rely=0.553, height=31, relwidth=0.230)
        self.urgent_label.configure(activebackground="#f9f9f9")
        self.urgent_label.configure(activeforeground="black")
        self.urgent_label.configure(background="#6b6b6b")
        self.urgent_label.configure(disabledforeground="#a3a3a3")
        self.urgent_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.urgent_label.configure(foreground="#ffffff")
        self.urgent_label.configure(highlightbackground="#d9d9d9")
        self.urgent_label.configure(highlightcolor="black")
        self.urgent_label.configure(relief="groove")
        self.urgent_label.configure(text='''Επείγων''')
        self.urgent = StringVar()
        self.urgent_entry = tk.Entry(top)
        self.urgent_entry.place(relx=0.27, rely=0.553, height=30, relwidth=0.593)
        self.urgent_entry.configure(textvariable=self.urgent)
        self.urgent_entry.configure(background="white")
        self.urgent_entry.configure(disabledforeground="#a3a3a3")
        self.urgent_entry.configure(font="TkFixedFont")
        self.urgent_entry.configure(foreground="#000000")
        self.urgent_entry.configure(insertbackground="black")

        self.send_mail_btn = tk.Button(top)
        self.send_mail_btn.place(relx=0.880, rely=0.553, relheight=0.060, relwidth=0.070)
        self.send_mail_btn.configure(background="#6b6b6b")
        self.send_mail_btn_img1 = PhotoImage(file="icons/send_mail.png")
        self.send_mail_btn.configure(image=self.send_mail_btn_img1)
        self.send_mail_btn.configure(command=self.send_mail)

        self.notes_label = tk.Label(top)
        self.notes_label.place(relx=0.025, rely=0.633, height=31, relwidth=0.940)
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
        self.notes_scrolledtext.place(relx=0.025, rely=0.690, relheight=0.23, relwidth=0.941)
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
        self.save_btn.place(relx=0.296, rely=0.936, height=34, width=147)
        self.save_btn.configure(activebackground="#ececec")
        self.save_btn.configure(activeforeground="#000000")
        self.save_btn.configure(background="#339933")
        self.save_btn.configure(disabledforeground="#a3a3a3")
        self.save_btn.configure(font="-family {Calibri} -size 11 -weight bold")
        self.save_btn.configure(foreground="#ffffff")
        self.save_btn.configure(highlightbackground="#d9d9d9")
        self.save_btn.configure(highlightcolor="black")
        self.save_btn.configure(pady="0")
        self.save_btn.configure(text='''Αποθήκευση''')
        self.save_btn.configure(command=self.add_task)

        if self.selected_customer:
            self.get_copier()
            self.get_copier_id()

    def get_copier_id(self, event=None):
        self.customers_list, self.serials = get_copiers_data()
        copier = self.copiers_combobox.get()
        list_data_of_copier = copier.split()
        try:
            for serial in self.serials:
                if serial == list_data_of_copier[-1]:
                    self.selected_serial = serial
        except IndexError:  # Αν εισάγουμε μηχάνημα μόνο όνομα και όχι serial nr
            self.selected_serial = ""
        con = sqlite3.connect(dbase)
        c = con.cursor()
        c.execute("SELECT ID, Εταιρεία FROM Φωτοτυπικά WHERE Serial =?", (self.selected_serial,))
        data = c.fetchall()
        try:
            self.copier_id = data[0][0]
            self.selected_copier = data[0][1] + "  Σειριακός : " + self.selected_serial
        except IndexError:  # Αν εισάγουμε μηχάνημα μόνο όνομα και όχι serial nr
            self.copier_id = 0
            self.selected_copier = self.copiers_combobox.get() + "  Σειριακός : " + self.selected_serial
        con.close()
        return

    def get_copier(self, event=None):
        # να πάρουμε το id του πελάτη απο το ονομα του
        customer = self.customer_combobox.get()
        self.copiers_combobox.set(value="")

        con = sqlite3.connect(dbase)
        cursor = con.cursor()
        cursor.execute("SELECT ID, Τηλέφωνο, Κινητό, Διεύθυνση FROM Πελάτες WHERE  Επωνυμία_Επιχείρησης =?", (customer,))
        customer_data = cursor.fetchall()  # ==> [(4,)] αρα θέλουμε το customer_id[0][0]
        self.customer_id = customer_data[0][0]

        self.phone_var = StringVar(w, value=customer_data[0][1])
        self.phone_entry.configure(textvariable=self.phone_var)

        self.notes_scrolledtext.delete('1.0', "end")
        self.mobile = StringVar(w, value="Κινητό : " + customer_data[0][2] + "\n")
        self.notes_scrolledtext.insert("1.0", self.mobile.get())
        self.notes = StringVar(w, value="Διεύθυνση : " + customer_data[0][3] + "\n")
        self.notes_scrolledtext.insert("2.0", self.notes.get())

        self.technician = StringVar(w, value="Ιορδάνης ")
        self.technician_entry.delete(0, 'end')
        self.technician_entry.insert(0, self.technician.get())

        # Εμφάνιση φωτοτυπικών σύμφονα με το customer_id
        cursor.execute("SELECT Εταιρεία, Serial FROM Φωτοτυπικά WHERE Πελάτη_ID = ? AND Κατάσταση = 1 ", (self.customer_id,))
        copiers = cursor.fetchall()
        self.copiers = []
        for copier in copiers:
            self.copiers.append("   Σειριακός: ".join(copier))
        cursor.close()
        con.close()
        # Αν επιλέξουμε φωτοτυπικό του πελάτη απο τα περασμένα στην βάση φωτοτυπικά
        if copiers:
            self.copiers_combobox.configure(values=self.copiers)
            self.copiers_combobox.set(value=self.copiers[0])
        # Διαφορετικά μπορούμε να εισάγουμε νέο μηχάνημα
        else:
            self.copiers_combobox.configure(textvariable=self.copier_stringvar)

    def quit(self, event):
        self.top.destroy()

    def add_task(self):

        # Demo
        if demo:
            con = sqlite3.connect(dbase)
            c = con.cursor()
            c.execute("SELECT *  FROM Calendar ;")
            tasks = c.fetchall()
            c.close()
            con.close()
            if len(tasks) > 4:
                messagebox.showerror("Demo",
                                    "Λυπούμαστε η εκδοση αυτή είναι demo και δεν μπορείτε να προσθέσεται νέες εργασίες")

                self.top.focus()
                return

        self.get_copier_id()  # Να πάρουμε το id του μηχανήματος
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

        # Ελεγχος αν εχουμε σημπληρώσει τα απαρέτητα πεδία

        if self.start_date.get() == "" or self.customer_combobox.get() == "" or self.copiers_combobox.get() == "":
            messagebox.showwarning("Προσοχή", "Παρακαλώ επιλέξτε \n1.Ημερομηνία, \n2.Πελάτη "
                                              "\n3.Φωτοτυπικό")
            self.top.focus()
            return

        # τα "" είναι η ημερομηνία ολοκλήροσης και ΔΤΕ που δεν τα συμπληρώνουμε εδώ αλλα στην επεξεργασία task
        # Το 1 στο τέλος είναι κατάσταση 1=> ενεργό 0 => ανενεργό δλδ ολοκληρώθηκε
        # Δεδομένα για το Calendar
        # "" ==> Ενέργειες
        # Αν ο χρήστης εισάγει νέο μηχάνημα που δεν είναι στην βάση
        if not self.copiers_combobox.get() in self.copiers:
            self.copier_id = "0"
        # "", "", ==>> Μετρητής και Επώμενο service
        data = [self.start_date.get(), self.customer_combobox.get(), self.copiers_combobox.get(), self.purpose_combobox.get(), "",
                self.technician.get(), "", self.urgent.get(), self.phone_var.get(),
                self.notes_scrolledtext.get('1.0', 'end-1c'), self.copier_id, "", self.service_id, "", "", 1]

        sql_insert = "INSERT INTO Calendar (" + culumns + ")" + "VALUES(" + values + ");"

        cursor.execute(sql_insert, tuple(data))
        conn.commit()
        conn.close()

        # Δημιουργία culumns για το Service
        conn = sqlite3.connect(dbase)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Service")
        headers = list(map(lambda x: x[0], cursor.description))
        culumns = ", ".join(headers)
        values = []
        for head in headers:
            if head == "ID":
                values.append("Null")
            else:
                values.append("?")
        values = ", ".join(values)
        # Δεδομένα για το Service
        # CREATE TABLE "Service" (
        # 	"ID"	INTEGER PRIMARY KEY AUTOINCREMENT,   # Service_id
        # 	"Ημερομηνία"	TEXT,      # ---------------  self.start_date.get()
        # 	"Σκοπός_Επίσκεψης"	TEXT,  # ---------------  self.purpose_combobox.get()
        # 	"Ενέργειες"	TEXT,          #  ""
        # 	"Σημειώσεις"	TEXT,       # --------------  self.notes_scrolledtext.get('1.0', 'end-1c')
        # 	"Μετρητής"	TEXT,           #  ""
        # 	"Επ_Service"	TEXT,       #  ""
        # 	"Copier_ID"	INTEGER,        # -------------   self.copier_id
        # 	"ΔΤΕ"	TEXT,               # ""
        # 	FOREIGN KEY("Copier_ID") REFERENCES "Φωτοτυπικά"("ID")
        # )

        data = [self.start_date.get(), self.purpose_combobox.get(), "", self.notes_scrolledtext.get('1.0', 'end-1c'),
                "", "", self.copier_id, ""]

        sql_insert = "INSERT INTO Service (" + culumns + ")" + "VALUES(" + values + ");"

        cursor.execute(sql_insert, tuple(data))
        conn.commit()
        conn.close()
        # messagebox.showinfo("Info", f"H εργασία προστέθηκε επιτυχώς στον πελάτη {self.customer_combobox.get()}")
        self.top.destroy()
        return None

    # Αποστολή email
    def send_mail(self):
        # Αν γράψουμε νέο φωτοτυπικό και όχι απο την λίστα
        if not self.selected_copier:
            self.selected_copier = self.copiers_combobox.get()

        data = [self.start_date.get(), self.customer_combobox.get(), self.copiers_combobox.get(), self.purpose_combobox.get(),
                self.technician.get(), "", self.urgent.get(), self.phone_var.get(),
                self.notes_scrolledtext.get('1.0', 'end-1c'), self.copier_id, "", 1]
        mail.send_mail(data)

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

 # Προσθήκη Φωτοτυπικού
    def add_copier(self, event=None):
        """ Προσθήκη φωτοτυπικού
        Καλει την συνάρτηση create_Topelevel1 του αρχείου add_copier

        :return:
        """

        self.top.focus()
        add_copier.create_add_copier_window(w, self.customer_id)


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
