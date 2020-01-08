#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 18, 2019 04:44:06 PM EET  platform: Windows NT

import sys
import sqlite3
from tkinter import StringVar, messagebox
import os
import logging
from datetime import datetime

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

import enable_customers_support

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

dbase = "\\\\192.168.1.200\\Public\\DROPBOX\\ΕΓΓΡΑΦΑ\\6.  ΒΙΒΛΙΟ SERVICE\\Service_book.db"
# spare_parts_db = "\\\\192.168.1.200\\Public\\DROPBOX\\ΕΓΓΡΑΦΑ\\2.  ΑΠΟΘΗΚΗ\\3. ΚΑΙΝΟΥΡΙΑ_ΑΠΟΘΗΚΗ.db"


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    enable_customers_support.set_Tk_var()
    top = Toplevel1(root)
    enable_customers_support.init(root, top)
    root.mainloop()


def get_customers():
    con = sqlite3.connect(dbase)
    c = con.cursor()
    c.execute("SELECT * FROM Πελάτες WHERE Κατάσταση = 0")
    # customers_data -=> Ολες οι πληροφορίες των απενεργοποιημένων πελατών
    customers_data = c.fetchall()

    c.close()
    con.close()
    customers_names = []
    for name in customers_data:
        customers_names.append(name[1])

    return sorted(customers_names)


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    enable_customers_support.set_Tk_var()
    top = Toplevel1(w)
    enable_customers_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        self.customers = get_customers()

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
        self.top = top
        top.geometry("900x400+480+276")
        top.minsize(120, 1)
        top.maxsize(1604, 881)
        top.resizable(1, 1)
        top.title("Ενεργοποίηση πελάτη")
        top.configure(background="#f6f6ee")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.bind('<Escape>', self.quit)
        top.focus()

        # Επιλογή απενεργοποιημένου πελάτη
        self.select_customer_label = tk.Label(top)
        self.select_customer_label.place(relx=0.017, rely=0.146, height=30, relwidth=0.244)
        self.select_customer_label.configure(activebackground="#f9f9f9")
        self.select_customer_label.configure(activeforeground="black")
        self.select_customer_label.configure(background="#994d33")
        self.select_customer_label.configure(disabledforeground="#a3a3a3")
        self.select_customer_label.configure(foreground="white")
        self.select_customer_label.configure(highlightbackground="#d9d9d9")
        self.select_customer_label.configure(highlightcolor="black")
        self.select_customer_label.configure(relief="groove")
        self.select_customer_label.configure(text='''Επιλογή  πελάτη''')

        # Εμφάνηση απενεργοποιημένων πελατών
        self.customer_combobox = ttk.Combobox(top)
        self.customer_combobox.place(relx=0.275, rely=0.146, relheight=0.063, relwidth=0.500)
        self.customer_combobox.configure(values=self.customers)
        # self.actions_combobox.configure(textvariable=edit_service_window_support.combobox)
        self.customer_combobox.bind("<<ComboboxSelected>>", self.get_customers_data)
        self.customer_combobox.configure(takefocus="")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.017, rely=0.246, height=20, relwidth=0.244)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#84f29c")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(relief="groove")
        self.Label1.configure(text='''Επωνυμία Επιχείρησης''')

        self.company_name_entry = tk.Entry(top)
        self.company_name_entry.place(relx=0.275, rely=0.246, height=20
                                      , relwidth=0.280)
        self.company_name = StringVar()
        self.company_name_entry.configure(textvariable=self.company_name)
        self.company_name_entry.configure(background="white")
        self.company_name_entry.configure(disabledforeground="#a3a3a3")
        self.company_name_entry.configure(font="TkFixedFont")
        self.company_name_entry.configure(foreground="#000000")
        self.company_name_entry.configure(highlightbackground="#d9d9d9")
        self.company_name_entry.configure(highlightcolor="black")
        self.company_name_entry.configure(insertbackground="black")
        self.company_name_entry.configure(selectbackground="#c4c4c4")
        self.company_name_entry.configure(selectforeground="black")

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.017, rely=0.422, height=20, relwidth=0.244)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#84f29c")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(relief="groove")
        self.Label2.configure(text='''Διεύθυνση''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.017, rely=0.334, height=20, relwidth=0.244)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#84f29c")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(relief="groove")
        self.Label3.configure(text='''Ονοματεπώνυμο''')

        self.fax_entry = tk.Entry(top)
        self.fax_entry.place(relx=0.757, rely=0.597, height=20, relwidth=0.217)
        self.fax = StringVar()
        self.fax_entry.configure(textvariable=self.fax)
        self.fax_entry.configure(background="white")
        self.fax_entry.configure(disabledforeground="#a3a3a3")
        self.fax_entry.configure(font="TkFixedFont")
        self.fax_entry.configure(foreground="#000000")
        self.fax_entry.configure(highlightbackground="#d9d9d9")
        self.fax_entry.configure(highlightcolor="black")
        self.fax_entry.configure(insertbackground="black")
        self.fax_entry.configure(selectbackground="#c4c4c4")
        self.fax_entry.configure(selectforeground="black")

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.568, rely=0.246, height=21, relwidth=0.170)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#84f29c")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(relief="groove")
        self.Label4.configure(text='''Πόλη''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.568, rely=0.422, height=21, relwidth=0.170)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#84f29c")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(relief="groove")
        self.Label5.configure(text='''Ταχ. Κώδικας''')

        self.Label6 = tk.Label(top)
        self.Label6.place(relx=0.568, rely=0.334, height=21, relwidth=0.170)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#84f29c")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(relief="groove")
        self.Label6.configure(text='''Περιοχή''')

        self.name_entry = tk.Entry(top)
        self.name_entry.place(relx=0.275, rely=0.334, height=20, relwidth=0.280)
        self.name = StringVar()
        self.name_entry.configure(textvariable=self.name)
        self.name_entry.configure(background="white")
        self.name_entry.configure(disabledforeground="#a3a3a3")
        self.name_entry.configure(font="TkFixedFont")
        self.name_entry.configure(foreground="#000000")
        self.name_entry.configure(highlightbackground="#d9d9d9")
        self.name_entry.configure(highlightcolor="black")
        self.name_entry.configure(insertbackground="black")
        self.name_entry.configure(selectbackground="#c4c4c4")
        self.name_entry.configure(selectforeground="black")

        self.mobile_entry = tk.Entry(top)
        self.mobile_entry.place(relx=0.275, rely=0.597, height=20, relwidth=0.280)
        self.mobile = StringVar()
        self.mobile_entry.configure(textvariable=self.mobile)
        self.mobile_entry.configure(background="white")
        self.mobile_entry.configure(disabledforeground="#a3a3a3")
        self.mobile_entry.configure(font="TkFixedFont")
        self.mobile_entry.configure(foreground="#000000")
        self.mobile_entry.configure(highlightbackground="#d9d9d9")
        self.mobile_entry.configure(highlightcolor="black")
        self.mobile_entry.configure(insertbackground="black")
        self.mobile_entry.configure(selectbackground="#c4c4c4")
        self.mobile_entry.configure(selectforeground="black")

        self.email_entry = tk.Entry(top)
        self.email_entry.place(relx=0.757, rely=0.509, height=20, relwidth=0.217)
        self.email = StringVar()
        self.email_entry.configure(textvariable=self.email)
        self.email_entry.configure(background="white")
        self.email_entry.configure(disabledforeground="#a3a3a3")
        self.email_entry.configure(font="TkFixedFont")
        self.email_entry.configure(foreground="#000000")
        self.email_entry.configure(highlightbackground="#d9d9d9")
        self.email_entry.configure(highlightcolor="black")
        self.email_entry.configure(insertbackground="black")
        self.email_entry.configure(selectbackground="#c4c4c4")
        self.email_entry.configure(selectforeground="black")

        self.city_entry = tk.Entry(top)
        self.city_entry.place(relx=0.757, rely=0.246, height=20, relwidth=0.217)
        self.city = StringVar()
        self.city_entry.configure(textvariable=self.city)
        self.city_entry.configure(background="white")
        self.city_entry.configure(disabledforeground="#a3a3a3")
        self.city_entry.configure(font="TkFixedFont")
        self.city_entry.configure(foreground="#000000")
        self.city_entry.configure(highlightbackground="#d9d9d9")
        self.city_entry.configure(highlightcolor="black")
        self.city_entry.configure(insertbackground="black")
        self.city_entry.configure(selectbackground="#c4c4c4")
        self.city_entry.configure(selectforeground="black")

        self.Label7 = tk.Label(top)
        self.Label7.place(relx=0.017, rely=0.509, height=20, relwidth=0.244)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#84f29c")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(relief="groove")
        self.Label7.configure(text='''Τηλέφωνο''')

        self.Label8 = tk.Label(top)
        self.Label8.place(relx=0.017, rely=0.597, height=20, relwidth=0.244)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#84f29c")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(relief="groove")
        self.Label8.configure(text='''Κινητό''')

        self.Label9 = tk.Label(top)
        self.Label9.place(relx=0.568, rely=0.597, height=21, relwidth=0.170)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#84f29c")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(relief="groove")
        self.Label9.configure(text='''Φαξ''')

        self.Label10 = tk.Label(top)
        self.Label10.place(relx=0.568, rely=0.509, height=21, relwidth=0.170)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(background="#84f29c")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(relief="groove")
        self.Label10.configure(text='''e-mail''')

        self.address_entry = tk.Entry(top)
        self.address_entry.place(relx=0.275, rely=0.422, height=20, relwidth=0.280)
        self.address = StringVar()
        self.address_entry.configure(textvariable=self.address)
        self.address_entry.configure(background="white")
        self.address_entry.configure(disabledforeground="#a3a3a3")
        self.address_entry.configure(font="TkFixedFont")
        self.address_entry.configure(foreground="#000000")
        self.address_entry.configure(highlightbackground="#d9d9d9")
        self.address_entry.configure(highlightcolor="black")
        self.address_entry.configure(insertbackground="black")
        self.address_entry.configure(selectbackground="#c4c4c4")
        self.address_entry.configure(selectforeground="black")

        self.phone_entry = tk.Entry(top)
        self.phone_entry.place(relx=0.275, rely=0.509, height=20, relwidth=0.280)
        self.phone = StringVar()
        self.phone_entry.configure(textvariable=self.phone)
        self.phone_entry.configure(background="white")
        self.phone_entry.configure(disabledforeground="#a3a3a3")
        self.phone_entry.configure(font="TkFixedFont")
        self.phone_entry.configure(foreground="#000000")
        self.phone_entry.configure(highlightbackground="#d9d9d9")
        self.phone_entry.configure(highlightcolor="black")
        self.phone_entry.configure(insertbackground="black")
        self.phone_entry.configure(selectbackground="#c4c4c4")
        self.phone_entry.configure(selectforeground="black")

        self.post_code_entry = tk.Entry(top)
        self.post_code_entry.place(relx=0.757, rely=0.422, height=20
                                   , relwidth=0.217)
        self.post = StringVar()
        self.post_code_entry.configure(textvariable=self.post)
        self.post_code_entry.configure(background="white")
        self.post_code_entry.configure(disabledforeground="#a3a3a3")
        self.post_code_entry.configure(font="TkFixedFont")
        self.post_code_entry.configure(foreground="#000000")
        self.post_code_entry.configure(highlightbackground="#d9d9d9")
        self.post_code_entry.configure(highlightcolor="black")
        self.post_code_entry.configure(insertbackground="black")
        self.post_code_entry.configure(selectbackground="#c4c4c4")
        self.post_code_entry.configure(selectforeground="black")

        self.place_entry = tk.Entry(top)
        self.place_entry.place(relx=0.757, rely=0.334, height=20, relwidth=0.217)
        self.place = StringVar()
        self.place_entry.configure(textvariable=self.place)
        self.place_entry.configure(background="white")
        self.place_entry.configure(disabledforeground="#a3a3a3")
        self.place_entry.configure(font="TkFixedFont")
        self.place_entry.configure(foreground="#000000")
        self.place_entry.configure(highlightbackground="#d9d9d9")
        self.place_entry.configure(highlightcolor="black")
        self.place_entry.configure(insertbackground="black")
        self.place_entry.configure(selectbackground="#c4c4c4")
        self.place_entry.configure(selectforeground="black")

        self.Label13 = tk.Label(top)
        self.Label13.place(relx=0.017, rely=0.714, height=21, relwidth=0.244)
        self.Label13.configure(activebackground="#f9f9f9")
        self.Label13.configure(activeforeground="black")
        self.Label13.configure(background="#2f42f0")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#ffffff")
        self.Label13.configure(highlightbackground="#d9d9d9")
        self.Label13.configure(highlightcolor="black")
        self.Label13.configure(relief="groove")
        self.Label13.configure(text='''Σελίδες Πακέτου''')

        self.Label14 = tk.Label(top)
        self.Label14.place(relx=0.568, rely=0.714, height=21, relwidth=0.170)
        self.Label14.configure(activebackground="#f9f9f9")
        self.Label14.configure(activeforeground="black")
        self.Label14.configure(background="#2f42f0")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(foreground="#ffffff")
        self.Label14.configure(highlightbackground="#d9d9d9")
        self.Label14.configure(highlightcolor="black")
        self.Label14.configure(relief="groove")
        self.Label14.configure(text='''Κόστος Πακέτου''')

        self.page_package_entry = tk.Entry(top)
        self.page_package_entry.place(relx=0.275, rely=0.714, height=20
                                      , relwidth=0.280)
        self.package = StringVar()
        self.page_package_entry.configure(textvariable=self.package)
        self.page_package_entry.configure(background="white")
        self.page_package_entry.configure(disabledforeground="#a3a3a3")
        self.page_package_entry.configure(font="TkFixedFont")
        self.page_package_entry.configure(foreground="#000000")
        self.page_package_entry.configure(highlightbackground="#d9d9d9")
        self.page_package_entry.configure(highlightcolor="black")
        self.page_package_entry.configure(insertbackground="black")
        self.page_package_entry.configure(selectbackground="#c4c4c4")
        self.page_package_entry.configure(selectforeground="black")

        self.package_cost_entry = tk.Entry(top)
        self.package_cost_entry.place(relx=0.757, rely=0.714, height=20
                                      , relwidth=0.217)
        self.cost = StringVar()
        self.package_cost_entry.configure(textvariable=self.cost)
        self.package_cost_entry.configure(background="white")
        self.package_cost_entry.configure(disabledforeground="#a3a3a3")
        self.package_cost_entry.configure(font="TkFixedFont")
        self.package_cost_entry.configure(foreground="#000000")
        self.package_cost_entry.configure(highlightbackground="#d9d9d9")
        self.package_cost_entry.configure(highlightcolor="black")
        self.package_cost_entry.configure(insertbackground="black")
        self.package_cost_entry.configure(selectbackground="#c4c4c4")
        self.package_cost_entry.configure(selectforeground="black")

        self.add_btn = tk.Button(top)
        self.add_btn.place(relx=0.344, rely=0.850, height=34, relwidth=0.250)
        self.add_btn.configure(activebackground="#ececec")
        self.add_btn.configure(activeforeground="#000000")
        self.add_btn.configure(background="#339933")
        self.add_btn.configure(disabledforeground="#a3a3a3")
        self.add_btn.configure(foreground="#ffffff")
        self.add_btn.configure(highlightbackground="#d9d9d9")
        self.add_btn.configure(highlightcolor="black")
        self.add_btn.configure(pady="0")
        self.add_btn.configure(relief="ridge")
        self.add_btn.configure(text='''Ενεργοποίηση πελάτη''')
        self.add_btn.configure(command=self.add_to_db)

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.017, rely=0.685, relwidth=0.955)

        self.Label11 = tk.Label(top)
        self.Label11.place(relx=0.017, rely=0.058, height=21, relwidth=0.955)
        self.Label11.configure(background="#994d33")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#ffffff")
        self.Label11.configure(relief="ridge")
        self.Label11.configure(text='''Ενεργοποίηση πελάτη''')

        # Αν δεν υπάρχουν απενεργοποιημένοι πελάτες
        if not self.customers:
            messagebox.showinfo("Προσοχή ", "Δεν υπάρχουν απενεργοποιημένοι πελάτες")
            self.top.destroy()

    def quit(self, event):
        self.top.destroy()

    def get_customers_data(self, event=None):

        customer_name = self.customer_combobox.get()
        con = sqlite3.connect(dbase)
        c = con.cursor()
        c.execute("SELECT * FROM Πελάτες WHERE Επωνυμία_Επιχείρησης =?", (customer_name,))
        data = c.fetchall()
        c.close()
        con.close()
        data = data[0]
        self.company_name = StringVar(value=data[1])
        self.company_name_entry.configure(textvariable=self.company_name, state="readonly")

        self.name = StringVar(value=data[2])
        self.name_entry.configure(textvariable=self.name, state="readonly")

        self.address = StringVar(value=data[3])
        self.address_entry.configure(textvariable=self.address, state="readonly")

        self.city = StringVar(value=data[4])
        self.city_entry.configure(textvariable=self.city, state="readonly")

        self.post = StringVar(value=data[5])
        self.post_code_entry.configure(textvariable=self.post, state="readonly")

        self.place = StringVar(value=data[6])
        self.place_entry.configure(textvariable=self.place, state="readonly")

        self.phone = StringVar(value=data[7])
        self.phone_entry.configure(textvariable=self.phone, state="readonly")

        self.mobile = StringVar(value=data[8])
        self.mobile_entry.configure(textvariable=self.mobile, state="readonly")

        self.fax = StringVar(value=data[9])
        self.fax_entry.configure(textvariable=self.fax, state="readonly")

        self.email = StringVar(value=data[10])
        self.email_entry.configure(textvariable=self.email, state="readonly")

        self.package = StringVar(value=data[11])
        self.page_package_entry.configure(textvariable=self.package, state="readonly")

        self.cost = StringVar(value=data[12])
        self.package_cost_entry.configure(textvariable=self.cost, state="readonly")

    def add_to_db(self):

        conn = sqlite3.connect(dbase)
        cursor = conn.cursor()
        cursor.execute("UPDATE Πελάτες SET Κατάσταση =1 WHERE Επωνυμία_Επιχείρησης=?", (self.customer_combobox.get(),))

        conn.commit()
        conn.close()
        messagebox.showinfo("Info", f"Ο πελάτης {self.company_name.get()} ενεργοποιήθηκε επιτυχώς")
        self.top.destroy()
        return None


if __name__ == '__main__':
    vp_start_gui()
