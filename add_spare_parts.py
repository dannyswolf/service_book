#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 26, 2019 12:38:51 AM EET  platform: Windows NT


import sys
from tkinter import PhotoImage, StringVar, messagebox
import sqlite3
import copiers_log_support
from settings import dbase, spare_parts_db, root_logger  # settings


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


def get_tables():
    no_needed_tables = ['ΠΡΩΤΟΣ_ΟΡΟΦΟΣ']
    con = sqlite3.connect(spare_parts_db)
    c = con.cursor()
    c.execute("SELECT name FROM sqlite_sequence ORDER BY name")
    tables = c.fetchall()
    c.close()
    con.close()
    companies = []
    for table in tables:
        if table[0] not in no_needed_tables:
            companies.append(table[0])

    return companies

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    copiers_log_support.init(root, top)
    root.mainloop()

w = None
service_id = ""
customer_id = ""
copier_name = ""

def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt, service_id, customer_id, copier_name
    service_id = args[0]  # Το Service_ID απο το add_service.py, edit_service_windows, edit_task.py
    customer_id = args[1]   # Το customer_id απο το add_service.py, edit_service_windows, edit_task.py
    copier_name = args[2]
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

        top.geometry("1024x500+310+227")
        top.minsize(120, 1)
        top.maxsize(2250, 2040)
        top.resizable(1, 1)
        top.title("Προσθήκη ανταλλακτικού")
        top.configure(background="#f6f6ee")
        top.focus()
        top.bind('<Escape>', self.quit)
        # top.protocol("WM_DELETE_WINDOW", self.root.focus())

        self.companies = get_tables()
        self.headers = []
        self.selected_company = ""
        self.service_ID = service_id
        self.customer_id = customer_id[0]
        self.copier = copier_name
        self.select_company_label = tk.Label(top)
        self.select_company_label.place(relx=0.025, rely=0.200, relheight=0.060, relwidth=0.260)
        self.select_company_label.configure(activebackground="#f9f9f9")
        self.select_company_label.configure(activeforeground="black")
        self.select_company_label.configure(background="#6b6b6b")
        self.select_company_label.configure(disabledforeground="#a3a3a3")
        self.select_company_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.select_company_label.configure(foreground="#ffffff")
        self.select_company_label.configure(highlightbackground="#d9d9d9")
        self.select_company_label.configure(highlightcolor="black")
        self.select_company_label.configure(relief="groove")
        self.select_company_label.configure(text='''Επιλογή εταιρείας''')
        self.company_combobox = ttk.Combobox(top)
        self.company_combobox.place(relx=0.29, rely=0.200, relheight=0.060, relwidth=0.500)
        self.company_combobox.configure(values=self.companies)
        # self.actions_combobox.configure(textvariable=edit_service_window_support.combobox)
        self.company_combobox.configure(takefocus="")
        self.company_combobox.bind("<<ComboboxSelected>>", self.get_spare_parts)

        self.entry = StringVar()
        self.Entry1 = tk.Entry(top, textvariable=self.entry)
        self.Entry1.place(relx=0.29, rely=0.300, height=25, relwidth=0.323)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font=("Calibri", 10, "bold"))
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.bind('<Return>', self.search)

        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.620, rely=0.300, height=25, width=145)
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

        self.add_to_service_btn = tk.Button(top)
        self.add_to_service_btn.place(relx=0.820, rely=0.300, height=25, width=145)
        self.add_to_service_btn.configure(activebackground="#ececec")
        self.add_to_service_btn.configure(activeforeground="#000000")
        self.add_to_service_btn.configure(background="#006291")
        self.add_to_service_btn.configure(compound='left')
        self.add_to_service_btn.configure(disabledforeground="#a3a3a3")
        self.add_to_service_btn.configure(font=font9)
        self.add_to_service_btn.configure(foreground="#ffffff")
        self.add_to_service_btn.configure(highlightbackground="#d9d9d9")
        self.add_to_service_btn.configure(highlightcolor="black")
        self.add_to_service_btn.configure(pady="0")
        self.add_to_service_btn.configure(text='''Προσθήκη''')
        self.add_to_service_btn.configure(command=self.add_to_service)

        self.spare_parts_treeview = ScrolledTreeView(top)
        self.spare_parts_treeview.place(relx=0.017, rely=0.367, relheight=0.59, relwidth=0.967)
        self.spare_parts_treeview.configure(show="headings", style="mystyle.Treeview")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.2, rely=0.067, height=31, relwidth=0.575)
        self.Label1.configure(background="#006291")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font11)
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(relief="groove")
        self.Label1.configure(text='''Επιλογή ανταλλακτικών''')

        if not self.service_ID:
            messagebox.showerror("Σφάλμα!", "Παρακαλώ επιλεξτε πρώτα ιστορικό συντήρησής.")
            self.top.destroy()

    def get_spare_parts(self, event=None):
        self.selected_company = self.company_combobox.get()
        if self.selected_company != "":
            self.spare_parts_treeview.delete(*self.spare_parts_treeview.get_children())

        con = sqlite3.connect(spare_parts_db)
        c = con.cursor()
        c.execute("SELECT * FROM " + self.selected_company + ";")
        self.headers = list(map(lambda x: x[0], c.description))
        data = c.fetchall()
        con.close()
        self.spare_parts_treeview["columns"] = [head for head in self.headers]
        for head in self.headers:
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

    def quit(self, event):
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
        self.spare_parts_treeview.delete(*self.spare_parts_treeview.get_children())
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

        conn = sqlite3.connect(spare_parts_db)
        cusror = conn.cursor()
        cusror.execute("SELECT * FROM " + self.selected_company + " WHERE " + search_headers, operators)
        fetch = cusror.fetchall()  # Δεδομένα απο Service
        conn.close()
        for item in fetch:
            self.spare_parts_treeview.insert("", "end", values=item)

    def add_to_service(self):
        selected_items = self.spare_parts_treeview.selection()
        if not selected_items:
            messagebox.showerror("Προσοχή", "Παρακαλώ επιλέξτε πρώτα προιόν")
            self.top.focus()
            return
        items_to_add = []
        for item in selected_items:
            info = self.spare_parts_treeview.set(item)
            items_to_add.append(info)
        service_con = sqlite3.connect(dbase)
        service_cursor = service_con.cursor()
        # # sql_insert = "INSERT INTO  " + table + "(" + culumns + ")" + "VALUES(NULL, ?, ?, ?, ?, ?, ?, ?);"

        # Ελεγχος αν το ανταλλακτικό υπάρχει τοτε να προσθέση στα τεμαχια +1
        # o ελεγχος γίνεται με τους κωδικους προιόντος
        # αν ο κωδικός υπάρχει στο ιστορικό του Service_ID τότε ρωτάει και αναλογα προσθέτη +1 στο τεμάχιο
        # πρώτα πέρνουμε του κωδικούς
        service_cursor.execute("SELECT ΚΩΔΙΚΟΣ FROM Ανταλλακτικά WHERE Service_ID =?", (self.service_ID,))
        spare_parts = service_cursor.fetchall()
        service_con.close()
        used_parts = []
        for part in spare_parts:
            # εδω τα κάνουμε σε λίστα γιατι το fetchall επιστρέφει [('6207',), ('6208',)]
            used_parts.append(part[0])

        added_codes = []
        for item in items_to_add:
            for key, value in item.items():   # Dictionary
                if key == "ΚΩΔΙΚΟΣ":  #
                    added_codes.append(value)
                # όταν το value  πάρει την τιμή του κωδικού πχ 6207 και ο κωδικός αυτός υπάρχει στα Service_ID
                # τότε προσθέτη +1 στο πεδίο Τεμάχια του πίνακα Ανταλλακτικά στο κωδικό 6207
                if value in used_parts:  # value είναι ο κωδικός ==> 6207

                    answer = messagebox.askyesno("Προσοχή!", f"Ο κωδικός  {value}, υπάρχει στο ιστορικό αυτό "
                                                              f"θέλετε να το ξανα προσθέσετε;")

                    # Προσθήκη +1 στα τεμάχια
                    if answer:
                        service_con = sqlite3.connect(dbase)
                        service_cursor = service_con.cursor()
                        service_cursor.execute("SELECT ΤΕΜΑΧΙΑ FROM Ανταλλακτικά WHERE ΚΩΔΙΚΟΣ = ? AND Service_ID =?",
                                               (value, self.service_ID,))
                        pieces = service_cursor.fetchall()
                        new_pieces = int(pieces[0][0]) + 1
                        service_cursor.execute("UPDATE Ανταλλακτικά SET ΤΕΜΑΧΙΑ =? WHERE ΚΩΔΙΚΟΣ =? AND Service_ID =?",
                                               (new_pieces, value, self.service_ID))
                        service_con.commit()
                        service_con.close()
                        con = sqlite3.connect(spare_parts_db)
                        c = con.cursor()

                        # Ενημέρωση αποθήκης  -1 στα προιόντα
                        c.execute("SELECT ΤΕΜΑΧΙΑ FROM " + self.selected_company + " WHERE ΚΩΔΙΚΟΣ =?", (value,))
                        old_pieces = c.fetchall()
                        print("old_pieces of code ", old_pieces, value)
                        new_pieces = int(old_pieces[0][0]) - 1
                        c.execute("UPDATE " + self.selected_company + " SET ΤΕΜΑΧΙΑ =? WHERE ΚΩΔΙΚΟΣ =?",
                                  (new_pieces, value))
                        con.commit()
                        print("line 302"
                            f"Οι κωδικοί {added_codes} αφερέθηκαν απο την αποθήκη {self.selected_company} με επιτυχία ")
                        c.close()
                        con.close()
                        # messagebox.showinfo("Πληροφορία", f"O κωδικός {value} προστέθηκε ")
                        self.top.destroy()
                        return
                    else:
                        self.top.focus()
                        return

        # Μετά το for item in items_to_add:
        self.get_spare_parts()
        self.top.focus()
        not_needed_keys = ["ID", "id", 'Id', 'ΕΤΑΙΡΕΙΑ', 'ΠΟΙΟΤΗΤΑ', 'ΑΝΑΛΩΣΙΜΟ', 'ΤΙΜΗ', 'ΣΥΝΟΛΟ', 'ΣΕΛΙΔΕΣ', 'ΠΕΛΑΤΕΣ']
        added_codes = []
        service_con = sqlite3.connect(dbase)
        service_cursor = service_con.cursor()
        for item in items_to_add:
            values = []  # values είναι πόσα ? να έχει ανάλογα τα culumn ==> keys
            keys = []    # ID , parts_nr, Περιγραφή , Τεμάχια etc...
            data = []    # Δεδομένα
            for key, value in item.items():   # Dictionary
                if value in used_parts:   # όταν το value  πάρει την τιμή του κωδικού πχ 6207
                    # και ο κωδικός αυτός υπάρχει στα Service_ID
                    # τότε να σταματήσει γιατί τρεχει το ποιο πανω loop (line 269) οταν ο κωδικός υπάρχει
                    # todo να μήν φτάνει εδώ αλλά να σταματάει στο στο line 269
                    return
                if key not in keys and key not in not_needed_keys:
                    keys.append(key)
                    if key == "ΚΩΔΙΚΟΣ":
                        added_codes.append(value)
                        data.append(value)
                        values.append('?')
                    elif key == "ΤΕΜΑΧΙΑ":
                        data.append('1')
                        values.append('?')

                    else:
                        data.append(value)
                        values.append('?')
            values.append('?')  # Για το self.copier
            values.append('?')  # Για το self.service_ID
            values.append('?')  # Για το self.customer_id
            values = ",".join(values)
            keys.append('Φωτοτυπικό')
            keys.append('Service_ID')
            keys.append('Customer_ID')
            data.append(self.copier)
            data.append(self.service_ID)
            data.append(self.customer_id)
            print("keys", keys)
            sql = ("INSERT INTO Ανταλλακτικά(" + ",".join(keys) + " )VALUES( " + values + " )")
            service_cursor.execute(sql, data)
            service_con.commit()

        # messagebox.showinfo("Info", f"Οι κωδικοί {added_codes} προστέθηκαν με επιτυχεία ")
        print(f"Line 349 Οι κωδικοί {added_codes} προστέθηκαν με επιτυχία στο service_id {self.service_ID} ")
        service_cursor.close()
        service_con.close()

        # Ενημέρωση αποθήκης -1
        con = sqlite3.connect(spare_parts_db)
        c = con.cursor()
        for code in added_codes:
            c.execute("SELECT ΤΕΜΑΧΙΑ FROM " + self.selected_company + " WHERE ΚΩΔΙΚΟΣ =?", (code,))
            old_pieces = c.fetchall()

            new_pieces = int(old_pieces[0][0]) - 1
            c.execute("UPDATE " + self.selected_company + " SET ΤΕΜΑΧΙΑ =? WHERE ΚΩΔΙΚΟΣ =?", (new_pieces, code))
            con.commit()
        print(f" Line 362 Οι κωδικοί {added_codes} αφερέθηκαν απο την αποθήκη {self.selected_company} με επιτυχία ")
        c.close()
        con.close()
        self.get_spare_parts()
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





