#  -*- coding: utf-8 -*-
from tkinter import Tk, ttk, messagebox, StringVar, PhotoImage
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


def get_senders_emails():
    con = sqlite3.connect(dbase)
    c = con.cursor()
    c.execute("SELECT * FROM Sender_emails;")
    sender_email_data = c.fetchall()
    c.execute("SELECT * FROM Receiver_emails;")
    receiver_email_data = c.fetchall()
    con.close()

    senders = []
    receivers = []
    for n in range(len(sender_email_data)):
        senders.append(sender_email_data[n][1])

    for n in range(len(receiver_email_data)):
        receivers.append(receiver_email_data[n][1])

    return senders, receivers

class SetEmailSettings:
    def __init__(self, top=None):
        self.root = top
        self.root.geometry("400x400+200+200")
        self.root.title("Ρυθμήσεις email")
        self.root.bind('<Escape>', self.quit)
        self.senders, self.receivers = get_senders_emails()
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

        self.sender_label = tk.Label(self.root)
        self.sender_label.place(relx=0.025, rely=0.090, height=31, relwidth=0.230)
        self.sender_label.configure(activebackground="#f9f9f9")
        self.sender_label.configure(activeforeground="black")
        self.sender_label.configure(background="#6b6b6b")
        self.sender_label.configure(disabledforeground="#a3a3a3")
        self.sender_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.sender_label.configure(foreground="#ffffff")
        self.sender_label.configure(highlightbackground="#d9d9d9")
        self.sender_label.configure(highlightcolor="black")
        self.sender_label.configure(relief="groove")
        self.sender_label.configure(text='''Λογαριασμοί''')
        self.senders_combobox = ttk.Combobox(self.root)
        self.senders_combobox.place(relx=0.27, rely=0.090, height=31, relwidth=0.600)
        self.senders_combobox.configure(values=self.senders)
        self.senders_combobox.configure(state="readonly")
        self.senders_combobox.bind("<<ComboboxSelected>>", self.show_sender_details)
        self.del_sender_btn = tk.Button(self.root)
        self.del_sender_btn.place(relx=0.900, rely=0.090, height=30, relwidth=0.080)
        self.del_sender_btn.configure(background="#0685c4")
        self.del_sender_btn_img = PhotoImage(file="icons/del_sender.png")
        self.del_sender_btn.configure(image=self.del_sender_btn_img)
        self.del_sender_btn.configure(command=self.del_sender)

        self.sender_email_label = tk.Label(self.root)
        self.sender_email_label.place(relx=0.025, rely=0.190, height=31, relwidth=0.230)
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
        self.sender_email_entry.place(relx=0.27, rely=0.190, height=30, relwidth=0.600)
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
        self.password_label.place(relx=0.025, rely=0.280, height=31, relwidth=0.230)
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
        self.password_entry.place(relx=0.27, rely=0.280, height=30, relwidth=0.600)
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
        self.smtp_server_label.place(relx=0.025, rely=0.370, height=31, relwidth=0.230)
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
        self.smtp_server_entry.place(relx=0.27, rely=0.370, height=30, relwidth=0.600)
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
        self.port_label.place(relx=0.025, rely=0.460, height=31, relwidth=0.230)
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
        self.port_entry.place(relx=0.27, rely=0.460, height=30, relwidth=0.150)
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

        self.receivers_label = tk.Label(self.root)
        self.receivers_label.place(relx=0.025, rely=0.670, height=31, relwidth=0.230)
        self.receivers_label.configure(activebackground="#f9f9f9")
        self.receivers_label.configure(activeforeground="black")
        self.receivers_label.configure(background="#6b6b6b")
        self.receivers_label.configure(disabledforeground="#a3a3a3")
        self.receivers_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.receivers_label.configure(foreground="#ffffff")
        self.receivers_label.configure(highlightbackground="#d9d9d9")
        self.receivers_label.configure(highlightcolor="black")
        self.receivers_label.configure(relief="groove")
        self.receivers_label.configure(text='''Παραλήπτες''')
        self.receivers_combobox = ttk.Combobox(self.root)
        self.receivers_combobox.place(relx=0.27, rely=0.670, height=31, relwidth=0.600)
        self.receivers_combobox.configure(values=self.receivers)
        self.receivers_combobox.configure(state="readonly")  #

        self.del_receivers_btn = tk.Button(self.root)
        self.del_receivers_btn.place(relx=0.900, rely=0.670, height=30, relwidth=0.080)
        self.del_receivers_btn.configure(background="#0685c4")
        self.del_receivers_btn_img = PhotoImage(file="icons/del_sender.png")
        self.del_receivers_btn.configure(image=self.del_sender_btn_img)
        self.del_receivers_btn.configure(command=self.delete_receiver)

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

    def show_sender_details(self, event=None):
        sender = self.senders_combobox.get()
        con = sqlite3.connect(dbase)
        c = con.cursor()
        c.execute("SELECT * FROM Sender_emails WHERE sender_email=?", (sender,))
        data = c.fetchall()
        con.close()
        try:
            email_var = StringVar(value=data[0][1])
            self.sender_email_entry.configure(textvariable=email_var)
            pass_var = StringVar(value=data[0][2])
            self.password_entry.configure(textvariable=pass_var, show="*")
            smtp_var = StringVar(value=data[0][3])
            self.smtp_server_entry.configure(textvariable=smtp_var)
            port_var = StringVar(value=data[0][4])
            self.port_entry.configure(textvariable=port_var)
        except IndexError:  # Οταν δεν έχουμε αποστολέα
            pass

    def del_sender(self):
        sender = self.senders_combobox.get()
        if sender == "" or sender == " ":
            return
        answer = messagebox.askyesno("Προσοχή!", f"Ειστε σήγουρος για την διαγραφή του {self.senders_combobox.get()}")
        if answer:

            con = sqlite3.connect(dbase)
            c = con.cursor()
            c.execute("DELETE FROM Sender_emails WHERE sender_email=?", (sender,))
            con.commit()
            con.close()
            self.senders, self.receivers = get_senders_emails()

            self.senders_combobox.configure(values=self.senders)
            try:
                self.senders_combobox.set(value=self.senders[0])
            except IndexError:  # Οταν δεν έχουμε αποστολέα
                self.senders_combobox.set(value=" ")

            empty_var = StringVar(value="")
            self.sender_email_entry.configure(textvariable=empty_var)
            self.password_entry.configure(textvariable=empty_var)
            self.smtp_server_entry.configure(textvariable=empty_var)
            self.port_entry.configure(textvariable=empty_var)
            messagebox.showwarning("Προσοχή", f"O {sender}, διαγάφηκε")
            self.root.focus()
        else:
            self.root.focus()
            return

    def delete_receiver(self):
        receiver = self.receivers_combobox.get()
        if receiver == "" or receiver == " ":
            return
        answer = messagebox.askyesno("Προσοχή!", f"Ειστε σήγουρος για την διαγραφή του {self.receivers_combobox.get()}")
        if answer:
            con = sqlite3.connect(dbase)
            c = con.cursor()
            c.execute("DELETE FROM Receiver_emails WHERE Receiver_email=?", (receiver,))
            con.commit()
            con.close()
            self.senders, self.receivers = get_senders_emails()
            self.receivers_combobox.configure(values=self.receivers)
            try:
                self.receivers_combobox.set(value=self.receivers[0])
            except IndexError:  # Οταν δεν έχουμε αποστολέα
                self.receivers_combobox.set(value=" ")
            messagebox.showwarning("Προσοχή", f"O {receiver}, διαγάφηκε")
            self.root.focus()
        else:
            self.root.focus()
            return

    def save_settings(self):
        email_data = [self.sender_email_entry.get(), self.password_entry.get(), self.smtp_server_entry.get(),
                      self.port_entry.get()]

        con = sqlite3.connect(dbase)
        c = con.cursor()
        sql = "INSERT INTO Sender_emails(sender_email, password, smtp_server, port)VALUES(?,?,?,?)"
        error = -1
        try:
            if "@" in self.sender_email_entry.get():
                c.execute(sql, tuple(email_data,))
            else:
                error += 1
                messagebox.showerror("Σφάλμα!", f"Μη έγκυρο email αποστολέα\nΟ αποστολέας δεν θα αποθυκευτή")
            if "@" in self.receiver_email_entry.get():
                c.execute("INSERT INTO Receiver_emails(Receiver_email)VALUES(?)", (self.receiver_email_entry.get(),))
            else:
                error += 1
                messagebox.showerror("Σφάλμα!", f"Μη έγκυρο email παραλήπτη\nΟ παραλήπτης δεν θα αποθυκευτή")

        except sqlite3.IntegrityError as error:
            messagebox.showerror("Σφάλμα", f"{error}")
            con.close()
            return
        if error:
            con.close()
            messagebox.showerror("Προσοχή!", "Τίποτα δεν αποθηκέυτηκε")
            self.root.focus()
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

rt = None

def run_email_settings(root):
    global rt
    rt = root
    w = tk.Toplevel(root)
    run_mail = SetEmailSettings(w)
    run_mail.root.mainloop()


