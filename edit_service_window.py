#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 16, 2019 11:26:05 PM EET  platform: Windows NT
import os
import sys
import sqlite3
from tkinter import StringVar, filedialog, messagebox, PhotoImage
import edit_service_window_support
import image_viewer
import add_spare_parts
from datetime import datetime
import logging

import insert_spare_parts

spare_parts_db = ""
dbase = "Service_book.db"
selected_service_id = None
selected_copier = None
selected_customer = None
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
            purpose_list.append(service_data[n][1])                        # Σκοπός
        if service_data[n][2] != "" and service_data[n][2] is not None:
            actions_list.append(service_data[n][2])                        # Ενέργειες
    return sorted(purpose_list), sorted(actions_list)

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


class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    edit_service_window_support.set_Tk_var()
    top = edit_service_window(root)
    edit_service_window_support.init(root, top)
    root.mainloop()


w = None


def create_edit_service_window(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt, selected_service_id, selected_copier, selected_customer
    selected_service_id = args[0]  # Επιλεγμένο Service  περνουμε το selected_service_id απο το service_book_colors.py
    try:
        selected_copier = args[1]      # Επιλεγμένο Φωτοτυπικό περνουμε το selected_copier απο το service_book_colors.py
        selected_customer = args[2]    # Επιλεγμένο πελάτης περνουμε το selected_customer απο το service_book_colors.py
    except IndexError as error:
        pass
    rt = root
    w = tk.Toplevel(root)
    edit_service_window_support.set_Tk_var()
    top = edit_service_window(w)
    edit_service_window_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_edit_service_window():
    global w
    w.destroy()
    w = None


class edit_service_window():

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        # Αρχικοποιηση του selected_service_id σαν self.selected_service_id
        self.selected_service_id = selected_service_id
        self.copier_id = ""
        self.selected_copier = selected_copier
        self.selecter_customer = selected_customer
        self.purpose_list, self.actions_list = get_service_data()
        self.files = []
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
            self.style.theme_use('clam')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="-family {Calibri} -size 10 -weight bold")
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])
        # ==============================  Notebook style  =============
        self.style.map('TNotebook.Tab', background=[('selected', "#6b6b6b"), ('active', "#69ab3a")])
        self.style.map('TNotebook.Tab', foreground=[('selected', "white"), ('active', "white")])

        self.top = top
        top.geometry("655x650+0+0")
        top.minsize(120, 1)
        top.maxsize(1604, 881)
        top.resizable(1, 1)
        top.title("Επεξεργασία ιστορικού συντήρησης")
        top.configure(background="#f6f6ee")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        top.bind('<Escape>', self.quit)
        top.focus()

        # ==========================  Notebook  ==================================
        self.notebook = ttk.Notebook(top)
        self.notebook.place(relx=0.021, rely=0.230, relheight=0.740, relwidth=0.938)
        self.notebook.configure(takefocus="")

        self.service_frame = tk.Frame(self.notebook)
        self.notebook.add(self.service_frame, padding=3)
        self.notebook.tab(0, text="Συντήρηση", compound="left", underline="-1", )
        self.service_frame.configure(background="#CFD5CE")
        self.service_frame.configure(highlightbackground="#d9d9d9")
        self.service_frame.configure(highlightcolor="black")

        self.spare_parts_frame = tk.Frame(self.notebook)
        self.notebook.add(self.spare_parts_frame, padding=3)
        self.notebook.tab(1, text="Ανταλλακτικά", compound="left", underline="-1", )
        self.spare_parts_frame.configure(background="#CFD5CE")
        self.spare_parts_frame.configure(highlightbackground="#d9d9d9")
        self.spare_parts_frame.configure(highlightcolor="black")

        # Εμφάνιση πελάτη
        self.customer_label = tk.Label(top)
        self.customer_label.place(relx=0.025, rely=0.100, height=25, relwidth=0.938)
        self.customer_label.configure(activebackground="#f9f9f9")
        self.customer_label.configure(background="brown")
        self.customer_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.customer_label.configure(foreground="#ffffff")
        self.customer_label.configure(relief="groove")
        self.customer_label.configure(text=self.selecter_customer)

        # Εμφάνιση Φωτοτυπικού
        self.selected_copier_label = tk.Label(top)
        self.selected_copier_label.place(relx=0.025, rely=0.160, height=25, relwidth=0.938)
        self.selected_copier_label.configure(activebackground="#f9f9f9")
        self.selected_copier_label.configure(background="#808000")
        self.selected_copier_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.selected_copier_label.configure(foreground="#ffffff")
        self.selected_copier_label.configure(relief="groove")
        self.selected_copier_label.configure(text=self.selected_copier)
        # Ημερομηνία
        self.date_label = tk.Label(self.service_frame)
        self.date_label.place(relx=0.025, rely=0.030, height=25, relwidth=0.331)
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
        self.date_entry = tk.Entry(self.service_frame)
        self.date_entry.place(relx=0.37, rely=0.030, height=25, relwidth=0.331)
        self.date_entry.configure(background="white")
        self.date_entry.configure(disabledforeground="#a3a3a3")
        self.date_entry.configure(font="-family {Calibri} -size 10 -weight bold")
        self.date_entry.configure(foreground="#000000")
        self.date_entry.configure(insertbackground="black")
        # Counter
        self.counter_label = tk.Label(self.service_frame)
        self.counter_label.place(relx=0.025, rely=0.100, height=25, relwidth=0.331)
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
        self.counter_entry = tk.Entry(self.service_frame)
        self.counter_entry.place(relx=0.37, rely=0.100, height=25, relwidth=0.331)
        self.counter_entry.configure(background="white")
        self.counter_entry.configure(disabledforeground="#a3a3a3")
        self.counter_entry.configure(font="-family {Calibri} -size 10 -weight bold")
        self.counter_entry.configure(foreground="#000000")
        self.counter_entry.configure(highlightbackground="#d9d9d9")
        self.counter_entry.configure(highlightcolor="black")
        self.counter_entry.configure(insertbackground="black")
        self.counter_entry.configure(selectbackground="#c4c4c4")
        self.counter_entry.configure(selectforeground="black")

        # Αρχεία
        self.show_files_btn = tk.Button(self.spare_parts_frame)
        self.show_files_btn.place(relx=0.320, rely=0.700, height=60, relwidth=0.250)
        self.show_files_btn.configure(activebackground="#ececec")
        self.show_files_btn.configure(activeforeground="#000000")
        self.show_files_btn.configure(background="#6b6b6b")
        self.show_files_btn.configure(disabledforeground="red")
        self.show_files_btn.configure(foreground="#ffffff")
        self.show_files_btn.configure(highlightbackground="#d9d9d9")
        self.show_files_btn.configure(highlightcolor="black")
        self.show_files_btn.configure(pady="0")
        self.show_files_btn.configure(text='''Προβολή \nαρχείων''')
        self.show_files_btn.configure(command=self.show_files)
        self.show_files_btn.configure(state="active")

        # Ανταλλακτικά
        self.add_spare_parts_btn = tk.Button(self.spare_parts_frame)
        self.add_spare_parts_btn.place(relx=0.625, rely=0.700, height=60, relwidth=0.250)
        self.add_spare_parts_btn.configure(activebackground="#ececec")
        self.add_spare_parts_btn.configure(activeforeground="#000000")
        self.add_spare_parts_btn.configure(background="green")
        self.add_spare_parts_btn.configure(disabledforeground="#a3a3a3")
        self.add_spare_parts_btn.configure(foreground="#ffffff")
        self.add_spare_parts_btn.configure(highlightbackground="#d9d9d9")
        self.add_spare_parts_btn.configure(highlightcolor="black")
        self.add_spare_parts_btn.configure(pady="0")
        self.add_spare_parts_btn.configure(text='''Προσθήκη\nανταλλακτικών''')
        self.add_spare_parts_btn.configure(command=self.add_spare_parts)

        # Ανανέωση μετα απο εισαγωγη ανταλλακτικών
        self.refresh_btn = tk.Button(self.spare_parts_frame)
        self.refresh_btn.place(relx=0.875, rely=0.700, height=60, relwidth=0.060)
        self.refresh_btn.configure(background="#6b6b6b")
        self.refresh_img = PhotoImage(file="icons/refresh.png")
        self.refresh_btn.configure(image=self.refresh_img)
        self.refresh_btn.configure(command=self.get_spare_parts)

        # Σκοπός
        self.purpose_label = tk.Label(self.service_frame)
        self.purpose_label.place(relx=0.025, rely=0.170, height=25, relwidth=0.331)
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
        self.purpose_combobox = ttk.Combobox(self.service_frame)
        self.purpose_combobox.place(relx=0.37, rely=0.170, relheight=0.055, relwidth=0.6)
        self.purpose_combobox.configure(values=self.purpose_list)
        # self.purpose_combobox.configure(textvariable=edit_service_window_support.combobox)
        self.purpose_combobox.configure(takefocus="")
        # Ενέργειες
        self.actions_label = tk.Label(self.service_frame)
        self.actions_label.place(relx=0.025, rely=0.240, height=25, relwidth=0.331)
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
        self.actions_combobox = ttk.Combobox(self.service_frame)
        self.actions_combobox.place(relx=0.37, rely=0.240, relheight=0.055, relwidth=0.6)
        self.actions_combobox.configure(values=self.actions_list)
        # self.actions_combobox.configure(textvariable=edit_service_window_support.combobox)
        self.actions_combobox.configure(takefocus="")

        # Επόμενο Service
        self.next_service_label = tk.Label(self.service_frame)
        self.next_service_label.place(relx=0.025, rely=0.310, height=25, relwidth=0.331)
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
        self.next_service_entry = tk.Entry(self.service_frame)
        self.next_service_entry.place(relx=0.37, rely=0.310, height=25, relwidth=0.331)
        self.next_service_entry.configure(background="white")
        self.next_service_entry.configure(disabledforeground="#a3a3a3")
        self.next_service_entry.configure(font="TkFixedFont")
        self.next_service_entry.configure(foreground="#000000")
        self.next_service_entry.configure(highlightbackground="#d9d9d9")
        self.next_service_entry.configure(highlightcolor="black")
        self.next_service_entry.configure(insertbackground="black")
        self.next_service_entry.configure(selectbackground="#c4c4c4")
        self.next_service_entry.configure(selectforeground="black")

        # Προσθήκη αρχείων
        self.add_files_btn = tk.Button(self.spare_parts_frame)
        self.add_files_btn.place(relx=0.025, rely=0.700, height=55, relwidth=0.237)
        self.add_files_btn.configure(activebackground="#ececec")
        self.add_files_btn.configure(activeforeground="#000000")
        self.add_files_btn.configure(background="green")
        self.add_files_btn.configure(disabledforeground="#a3a3a3")
        self.add_files_btn.configure(foreground="#ffffff")
        self.add_files_btn.configure(highlightbackground="#d9d9d9")
        self.add_files_btn.configure(highlightcolor="black")
        self.add_files_btn.configure(pady="0")
        self.add_files_btn.configure(text='''Προσθήκη\nαρχείων''')
        self.add_files_btn.configure(command=self.add_files)

        # Δελτίο Τεχνικής Εξυπηρέτησης
        self.dte_label = tk.Label(self.service_frame)
        self.dte_label.place(relx=0.025, rely=0.380, height=25, relwidth=0.331)
        self.dte_label.configure(activebackground="#f9f9f9")
        self.dte_label.configure(activeforeground="black")
        self.dte_label.configure(background="#6b6b6b")
        self.dte_label.configure(disabledforeground="#a3a3a3")
        self.dte_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.dte_label.configure(foreground="#ffffff")
        self.dte_label.configure(highlightbackground="#d9d9d9")
        self.dte_label.configure(highlightcolor="black")
        self.dte_label.configure(relief="groove")
        self.dte_label.configure(text='''Δελτίο Τεχν. Εξυπ.''')
        self.dte_entry = tk.Entry(self.service_frame)
        self.dte_entry.place(relx=0.37, rely=0.380, height=25, relwidth=0.331)
        self.dte_entry.configure(background="white")
        self.dte_entry.configure(disabledforeground="#a3a3a3")
        self.dte_entry.configure(font="TkFixedFont")
        self.dte_entry.configure(foreground="#000000")
        self.dte_entry.configure(highlightbackground="#d9d9d9")
        self.dte_entry.configure(highlightcolor="black")
        self.dte_entry.configure(insertbackground="black")
        self.dte_entry.configure(selectbackground="#c4c4c4")
        self.dte_entry.configure(selectforeground="black")

        self.TSeparator1 = ttk.Separator(self.service_frame)
        self.TSeparator1.place(relx=0.025, rely=0.450, relwidth=0.938)
        # Σημειώσεις
        self.notes_label = tk.Label(self.service_frame)
        self.notes_label.place(relx=0.025, rely=0.470, height=30, relwidth=0.331)
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
        self.notes_scrolledtext = ScrolledText(self.service_frame)
        self.notes_scrolledtext.place(relx=0.025, rely=0.550, relheight=0.300, relwidth=0.941)
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


        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.025, rely=0.021, height=31, relwidth=0.938)
        self.Label2.configure(background="#006291")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(relief="groove")
        self.Label2.configure(text='''Επεξεργασία ιστορικού''')

        self.edit()
        self.check_if_files_exists()

        # Ανταλλακτικά
        self.spare_parts_label = tk.Label(self.spare_parts_frame)
        self.spare_parts_label.place(relx=0.017, rely=0.010, height=30, relwidth=0.970)
        self.spare_parts_label.configure(activebackground="#f9f9f9")
        self.spare_parts_label.configure(activeforeground="black")
        self.spare_parts_label.configure(background="#6b6b6b")
        self.spare_parts_label.configure(disabledforeground="#a3a3a3")
        self.spare_parts_label.configure(font=font11)
        self.spare_parts_label.configure(foreground="#ffffff")
        self.spare_parts_label.configure(highlightbackground="#d9d9d9")
        self.spare_parts_label.configure(highlightcolor="black")
        self.spare_parts_label.configure(relief="groove")
        self.spare_parts_label.configure(text='''Ανταλλακτικά''')

        self.spare_parts_treeview = ScrolledTreeView(self.spare_parts_frame)
        self.spare_parts_treeview.place(relx=0.017, rely=0.100, relheight=0.500, relwidth=0.970)
        self.spare_parts_treeview.configure(show="headings", style="mystyle.Treeview")
        self.get_spare_parts()


    # Ελεγχος αν υπάρχουν αρχεία για προβολή
    def check_if_files_exists(self):
        con = sqlite3.connect(dbase)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Service_images WHERE Service_ID =?", (self.selected_service_id,))
        images = cursor.fetchall()
        cursor.close()
        con.close()
        if images == []:  # αδεια λιστα δλδ δεν υπάρχουν αρχεια και απενεργοποιουμε το κουμπί προβολή αρχείων
            self.show_files_btn.configure(state="disabled")

    # Προβολή αρχείων
    def show_files(self):
        image_viewer.create_Toplevel1(w, self.selected_service_id)

    # επεξεργασία δεδομένων
    def edit(self):
        edit_conn = sqlite3.connect(dbase)
        edit_corsor = edit_conn.cursor()
        edit_corsor.execute("SELECT * FROM Service WHERE ID = ?", (self.selected_service_id,))
        self.culumns = list(map(lambda x: x[0], edit_corsor.description))

        data = edit_corsor.fetchall()
        self.copier_id = data[0][7]
        edit_corsor.close()
        edit_conn.close()
        # w ==>> το global root
        date = StringVar(w, value=data[0][1])
        self.date_entry.configure(textvariable=date)
        purpose_combobox = StringVar(w, value=data[0][2])
        self.purpose_combobox.set(purpose_combobox.get())
        action = StringVar(w, value=data[0][3])
        self.actions_combobox.set(action.get())
        notes = StringVar(w, value=data[0][4])
        self.notes_scrolledtext.insert('1.0', notes.get())
        counter = StringVar(w, value=data[0][5])
        self.counter_entry.configure(textvariable=counter)
        next_service = StringVar(w, value=data[0][6])
        self.next_service_entry.configure(textvariable=next_service)
        dte = StringVar(w, value=data[0][8])
        self.dte_entry.configure(textvariable=dte)

        # Προσθήκη αλλαγών στην βαση δεδομένων
        def add_to_db():
            self.add_files_to_db()
            edited_culumns = []
            for culumn in self.culumns:
                if culumn != "ID":
                    edited_culumns.append(culumn + "=?")
            edited_culumns = ",".join(edited_culumns)
            data_to_add = [date.get(), self.purpose_combobox.get(), self.actions_combobox.get(),
                           self.notes_scrolledtext.get("1.0", "end-1c"), counter.get(), next_service.get(),
                           self.copier_id, dte.get(), self.selected_service_id]

            add_conn = sqlite3.connect(dbase)
            add_cursor = add_conn.cursor()
            add_cursor.execute("UPDATE Service  SET " + edited_culumns + " WHERE ID=? ", (tuple(data_to_add)))
            add_conn.commit()
            add_conn.close()
            w.destroy()

        self.save_btn = tk.Button(w)
        self.save_btn.place(relx=0.350, rely=0.914, height=34, width=147)
        self.save_btn.configure(activebackground="#ececec")
        self.save_btn.configure(activeforeground="#000000")
        self.save_btn.configure(background="#808000")
        self.save_btn.configure(disabledforeground="#a3a3a3")
        self.save_btn.configure(font=("Calibri", 12, "bold"))
        self.save_btn.configure(foreground="#ffffff")
        self.save_btn.configure(highlightbackground="#d9d9d9")
        self.save_btn.configure(highlightcolor="black")
        self.save_btn.configure(pady="2")
        self.save_btn.configure(text="Αποθήκευση")
        self.save_btn.configure(command=add_to_db)

    # Προσθήκη αρχείων
    def add_files(self):

        self.files = filedialog.askopenfilenames(initialdir=os.getcwd(), title="Επιλογή αρχείων για προσθήκη",
                                                 filetypes=[("Υπ. αρχεία", "*.jpg *.png *.pdf")])

        if self.files == "":  # αν ο χρήστης επιλεξει ακυρο
            self.top.focus()
            return

        self.top.focus()

    def add_files_to_db(self):
        if self.files == "":
            return
        con = sqlite3.connect(dbase)
        cu = con.cursor()

        def convert_bytes(size):
            for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
                if size < 1024.0:
                    return "%3.1f %s" % (size, x)
                size /= 1024.0

            return size

        # Εισαγωγη αρχείων
        for img in self.files:
            base = os.path.basename(img)
            filename, ext = os.path.splitext(base)
            with open(img, 'rb') as f:
                file = f.read()  # Εισαγωγη αρχείων
                # file_size = convert_bytes(len(file))  # Καλύτερα σε bytes για ευκολή ταξινόμηση
                file_size = len(file)  # μεγεθος σε bytes
            cu.execute("INSERT INTO Service_images(Service_ID, Filename, Type, File_size, File, Copier_ID)"
                       "VALUES(?,?,?,?,?,?)", (self.selected_service_id, filename, ext, file_size, sqlite3.Binary(file),
                                              self.copier_id))

        con.commit()
        con.close()
        messagebox.showinfo("Info", f"Οι εικόνες προστέθηκαν επιτυχώς")
        self.top.focus()

    def quit(self, event):
        self.top.destroy()

    def get_spare_parts(self, event=None):
        self.spare_parts_treeview.delete(*self.spare_parts_treeview.get_children())
        con = sqlite3.connect(dbase)
        c = con.cursor()
        c.execute("SELECT * FROM Ανταλλακτικά WHERE Service_ID =?", (self.selected_service_id,))
        headers = list(map(lambda x: x[0], c.description))
        data = c.fetchall()
        con.close()
        self.spare_parts_treeview["columns"] = [head for head in headers]
        for head in headers:
            if head == "id" or head == "ID" or head == "Id":
                platos = 1
            elif head == "ΠΕΡΙΓΡΑΦΗ":
                platos = 500
            else:
                platos = 121
            self.spare_parts_treeview.heading(head, text=head, anchor="center")
            self.spare_parts_treeview.column(head, width=platos, anchor="center")
        for d in data:
            self.spare_parts_treeview.insert("", "end", values=d)

    # Προσθήκη ανταλλακτικών
    def add_spare_parts(self):
        self.top.focus()
        if spare_parts_db:
            add_spare_parts.create_Toplevel1(self.top, self.selected_service_id)
        else:
            insert_spare_parts.create_insert_spare_parts_window(self.top, self.selected_service_id)

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
