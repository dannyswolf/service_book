#  -*- coding: utf-8 -*-
import hashlib
import sqlite3
import sys
import tkinter as tk
from tkinter import Tk, messagebox, StringVar

from settings import dbase, root_logger, demo

# -------------ΔΗΜΗΟΥΡΓΕΙΑ LOG FILE  ------------------
sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info



class activate:
    def __init__(self):

        self.root = Tk()
        self.root.geometry("350x150+200+200")
        self.root.title("Ενεργοποίηση")
        self.root.bind('<Escape>', self.quit)

        # εμαιλ
        self.key_label = tk.Label(self.root)
        self.key_label.place(relx=0.025, rely=0.090, height=31, relwidth=0.230)
        self.key_label.configure(activebackground="#f9f9f9")
        self.key_label.configure(activeforeground="black")
        self.key_label.configure(background="#6b6b6b")
        self.key_label.configure(disabledforeground="#a3a3a3")
        self.key_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.key_label.configure(foreground="#ffffff")
        self.key_label.configure(highlightbackground="#d9d9d9")
        self.key_label.configure(highlightcolor="black")
        self.key_label.configure(relief="groove")
        self.key_label.configure(text='''Κλειδί''')

        self.key = StringVar()
        # self.sender_email.trace('w', self.check_sender_email)
        self.key_entry = tk.Entry(self.root)
        self.key_entry.place(relx=0.27, rely=0.090, height=30, relwidth=0.600)
        self.key_entry.configure(textvariable=self.key)
        self.key_entry.configure(background="white")
        self.key_entry.configure(disabledforeground="#a3a3a3")
        self.key_entry.configure(font="TkFixedFont")
        self.key_entry.configure(foreground="#000000")
        self.key_entry.configure(highlightbackground="#d9d9d9")
        self.key_entry.configure(highlightcolor="black")
        self.key_entry.configure(insertbackground="black")
        self.key_entry.configure(selectbackground="#c4c4c4")
        self.key_entry.configure(selectforeground="black")

        self.email_label = tk.Label(self.root)
        self.email_label.place(relx=0.025, rely=0.350, height=31, relwidth=0.230)
        self.email_label.configure(activebackground="#f9f9f9")
        self.email_label.configure(activeforeground="black")
        self.email_label.configure(background="#6b6b6b")
        self.email_label.configure(disabledforeground="#a3a3a3")
        self.email_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.email_label.configure(foreground="#ffffff")
        self.email_label.configure(highlightbackground="#d9d9d9")
        self.email_label.configure(highlightcolor="black")
        self.email_label.configure(relief="groove")
        self.email_label.configure(text='''E-mail''')

        self.email = StringVar()
        # self.sender_email.trace('w', self.check_sender_email)
        self.email_entry = tk.Entry(self.root)
        self.email_entry.place(relx=0.27, rely=0.350, height=30, relwidth=0.600)
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

        # self.sender_email_warning = ttk.Label(top)
        # self.sender_email_warning_img = PhotoImage(file="icons/lamp.png")
        # self.sender_email_warning.configure(background="#f6f6ee")
        # self.sender_email_warning.configure(image=self.sender_email_warning_img)
        # self.sender_email_warning.configure(compound='top')

        # Login Btn
        self.activate_btn = tk.Button(self.root)
        self.activate_btn.place(relx=0.350, rely=0.650, height="30", relwidth=0.280)
        self.activate_btn.configure(foreground="white")
        self.activate_btn.configure(text="Ενεργοποίηση")
        self.activate_btn.configure(background="#5fa15f")
        self.activate_btn.configure(command=self.activate)

    def activate(self):

        con = sqlite3.connect(dbase)
        c = con.cursor()
        c.execute("UPDATE sqlite_sequence SET seq=?  WHERE name ='key'", (self.key_entry.get(),))
        con.commit()
        con.close()
        my_key = self.email_entry.get()
        # Assumes the default UTF-8
        hash_object = hashlib.md5(my_key.encode())

        if self.key_entry.get() == hash_object.hexdigest():
            con = sqlite3.connect(dbase)
            c = con.cursor()
            c.execute("UPDATE  sqlite_sequence SET seq = 0 WHERE name ='demo'")
            c.execute("UPDATE sqlite_sequence SET seq = ? WHERE name ='customer_email'", (self.email_entry.get(),))
            con.commit()
            con.close()
            messagebox.showinfo("Ενεργοποίηση", "Η ενεργοποίηση ήταν επιτυχής\nΠαρακαλώ κλείστε και ανοίξτε ξανά το πρόγραμμα")
            self.root.destroy()
        else:
            messagebox.showerror("Ενεργοποίηση", "Η ενεργοποίηση δεν ήταν επιτυχής")
            self.root.focus()
            return

    def quit(self, event):
        self.root.destroy()


if __name__ == "__main__":
    set_mail = activate()
    set_mail.root.mainloop()


def run_activate():
    if not demo:
        con = sqlite3.connect(dbase)
        c = con.cursor()
        c.execute("SELECT seq from sqlite_sequence WHERE name ='customer_email'")
        name = c.fetchall()
        messagebox.showinfo("Προσοχή", f'Η εφαρμογή ειναι ενεργοποιημένη στο email {name[0][0]}')
        return
    run_mail = activate()
    run_mail.root.mainloop()


