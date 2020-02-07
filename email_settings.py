#  -*- coding: utf-8 -*-
from tkinter import Tk, ttk, messagebox, StringVar
import tkinter as tk
import sqlite3
import sys
from settings import dbase, root_logger
# -------------ΔΗΜΗΟΥΡΓΕΙΑ LOG FILE  ------------------
sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info

smtp_server = None
ssl_port = None
port = None
sender_email = None
password = None
receiver_email = None


class SetEmailSettings:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x400+200+200")
        self.root.title("Ρυθμήσεις email")
        self.root.bind('<Escape>', self.quit)

        # Αποστολέας
        self.sender_label = tk.Label(self.root)
        self.sender_label.place(relx=0.025, rely=0.010, height=25, relwidth=0.950)
        self.sender_label.configure(activebackground="#f9f9f9")
        self.sender_label.configure(activeforeground="black")
        self.sender_label.configure(background="#006291")
        self.sender_label.configure(disabledforeground="#a3a3a3")
        self.sender_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.sender_label.configure(foreground="#ffffff")
        self.sender_label.configure(highlightbackground="#d9d9d9")
        self.sender_label.configure(highlightcolor="black")
        self.sender_label.configure(relief="groove")
        self.sender_label.configure(text='''Αποστολέας''')

        self.sender_email_label = tk.Label(self.root)
        self.sender_email_label.place(relx=0.025, rely=0.090, height=31, relwidth=0.230)
        self.sender_email_label.configure(activebackground="#f9f9f9")
        self.sender_email_label.configure(activeforeground="black")
        self.sender_email_label.configure(background="#6b6b6b")
        self.sender_email_label.configure(disabledforeground="#a3a3a3")
        self.sender_email_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.sender_email_label.configure(foreground="#ffffff")
        self.sender_email_label.configure(highlightbackground="#d9d9d9")
        self.sender_email_label.configure(highlightcolor="black")
        self.sender_email_label.configure(relief="groove")
        self.sender_email_label.configure(text='''Όνομα χρήστη''')

        self.sender_email = StringVar()
        # self.sender_email.trace('w', self.check_sender_email)
        self.sender_email_entry = tk.Entry(self.root)
        self.sender_email_entry.place(relx=0.27, rely=0.090, height=30, relwidth=0.600)
        self.sender_email_entry.configure(textvariable=self.sender_email)
        self.sender_email_entry.configure(background="white")
        self.sender_email_entry.configure(disabledforeground="#a3a3a3")
        self.sender_email_entry.configure(font="TkFixedFont")
        self.sender_email_entry.configure(foreground="#000000")
        self.sender_email_entry.configure(highlightbackground="#d9d9d9")
        self.sender_email_entry.configure(highlightcolor="black")
        self.sender_email_entry.configure(insertbackground="black")
        self.sender_email_entry.configure(selectbackground="#c4c4c4")
        self.sender_email_entry.configure(selectforeground="black")
        # self.sender_email_warning = ttk.Label(top)
        # self.sender_email_warning_img = PhotoImage(file="icons/lamp.png")
        # self.sender_email_warning.configure(background="#f6f6ee")
        # self.sender_email_warning.configure(image=self.sender_email_warning_img)
        # self.sender_email_warning.configure(compound='top')

        # Κωδικός
        self.password_label = tk.Label(self.root)
        self.password_label.place(relx=0.025, rely=0.180, height=31, relwidth=0.230)
        self.password_label.configure(activebackground="#f9f9f9")
        self.password_label.configure(activeforeground="black")
        self.password_label.configure(background="#6b6b6b")
        self.password_label.configure(disabledforeground="#a3a3a3")
        self.password_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.password_label.configure(foreground="#ffffff")
        self.password_label.configure(highlightbackground="#d9d9d9")
        self.password_label.configure(highlightcolor="black")
        self.password_label.configure(relief="groove")
        self.password_label.configure(text='''Κωδικός''')

        self.password = StringVar()
        # self.sender_email.trace('w', self.check_sender_email)
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.place(relx=0.27, rely=0.180, height=30, relwidth=0.600)
        self.password_entry.configure(textvariable=self.password)
        self.password_entry.configure(background="white")
        self.password_entry.configure(disabledforeground="#a3a3a3")
        self.password_entry.configure(font="TkFixedFont")
        self.password_entry.configure(foreground="#000000")
        self.password_entry.configure(highlightbackground="#d9d9d9")
        self.password_entry.configure(highlightcolor="black")
        self.password_entry.configure(insertbackground="black")
        self.password_entry.configure(selectbackground="#c4c4c4")
        self.password_entry.configure(selectforeground="black")

        # smtp_server
        self.smtp_server_label = tk.Label(self.root)
        self.smtp_server_label.place(relx=0.025, rely=0.270, height=31, relwidth=0.230)
        self.smtp_server_label.configure(activebackground="#f9f9f9")
        self.smtp_server_label.configure(activeforeground="black")
        self.smtp_server_label.configure(background="#6b6b6b")
        self.smtp_server_label.configure(disabledforeground="#a3a3a3")
        self.smtp_server_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.smtp_server_label.configure(foreground="#ffffff")
        self.smtp_server_label.configure(highlightbackground="#d9d9d9")
        self.smtp_server_label.configure(highlightcolor="black")
        self.smtp_server_label.configure(relief="groove")
        self.smtp_server_label.configure(text='''Smtp Server''')

        self.smtp_server = StringVar()
        # self.smtp_server.trace('w', self.check_smtp_server)
        self.smtp_server_entry = tk.Entry(self.root)
        self.smtp_server_entry.place(relx=0.27, rely=0.270, height=30, relwidth=0.600)
        self.smtp_server_entry.configure(textvariable=self.smtp_server)
        self.smtp_server_entry.configure(background="white")
        self.smtp_server_entry.configure(disabledforeground="#a3a3a3")
        self.smtp_server_entry.configure(font="TkFixedFont")
        self.smtp_server_entry.configure(foreground="#000000")
        self.smtp_server_entry.configure(highlightbackground="#d9d9d9")
        self.smtp_server_entry.configure(highlightcolor="black")
        self.smtp_server_entry.configure(insertbackground="black")
        self.smtp_server_entry.configure(selectbackground="#c4c4c4")
        self.smtp_server_entry.configure(selectforeground="black")

        # port
        self.port_label = tk.Label(self.root)
        self.port_label.place(relx=0.025, rely=0.360, height=31, relwidth=0.230)
        self.port_label.configure(activebackground="#f9f9f9")
        self.port_label.configure(activeforeground="black")
        self.port_label.configure(background="#6b6b6b")
        self.port_label.configure(disabledforeground="#a3a3a3")
        self.port_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.port_label.configure(foreground="#ffffff")
        self.port_label.configure(highlightbackground="#d9d9d9")
        self.port_label.configure(highlightcolor="black")
        self.port_label.configure(relief="groove")
        self.port_label.configure(text='''Port''')

        self.port = StringVar()
        self.port_entry = tk.Entry(self.root)
        self.port_entry.place(relx=0.27, rely=0.360, height=30, relwidth=0.150)
        self.port_entry.configure(textvariable=self.port)
        self.port_entry.configure(background="white")
        self.port_entry.configure(disabledforeground="#a3a3a3")
        self.port_entry.configure(font="TkFixedFont")
        self.port_entry.configure(foreground="#000000")
        self.port_entry.configure(highlightbackground="#d9d9d9")
        self.port_entry.configure(highlightcolor="black")
        self.port_entry.configure(insertbackground="black")
        self.port_entry.configure(selectbackground="#c4c4c4")
        self.port_entry.configure(selectforeground="black")

        # # ssl_port
        # self.ssl_port_label = tk.Label(self.root)
        # self.ssl_port_label.place(relx=0.025, rely=0.450, height=31, relwidth=0.230)
        # self.ssl_port_label.configure(activebackground="#f9f9f9")
        # self.ssl_port_label.configure(activeforeground="black")
        # self.ssl_port_label.configure(background="#6b6b6b")
        # self.ssl_port_label.configure(disabledforeground="#a3a3a3")
        # self.ssl_port_label.configure(font="-family {Calibri} -size 10 -weight bold")
        # self.ssl_port_label.configure(foreground="#ffffff")
        # self.ssl_port_label.configure(highlightbackground="#d9d9d9")
        # self.ssl_port_label.configure(highlightcolor="black")
        # self.ssl_port_label.configure(relief="groove")
        # self.ssl_port_label.configure(text='''SSL Port''')
        #
        # self.ssl_port = StringVar()
        # self.ssl_port_entry = tk.Entry(self.root)
        # self.ssl_port_entry.place(relx=0.27, rely=0.450, height=30, relwidth=0.150)
        # self.ssl_port_entry.configure(textvariable=self.ssl_port)
        # self.ssl_port_entry.configure(background="white")
        # self.ssl_port_entry.configure(disabledforeground="#a3a3a3")
        # self.ssl_port_entry.configure(font="TkFixedFont")
        # self.ssl_port_entry.configure(foreground="#000000")
        # self.ssl_port_entry.configure(highlightbackground="#d9d9d9")
        # self.ssl_port_entry.configure(highlightcolor="black")
        # self.ssl_port_entry.configure(insertbackground="black")
        # self.ssl_port_entry.configure(selectbackground="#c4c4c4")
        # self.ssl_port_entry.configure(selectforeground="black")

        # Παραλήπτης
        self.receiver_label = tk.Label(self.root)
        self.receiver_label.place(relx=0.025, rely=0.580, height=25, relwidth=0.950)
        self.receiver_label.configure(activebackground="#f9f9f9")
        self.receiver_label.configure(activeforeground="black")
        self.receiver_label.configure(background="#006291")
        self.receiver_label.configure(disabledforeground="#a3a3a3")
        self.receiver_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.receiver_label.configure(foreground="#ffffff")
        self.receiver_label.configure(highlightbackground="#d9d9d9")
        self.receiver_label.configure(highlightcolor="black")
        self.receiver_label.configure(relief="groove")
        self.receiver_label.configure(text='''Παραλήπτης''')

        # # Όνομα Παραλήπτη
        # self.receiver_name_label = tk.Label(self.root)
        # self.receiver_name_label.place(relx=0.025, rely=0.670, height=31, relwidth=0.280)
        # self.receiver_name_label.configure(activebackground="#f9f9f9")
        # self.receiver_name_label.configure(activeforeground="black")
        # self.receiver_name_label.configure(background="#6b6b6b")
        # self.receiver_name_label.configure(disabledforeground="#a3a3a3")
        # self.receiver_name_label.configure(font="-family {Calibri} -size 10 -weight bold")
        # self.receiver_name_label.configure(foreground="#ffffff")
        # self.receiver_name_label.configure(highlightbackground="#d9d9d9")
        # self.receiver_name_label.configure(highlightcolor="black")
        # self.receiver_name_label.configure(relief="groove")
        # self.receiver_name_label.configure(text='''Όνομα παραλήπτη''')
        #
        # self.receiver_name = StringVar()
        # self.receiver_name_entry = tk.Entry(self.root)
        # self.receiver_name_entry.place(relx=0.320, rely=0.670, height=30, relwidth=0.600)
        # self.receiver_name_entry.configure(textvariable=self.receiver_name)
        # self.receiver_name_entry.configure(background="white")
        # self.receiver_name_entry.configure(disabledforeground="#a3a3a3")
        # self.receiver_name_entry.configure(font="TkFixedFont")
        # self.receiver_name_entry.configure(foreground="#000000")
        # self.receiver_name_entry.configure(highlightbackground="#d9d9d9")
        # self.receiver_name_entry.configure(highlightcolor="black")
        # self.receiver_name_entry.configure(insertbackground="black")
        # self.receiver_name_entry.configure(selectbackground="#c4c4c4")
        # self.receiver_name_entry.configure(selectforeground="black")

        # Email Παραλήπτη
        self.receiver_email_label = tk.Label(self.root)
        self.receiver_email_label.place(relx=0.025, rely=0.760, height=31, relwidth=0.280)
        self.receiver_email_label.configure(activebackground="#f9f9f9")
        self.receiver_email_label.configure(activeforeground="black")
        self.receiver_email_label.configure(background="#6b6b6b")
        self.receiver_email_label.configure(disabledforeground="#a3a3a3")
        self.receiver_email_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.receiver_email_label.configure(foreground="#ffffff")
        self.receiver_email_label.configure(highlightbackground="#d9d9d9")
        self.receiver_email_label.configure(highlightcolor="black")
        self.receiver_email_label.configure(relief="groove")
        self.receiver_email_label.configure(text='''E-mail παραλήπτη''')

        self.receiver_email = StringVar()
        self.receiver_email_entry = tk.Entry(self.root)
        self.receiver_email_entry.place(relx=0.320, rely=0.760, height=30, relwidth=0.600)
        self.receiver_email_entry.configure(textvariable=self.receiver_email)
        self.receiver_email_entry.configure(background="white")
        self.receiver_email_entry.configure(disabledforeground="#a3a3a3")
        self.receiver_email_entry.configure(font="TkFixedFont")
        self.receiver_email_entry.configure(foreground="#000000")
        self.receiver_email_entry.configure(highlightbackground="#d9d9d9")
        self.receiver_email_entry.configure(highlightcolor="black")
        self.receiver_email_entry.configure(insertbackground="black")
        self.receiver_email_entry.configure(selectbackground="#c4c4c4")
        self.receiver_email_entry.configure(selectforeground="black")

        # Αποθήκευση
        self.save_btn = tk.Button(self.root)
        self.save_btn.place(relx=0.350, rely=0.900, height="30", relwidth=0.200)
        self.save_btn.configure(foreground="white")
        self.save_btn.configure(text="Αποθήκευση")
        self.save_btn.configure(background="#5fa15f")
        self.save_btn.configure(command=self.save_settings)

    def save_settings(self):
        email_data = [self.sender_email_entry.get(), self.password_entry.get(), self.smtp_server_entry.get(),
                      self.port_entry.get()]

        con = sqlite3.connect(dbase)
        c = con.cursor()
        sql = "INSERT INTO Sender_emails(sender_email, password, smtp_server, port)VALUES(?,?,?,?)"
        try:
            if "@" in self.sender_email_entry.get():
                c.execute(sql, tuple(email_data,))
            if "@" in self.receiver_email_entry.get():
                c.execute("INSERT INTO Receiver_emails(Receiver_email)VALUES(?)", (self.receiver_email_entry.get(),))

        except sqlite3.IntegrityError as error:
            messagebox.showerror("Σφάλμα", f"{error}")
            con.close()
            return
        con.commit()
        con.close()
        messagebox.showinfo("Προσοχή!", "Τα στοιχεία αποθηκέυτηκαν")
        self.root.destroy()

    def quit(self, event):
        self.root.destroy()


if __name__ == "__main__":
    set_mail = SetEmailSettings()
    set_mail.root.mainloop()


def run_email_settings():
    run_mail = SetEmailSettings()
    run_mail.root.mainloop()


