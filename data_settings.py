#  -*- coding: utf-8 -*-
import sqlite3
import sys
import tkinter as tk
from tkinter import ttk, messagebox, PhotoImage

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


def get_service_data():
    con = sqlite3.connect(dbase)
    c = con.cursor()
    c.execute("SELECT Σκοπός FROM Service_data;")
    purposes = c.fetchall()
    c.execute("SELECT Ενέργειες FROM Service_data;")
    actions = c.fetchall()
    con.close()

    purposes_lists = []
    actions_list = []
    for n in range(len(purposes)):
        if purposes[n][0] != "" and purposes[n][0] is not None:
            purposes_lists.append(purposes[n][0])

    for n in range(len(actions)):
        if actions[n][0] != "" and actions[n][0] is not None:
            actions_list.append(actions[n][0])

    return sorted(purposes_lists), sorted(actions_list)


def get_companies():
    con = sqlite3.connect(dbase)
    c = con.cursor()
    c.execute("SELECT Εταιρεία FROM Companies;")
    companies = c.fetchall()
    c.execute("SELECT Μοντέλο FROM Companies;")
    models = c.fetchall()
    con.close()

    companies_list = []
    models_list = []
    for n in range(len(companies)):
        if companies[n][0] != "" and companies[n][0] is not None:
            companies_list.append(companies[n][0])

    for n in range(len(models)):
        if models[n][0] != "" and models[n][0] is not None:
            models_list.append(models[n][0])

    return sorted(companies_list), sorted(models_list)

