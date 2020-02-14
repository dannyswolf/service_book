#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 26, 2019 12:38:51 AM EET  platform: Windows NT

import sys
from tkinter import PhotoImage, StringVar
import sqlite3
from settings import dbase,  root_logger  # settings


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

import copiers_log_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    copiers_log_support.init(root, top)
    root.mainloop()


w = None
rt = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    copiers_log_support.init(w, top, *args, **kwargs)
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
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family Calibri -size 12 -weight bold -slant roman "  \
            "-underline 1 -overstrike 0"
        font9 = "-family Calibri -size 10 -weight bold -slant roman "  \
            "-underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('clam')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])
        # ==============================  Notebook style  =============
        self.style.map('TNotebook.Tab', background=[('selected', "#6b6b6b"), ('active', "#69ab3a")])
        self.style.map('TNotebook.Tab', foreground=[('selected', "white"), ('active', "white")])
        self.top = top
        top.geometry("600x300+310+227")
        top.minsize(120, 1)
        top.maxsize(2604, 2881)
        top.resizable(1, 1)
        top.title("Ιστορικό μεταφοράς μηχανήματος")
        top.configure(background="#f6f6ee")
        top.focus()
        top.bind('<Escape>', self.quit)

        self.entry = StringVar()
        self.Entry1 = tk.Entry(top, textvariable=self.entry)
        self.Entry1.place(relx=0.2, rely=0.267, height=25, relwidth=0.323)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=("Calibri", 10, "bold"))
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.bind('<Return>', self.search)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.533, rely=0.267, height=25, width=145)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#006291")
        self.Button1.configure(compound='left')
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font=font9)
        self.Button1.configure(foreground="#ffffff")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.search_img = PhotoImage(file="icons/search.png")
        self.Button1.configure(image=self.search_img)
        self.Button1.configure(text='''Αναζήτηση''')
        self.Button1.configure(command=self.search)

        self.Scrolledtreeview1 = ScrolledTreeView(top)
        self.Scrolledtreeview1.place(relx=0.017, rely=0.367, relheight=0.59, relwidth=0.967)
        self.Scrolledtreeview1.configure(show="headings", style="mystyle.Treeview")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.2, rely=0.067, height=31, relwidth=0.575)
        self.Label1.configure(background="#006291")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(relief="groove")
        self.Label1.configure(text='''Ιστορικό μεταφοράς μηχανήματος''')
        self.get_data()

    def get_data(self):

        con = sqlite3.connect(dbase)
        cursor = con.cursor()
        cursor.execute("SELECT * FROM Copiers_Log")
        self.headers = list(map(lambda x: x[0], cursor.description))

        data = cursor.fetchall()
        cursor.close()
        con.close()
        self.Scrolledtreeview1["columns"] = [head for head in self.headers]
        for head in self.headers:
            if head == "ID_μηχανήματος":
                platos = 1
            else:
                platos = 100
            self.Scrolledtreeview1.heading(head, text=head, anchor="center")
            self.Scrolledtreeview1.column(head, width=platos, anchor="center")

        for n in range(len(data)):
            self.Scrolledtreeview1.insert("", "end", values=data[n])

    def quit(self, event):
        rt.focus()
        self.top.destroy()

    def fixed_map(self, option):
        # Fix for setting text colour for Tkinter 8.6.9
        # From: https://core.tcl.tk/tk/info/509cafafae
        #
        # Returns the style map for 'option' with any styles starting with
        # ('!disabled', '!selected', ...) filtered out.

        # style.map() returns an empty list for missing options, so this
        # should be future-safe.
        return [elm for elm in self.style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]

    def search(self, event=None):
        # Αδειάζουμε πρώτα το tree
        self.Scrolledtreeview1.delete(*self.Scrolledtreeview1.get_children())
        data_to_search = self.entry.get()
        search_headers = []
        no_neded_headers = ["id", "ID", "Id"]
        operators = []
        for header in self.headers:

            if header not in no_neded_headers:
                search_headers.append(header + " LIKE ?")
                operators.append('%' + str(data_to_search) + '%')
        search_headers = " OR ".join(search_headers)
        # ΕΤΑΙΡΕΙΑ LIKE ? OR ΜΟΝΤΕΛΟ LIKE ? OR ΚΩΔΙΚΟΣ LIKE ? OR TEMAXIA LIKE ? OR ΤΙΜΗ LIKE ? etc...

        # search_cursor.execute("SELECT * FROM " + table + " WHERE \
        # ΤΟΝΕΡ LIKE ? OR ΜΟΝΤΕΛΟ LIKE ? OR ΚΩΔΙΚΟΣ LIKE ? OR TEMAXIA LIKE ? OR ΤΙΜΗ LIKE ? etc...
        # ('%' + str(search_data.get()) + '%', '%' + str(search_data.get()) + '%', '%' + str(search_data.get())...

        # Αναζήτηση σε ολο το Service και αν το [-1] είναι ισο με το επιλεγμένο φωτοτυπικό δλδ
        # ελεγχουμε να πάρουμε τα δεδομένα του Service μόνο για το επιλεγμένο Φωτοτυπικό
        #
        conn = sqlite3.connect(dbase)
        cusror = conn.cursor()
        cusror.execute("SELECT * FROM Copiers_Log WHERE " + search_headers, operators)
        fetch = cusror.fetchall()  # Δεδομένα απο Service
        conn.close()
        columns = []
        # for head in self.headers:
            # columns.append(head)

        # self.Scrolledtreeview1["columns"] = [head for head in columns]
        # for head in self.headers:
        #     if head == "ID":
        #         platos = 1
        #     elif head == "Ημερομηνία":
        #         platos = 100
        #     elif head == "Σκοπός_Επίσκεψης":
        #         platos = 220
        #     elif head == "Ενέργειες":
        #         platos = 180
        #     elif head == "Σημειώσεις":
        #         platos = 275
        #     elif head == "Μετρητής":
        #         platos = 80
        #     elif head == "Επ_Service":
        #         platos = 110
        #     elif head == "ΔΤΕ":
        #         platos = 70
        #     else:
        #         platos = 100
        #     self.Scrolledtreeview1.heading(head, text=head, anchor="center")
        #     self.Scrolledtreeview1.column(head, width=platos, anchor="center")
        # item[-2] ==> Copier_ID στον πίνακα Service
        for item in fetch:
            self.Scrolledtreeview1.insert("", "end", values=item)

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

        #self.configure(yscrollcommand=_autoscroll(vsb),
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
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