class SetDataSettings:
    def __init__(self, top=None):
        self.root = top
        self.root.geometry("420x350+200+200")
        self.root.title("Ρυθμήσεις Service Data")
        self.root.bind('<Escape>', self.quit)
        self.purposes, self.actions = get_service_data()
        self.companies, self.models = get_companies()
        # Σκοπός
        self.purpose_big_label = tk.Label(self.root)
        self.purpose_big_label.place(relx=0.025, rely=0.010, height=25, relwidth=0.960)
        self.purpose_big_label.configure(activebackground="#f9f9f9")
        self.purpose_big_label.configure(activeforeground="black")
        self.purpose_big_label.configure(background="#006291")
        self.purpose_big_label.configure(disabledforeground="#a3a3a3")
        self.purpose_big_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.purpose_big_label.configure(foreground="#ffffff")
        self.purpose_big_label.configure(highlightbackground="#d9d9d9")
        self.purpose_big_label.configure(highlightcolor="black")
        self.purpose_big_label.configure(relief="groove")
        self.purpose_big_label.configure(text='''Δεδομένα Service''')

        self.purpose_label = tk.Label(self.root)
        self.purpose_label.place(relx=0.025, rely=0.120, height=31, relwidth=0.250)
        self.purpose_label.configure(activebackground="#f9f9f9")
        self.purpose_label.configure(activeforeground="black")
        self.purpose_label.configure(background="#6b6b6b")
        self.purpose_label.configure(disabledforeground="#a3a3a3")
        self.purpose_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.purpose_label.configure(foreground="#ffffff")
        self.purpose_label.configure(highlightbackground="#d9d9d9")
        self.purpose_label.configure(highlightcolor="black")
        self.purpose_label.configure(relief="groove")
        self.purpose_label.configure(text='''Περιγρ.Προβλήμ.''')
        self.purpose_combobox = ttk.Combobox(self.root)
        self.purpose_combobox.place(relx=0.300, rely=0.120, height=31, relwidth=0.600)
        self.purpose_combobox.configure(values=self.purposes)
        # self.purpose_combobox.configure(state="readonly")
        # self.purpose_combobox.bind("<<ComboboxSelected>>", self.show_purposes_details)
        self.del_purpose_btn = tk.Button(self.root)
        self.del_purpose_btn.place(relx=0.900, rely=0.120, height=30, relwidth=0.080)
        self.del_purpose_btn.configure(background="#0685c4")
        self.del_purpose_btn_img = PhotoImage(file="icons/delete_service_data.png")
        self.del_purpose_btn.configure(image=self.del_purpose_btn_img)
        self.del_purpose_btn.configure(command=self.del_purpose)

        self.actions_label = tk.Label(self.root)
        self.actions_label.place(relx=0.025, rely=0.220, height=31, relwidth=0.250)
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
        self.actions_combobox = ttk.Combobox(self.root)
        self.actions_combobox.place(relx=0.30, rely=0.220, height=31, relwidth=0.600)
        self.actions_combobox.configure(values=self.actions)
        # self.purpose_combobox.configure(state="readonly")
        # self.purpose_combobox.bind("<<ComboboxSelected>>", self.show_purposes_details)
        self.del_actions_btn = tk.Button(self.root)
        self.del_actions_btn.place(relx=0.900, rely=0.220, height=30, relwidth=0.080)
        self.del_actions_btn.configure(background="#0685c4")
        self.del_actions_btn_img = PhotoImage(file="icons/delete_service_data.png")
        self.del_actions_btn.configure(image=self.del_actions_btn_img)
        self.del_actions_btn.configure(command=self.del_action)

        # Αποθήκευση
        self.save_btn = tk.Button(self.root)
        self.save_btn.place(relx=0.350, rely=0.340, height="30", relwidth=0.200)
        self.save_btn.configure(foreground="white")
        self.save_btn.configure(text="Αποθήκευση")
        self.save_btn.configure(background="#5fa15f")
        self.save_btn.configure(command=self.save_settings)

        # Comapnies
        self.companies_label = tk.Label(self.root)
        self.companies_label.place(relx=0.025, rely=0.480, height=31, relwidth=0.250)
        self.companies_label.configure(activebackground="#f9f9f9")
        self.companies_label.configure(activeforeground="black")
        self.companies_label.configure(background="#6b6b6b")
        self.companies_label.configure(disabledforeground="#a3a3a3")
        self.companies_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.companies_label.configure(foreground="#ffffff")
        self.companies_label.configure(highlightbackground="#d9d9d9")
        self.companies_label.configure(highlightcolor="black")
        self.companies_label.configure(relief="groove")
        self.companies_label.configure(text='''Εταιρεία''')
        self.companies_combobox = ttk.Combobox(self.root)
        self.companies_combobox.place(relx=0.30, rely=0.480, height=31, relwidth=0.600)
        self.companies_combobox.configure(values=self.companies)
        # self.purpose_combobox.configure(state="readonly")
        # self.purpose_combobox.bind("<<ComboboxSelected>>", self.show_purposes_details)
        self.del_companies_btn = tk.Button(self.root)
        self.del_companies_btn.place(relx=0.900, rely=0.480, height=30, relwidth=0.080)
        self.del_companies_btn.configure(background="#0685c4")
        self.del_companies_btn_img = PhotoImage(file="icons/delete_service_data.png")
        self.del_companies_btn.configure(image=self.del_companies_btn_img)
        self.del_companies_btn.configure(command=self.del_company)

        self.models_label = tk.Label(self.root)
        self.models_label.place(relx=0.025, rely=0.580, height=31, relwidth=0.250)
        self.models_label.configure(activebackground="#f9f9f9")
        self.models_label.configure(activeforeground="black")
        self.models_label.configure(background="#6b6b6b")
        self.models_label.configure(disabledforeground="#a3a3a3")
        self.models_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.models_label.configure(foreground="#ffffff")
        self.models_label.configure(highlightbackground="#d9d9d9")
        self.models_label.configure(highlightcolor="black")
        self.models_label.configure(relief="groove")
        self.models_label.configure(text='''Μοντέλο''')
        self.models_combobox = ttk.Combobox(self.root)
        self.models_combobox.place(relx=0.30, rely=0.580, height=31, relwidth=0.600)
        self.models_combobox.configure(values=self.models)
        # self.purpose_combobox.configure(state="readonly")
        # self.purpose_combobox.bind("<<ComboboxSelected>>", self.show_purposes_details)
        self.del_models_btn = tk.Button(self.root)
        self.del_models_btn.place(relx=0.900, rely=0.580, height=30, relwidth=0.080)
        self.del_models_btn.configure(background="#0685c4")
        self.del_models_btn_img = PhotoImage(file="icons/delete_service_data.png")
        self.del_models_btn.configure(image=self.del_models_btn_img)
        self.del_models_btn.configure(command=self.del_model)

        # Αποθήκευση
        self.save_companies_btn = tk.Button(self.root)
        self.save_companies_btn.place(relx=0.350, rely=0.700, height="30", relwidth=0.200)
        self.save_companies_btn.configure(foreground="white")
        self.save_companies_btn.configure(text="Αποθήκευση")
        self.save_companies_btn.configure(background="#5fa15f")
        self.save_companies_btn.configure(command=self.save_companies)

    def del_company(self):
        company = self.companies_combobox.get()
        if company == "" or company == " ":
            return
        answer = messagebox.askyesno("Προσοχή!", f"Ειστε σήγουρος για την διαγραφή του {company}")
        if answer:

            con = sqlite3.connect(dbase)
            c = con.cursor()
            c.execute("DELETE FROM Companies WHERE Εταιρεία=?", (company,))
            con.commit()
            con.close()
            self.companies, self.models = get_companies()

            self.companies_combobox.configure(values=self.companies)
            try:
                self.companies_combobox.set(value=self.companies[0])
            except IndexError:  # Οταν δεν έχουμε αποστολέα
                self.companies_combobox.set(value=" ")

            messagebox.showwarning("Προσοχή", f"H {company}, διαγάφηκε")
            self.root.focus()
        else:
            self.root.focus()
            return

    def del_model(self):
        model = self.models_combobox.get()
        if model == "" or model == " ":
            return
        answer = messagebox.askyesno("Προσοχή!", f"Ειστε σήγουρος για την διαγραφή του {model}")
        if answer:

            con = sqlite3.connect(dbase)
            c = con.cursor()
            c.execute("DELETE FROM Companies WHERE Μοντέλο=?", (model,))
            con.commit()
            con.close()
            self.companies, self.models = get_companies()

            self.models_combobox.configure(values=self.models)
            try:
                self.models_combobox.set(value=self.models[0])
            except IndexError:  # Οταν δεν έχουμε αποστολέα
                self.models_combobox.set(value=" ")

            messagebox.showwarning("Προσοχή", f"To {model}, διαγάφηκε")
            self.root.focus()
        else:
            self.root.focus()
            return

    def del_purpose(self):
        purpose = self.purpose_combobox.get()
        if purpose == "" or purpose == " ":
            return
        answer = messagebox.askyesno("Προσοχή!", f"Ειστε σήγουρος για την διαγραφή του {purpose}")
        if answer:

            con = sqlite3.connect(dbase)
            c = con.cursor()
            c.execute("DELETE FROM Service_data WHERE Σκοπός=?", (purpose,))
            con.commit()
            con.close()
            self.purposes, self.actions = get_service_data()

            self.purpose_combobox.configure(values=self.purposes)
            try:
                self.purpose_combobox.set(value=self.purposes[0])
            except IndexError:  # Οταν δεν έχουμε αποστολέα
                self.purpose_combobox.set(value=" ")

            messagebox.showwarning("Προσοχή", f"Το {purpose}, διαγάφηκε")
            self.root.focus()
        else:
            self.root.focus()
            return

    def del_action(self):
        action = self.actions_combobox.get()
        if action == "" or action == " ":
            return
        answer = messagebox.askyesno("Προσοχή!", f"Ειστε σήγουρος για την διαγραφή του {action}")
        if answer:

            con = sqlite3.connect(dbase)
            c = con.cursor()
            c.execute("DELETE FROM Service_data WHERE Ενέργειες=?", (action,))
            con.commit()
            con.close()
            self.purposes, self.actions = get_service_data()

            self.actions_combobox.configure(values=self.actions)
            try:
                self.actions_combobox.set(value=self.actions[0])
            except IndexError:  # Οταν δεν έχουμε αποστολέα
                self.actions_combobox.set(value=" ")

            messagebox.showwarning("Προσοχή", f"Το {action}, διαγάφηκε")
            self.root.focus()
        else:
            self.root.focus()
            return

    def save_settings(self):
        if self.purpose_combobox.get() in self.purposes:
            messagebox.showinfo("Προσοχή", f"Το {self.purpose_combobox.get()} υπάρχει στην λίστα περιγραφή προβλήματος")
            self.root.focus()
            return None
        elif self.actions_combobox.get() in self.actions:
            messagebox.showinfo("Προσοχή", f"Το {self.actions_combobox.get()} υπάρχει στην λίστα ενέργειες!")
            self.root.focus()
            return None

        else:
            conn = sqlite3.connect(dbase)
            cursor = conn.cursor()
            # "INSERT INTO  " + table + "(" + culumns + ")" + "VALUES(NULL, ?, ?, ?, ?, ?, ?, ?);"
            # INSERT INTO artists (name)VALUES('Bud Powell');
            if self.purpose_combobox.get() != "":
                sql = "INSERT INTO Service_data (Σκοπός)VALUES(?);"
                cursor.execute(sql, (self.purpose_combobox.get(),))
            if self.actions_combobox.get() != "":
                sql1 = "INSERT INTO Service_data(Ενέργειες)VALUES(?);"
                cursor.execute(sql1, (self.actions_combobox.get(),))
            conn.commit()
            cursor.close()
            conn.close()
            self.purposes, self.actions = get_service_data()
            self.purpose_combobox.configure(values=self.purposes)
            self.actions_combobox.configure(values=self.actions)

            messagebox.showinfo("Info", f"Τα στοιχεία προστέθηκαν επιτυχώς")
            self.root.focus()

    def save_companies(self):
        if self.companies_combobox.get() in self.companies:
            messagebox.showinfo("Προσοχή", f"Το {self.companies_combobox.get()} υπάρχει στην λίστα")
            self.root.focus()
            return None
        elif self.models_combobox.get() in self.actions:
            messagebox.showinfo("Προσοχή", f"Το {self.models_combobox.get()} υπάρχει στην λίστα!")
            self.root.focus()
            return None

        else:
            conn = sqlite3.connect(dbase)
            cursor = conn.cursor()
            # "INSERT INTO  " + table + "(" + culumns + ")" + "VALUES(NULL, ?, ?, ?, ?, ?, ?, ?);"
            # INSERT INTO artists (name)VALUES('Bud Powell');
            if self.companies_combobox.get() != "":
                sql = "INSERT INTO Companies(Εταιρεία)VALUES(?);"
                cursor.execute(sql, (self.companies_combobox.get(),))
            if self.models_combobox.get() != "":
                sql1 = "INSERT INTO Companies(Μοντέλο)VALUES(?);"
                cursor.execute(sql1, (self.models_combobox.get(),))
            conn.commit()
            cursor.close()
            conn.close()
            self.companies, self.models = get_companies()
            self.companies_combobox.configure(values=self.companies)
            self.models_combobox.configure(values=self.models)

            messagebox.showinfo("Info", f"Τα στοιχεία προστέθηκαν επιτυχώς")
            self.root.focus()


    def quit(self, event):
        self.root.destroy()


if __name__ == "__main__":
    set_mail = SetDataSettings()
    set_mail.root.mainloop()

rt = None


def run_data_settings(root):
    global rt
    rt = root
    w = tk.Toplevel(root)
    run_mail = SetDataSettings(w)
    run_mail.root.mainloop()


