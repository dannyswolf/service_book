#  -*- coding: utf-8 -*-
import datetime
import sys
import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename

from settings import user, root_logger, dbase  # settings
from tkinter import Tk, ttk, messagebox, PhotoImage
from tkinter.ttk import Progressbar
import tkinter as tk
import time
import sqlite3
import shutil  # για διαγραφη των φακέλων με τις εικόνες
# -------------ΔΗΜΗΟΥΡΓΕΙΑ LOG FILE  ------------------
sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info
print(f"{100 * '*'}\n\t\t\t\t\t\t\t\t\t\tFILE {__name__}")



rt = None
w = None


def send_mail(root, data):
    global rt, w
    rt = root
    w = tk.Toplevel(root)

    top = Mail(w, data)


class Mail:
    def __init__(self, top=None, *args):
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('clam')
        self.top = top
        self.data = args[0]
        self.top.geometry("400x350+300+300")
        self.top.title("Αποστολή e-mail")

        self.senders = []
        self.receivers = []
        self.smtp_server = ""
        self.port = ""
        self.password = ""
        self.receiver_email = ""
        # Όνομα Αποστολέα
        self.sender_email_label = tk.Label(self.top)
        self.sender_email_label.place(relx=0.005, rely=0.050, height=31, relwidth=0.280)
        self.sender_email_label.configure(activebackground="#f9f9f9")
        self.sender_email_label.configure(activeforeground="black")
        self.sender_email_label.configure(background="#6b6b6b")
        self.sender_email_label.configure(disabledforeground="#a3a3a3")
        self.sender_email_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.sender_email_label.configure(foreground="#ffffff")
        self.sender_email_label.configure(highlightbackground="#d9d9d9")
        self.sender_email_label.configure(highlightcolor="black")
        self.sender_email_label.configure(relief="groove")
        self.sender_email_label.configure(text='''Αποστολέας''')

        self.senders_combobox = ttk.Combobox(self.top)
        self.senders_combobox.place(relx=0.29, rely=0.050, height=31, relwidth=0.600)
        self.senders_combobox.configure(values=self.senders)
        self.senders_combobox.configure(takefocus="")
        # senders_combobox.bind("<<ComboboxSelected>>", self.get_repository)
        self.senders_combobox.configure(state="readonly")
        # self.senders_combobox.set(value=self.senders[0])

        # Email Παραλήπτη
        self.receiver_email_label = tk.Label(self.top)
        self.receiver_email_label.place(relx=0.005, rely=0.250, height=31, relwidth=0.280)
        self.receiver_email_label.configure(activebackground="#f9f9f9")
        self.receiver_email_label.configure(activeforeground="black")
        self.receiver_email_label.configure(background="#6b6b6b")
        self.receiver_email_label.configure(disabledforeground="#a3a3a3")
        self.receiver_email_label.configure(font="-family {Calibri} -size 10 -weight bold")
        self.receiver_email_label.configure(foreground="#ffffff")
        self.receiver_email_label.configure(highlightbackground="#d9d9d9")
        self.receiver_email_label.configure(highlightcolor="black")
        self.receiver_email_label.configure(relief="groove")
        self.receiver_email_label.configure(text='''Ε-mail παραλήπτη''')
        self.receiver_combobox = ttk.Combobox(self.top)
        self.receiver_combobox.place(relx=0.29, rely=0.250, height=31, relwidth=0.600)
        self.receiver_combobox.configure(values=self.receivers)
        self.receiver_combobox.configure(takefocus="")
        # self.receiver_combobox.set(value=self.receivers[0])
        # senders_combobox.bind("<<ComboboxSelected>>", self.get_repository)
        # receiver_combobox.configure(state="readonly")

        # Progress bar widget
        self.style = ttk.Style()
        self.style.theme_use('clam')
        # options troughcolor='green', bordercolor=TROUGH_COLOR,  lightcolor=BAR_COLOR, darkcolor=BAR_COLOR
        self.style.configure("green.Horizontal.TProgressbar",  bordercolor="black", background='green')
        self.progress = Progressbar(self.top, style="green.Horizontal.TProgressbar", orient='horizontal', length=100, mode='determinate')
        self.progress["maximum"] = 100
        self.progress.place(relx=0.29, rely=0.350, relheight=0.060, relwidth=0.600)

        self.send_btn = tk.Button(self.top, text="Αποστολή", command=self.set_receiver)
        self.send_btn.configure(background="green")
        self.send_btn.configure(foreground="white")
        self.send_btn.place(relx=0.29, rely=0.450, height=31, relwidth=0.200)

        # Ανανέωση μετα απο Προσθήκη Φωτοτυπικού
        self.refresh_emails_btn = tk.Button(self.top)
        self.refresh_emails_btn.place(relx=0.900, rely=0.050, height=30, relwidth=0.080)
        self.refresh_emails_btn.configure(background="#0685c4")
        self.refresh_emails_btn_img = PhotoImage(file="icons/refresh.png")
        self.refresh_emails_btn.configure(image=self.refresh_emails_btn_img)
        self.refresh_emails_btn.configure(command=self.get_senders_emails)

        self.get_senders_emails()

    def get_server_settings(self, sender):

        con = sqlite3.connect(dbase)
        c = con.cursor()
        c.execute("SELECT smtp_server, port, password FROM Sender_emails WHERE sender_email =?", (sender,))
        data_from_Sender_emails = c.fetchall()
        con.close()
        self.smtp_server = data_from_Sender_emails[0][0]
        self.port = data_from_Sender_emails[0][1]
        self.password = data_from_Sender_emails[0][2]

    # -------------------------------- Email -------------------------------------------
    def get_senders_emails(self):
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

        self.senders = senders
        self.receivers = receivers

        self.senders_combobox.configure(values=self.senders)
        self.senders_combobox.set(value=self.senders[0])
        self.receiver_combobox.configure(values=self.receivers)
        self.receiver_combobox.set(value=self.receivers[0])
        # self.senders_combobox.configure(values=self.senders)

        return senders, receivers

    def set_receiver(self, receiver_email=None):

        if not receiver_email:
            self.receiver_email = str(self.receiver_combobox.get())
            if receiver_email == "":
                messagebox.showwarning("Προσοχή!", "Παρακαλώ συμπληρώστε ενα email")
                return

        message = MIMEMultipart()

        self.progress.start()
        self.progress['value'] = 20
        self.progress.update()
        if len(self.data) > 10:
            date = self.data[0]

            customer = self.data[1]

            copier = self.data[2]

            message["Subject"] = "Service Book " + " " + customer + " " + copier
            message["From"] = self.senders_combobox.get()
            message["To"] = self.receiver_email
            purpose = self.data[3]

            technician = self.data[4]

            actions = self.data[5]

            counter = self.data[6]

            next_service = self.data[7]

            files = self.data[8]

            spare_parts = self.data[9]

            urgent = self.data[10]

            phone = self.data[11]

            notes = self.data[12]

            dte = self.data[13]

            copier_id = self.data[14]

            finish_date = self.data[15]

            customer_id = self.data[17]

            service_id = self.data[18]

            if self.data[16] == 0:
                status = "Δεν έχει ολοκληρωθεί"
                finish_date = ""
            else:
                status = "Ολοκληρώθηκε"

                # Προσθήκη αρχείων
            # if files:
            #     for file in files:
            #         with open(file, "rb") as fil:
            #             ext = file.split('.')[-1:]
            #             attached_file = MIMEApplication(fil.read(), _subtype=ext)
            #             attached_file.add_header('content-disposition', 'attachment', filename=basename(file))
            #             message.attach(attached_file)

            # get_images_from_db:
            con = sqlite3.connect(dbase)
            cursor = con.cursor()
            cursor.execute("SELECT * FROM Service_images WHERE Service_ID =?", (service_id,))
            images = cursor.fetchall()

            cursor.close()
            con.close()
            if images:
                files = []
                images_path = "Service_images/Service_ID_" + str(service_id) + "/"
                if not os.path.exists(images_path):
                    os.makedirs(images_path)
                # Δημιουργεία εικόνων
                # images[num][4] ==> Η εικόνα σε sqlite3.Binary
                # images[num][2 ] =>> Ονομα αρχείου
                for num, i in enumerate(images):
                    with open(images_path + images[num][1] + images[num][2], 'wb') as image_file:
                        image_file.write(images[num][4])
                images = os.listdir(images_path)

                for img in images:
                    files.append(img)
                    ext = img.split('.')[-1:]
                    img = images_path + img
                    with open(img, "rb") as file:
                        attached_file = MIMEApplication(file.read(), _subtype=ext)
                        attached_file.add_header('content-disposition', 'attachment', filename=basename(img))
                        message.attach(attached_file)

            html = f"""\
                            <html>
                                <body>
<p><b>Ημερομηνία:  </b>  {date} <br> <b>Πελάτης: </b>  {customer}  <br><b>Customer_id</b> {customer_id} 
<br> <b>Φωτοτυπικό: </b>  {copier} <br><b>Copier_ID: </b>   {copier_id} <br><b>Σκοπός: </b> {purpose} 
<br><b>Τεχνικός : </b>  {technician} <br><b>Ενέργιες:  </b>{actions} <br><b>Επείγων: </b>  {urgent} 
<br><b>Τηλέφωνο:  </b> {phone} <br><b>ΔΤΕ:  </b>{dte} <br><b>Κατάσταση:  </b>{status}<br> 
<br><b>Ημ_Ολοκλ: </b>   {finish_date}  <br><b>Μετρητής:  </b>{counter} <br><b>Επόμενο Service:  </b>{next_service}
<br> <br><b>Αρχεία: </b>   {files} <br><b>Ανταλλακτικά:  </b>{spare_parts}<br> <br><b>Σημειώσεις: </b>  {notes} <b>
<br>Χρήστης:  </b>{user}
                                </body>
                            </html>
                            """
        elif len(self.data) == 3:  # Οταν δημηουργούμε κλήση

            customer = self.data[0]
            copier = self.data[1]
            file = self.data[2]

            message["Subject"] = "Service Book " + " " + customer + " " + copier
            message["From"] = self.senders_combobox.get()
            message["To"] = self.receiver_email
            with open(file, "rb") as img:
                attached_file = MIMEApplication(img.read(), _subtype="png")
                attached_file.add_header('content-disposition', 'attachment', filename=basename(file))
                message.attach(attached_file)
            date = datetime.datetime.today()
            html = f"""\
                            <html>
                                <body>
                        <p><b>Ημερομηνία:  </b>  {date} <br> <b>Πελάτης: </b>  {customer}  <br> <b>Φωτοτυπικό: </b>  {copier}  
                       <br> <b>Χρήστης:  </b>{user}
                                </body>
                            </html>
                            """
        elif len(self.data) == 5:  # επεξεργασία κλήσης και συντήρησης

            customer = self.data[0]
            copier = self.data[1]
            file1 = self.data[2]
            file2 = self.data[3]
            service_id = self.data[4]

            message["Subject"] = "Service Book " + " " + customer + " " + copier
            message["From"] = self.senders_combobox.get()
            message["To"] = self.receiver_email
            with open(file1, "rb") as img:
                attached_file = MIMEApplication(img.read(), _subtype="png")
                attached_file.add_header('content-disposition', 'attachment', filename=basename(file1))
                message.attach(attached_file)
            try:
                with open(file2, "rb") as img:
                    attached_file = MIMEApplication(img.read(), _subtype="png")
                    attached_file.add_header('content-disposition', 'attachment', filename=basename(file2))
                    message.attach(attached_file)
            except FileNotFoundError:  # όταν δεν στελνουμε σαν screen shot την καρτέλα ανταλλακτικά
                pass

            # get_images_from_db:
            con = sqlite3.connect(dbase)
            cursor = con.cursor()
            cursor.execute("SELECT * FROM Service_images WHERE Service_ID =?", (service_id,))
            images = cursor.fetchall()

            cursor.close()
            con.close()
            if images:
                files = []
                images_path = "Service_images/Service_ID_" + str(service_id) + "/"
                if not os.path.exists(images_path):
                    os.makedirs(images_path)
                # Δημιουργεία εικόνων
                # images[num][4] ==> Η εικόνα σε sqlite3.Binary
                # images[num][2 ] =>> Ονομα αρχείου
                for num, i in enumerate(images):
                    with open(images_path + images[num][1] + images[num][2], 'wb') as image_file:
                        image_file.write(images[num][4])
                images = os.listdir(images_path)

                for img in images:
                    files.append(img)
                    ext = img.split('.')[-1:]
                    img = images_path + img
                    with open(img, "rb") as file:
                        attached_file = MIMEApplication(file.read(), _subtype=ext)
                        attached_file.add_header('content-disposition', 'attachment', filename=basename(img))
                        message.attach(attached_file)

            date = datetime.datetime.today()
            html = f"""\
                            <html>
                                <body>
                        <p><b>Ημερομηνία:  </b>  {date} <br> <b>Πελάτης: </b>  {customer}  <br> <b>Φωτοτυπικό: </b>  {copier}  
                       <br> <b>Χρήστης:  </b>{user}
                                </body>
                            </html>
                            """

        else:
            date = self.data[0]
            customer = self.data[1]
            copier = self.data[2]
            message["Subject"] = "Service Book " + " " + customer + " " + copier
            message["From"] = self.senders_combobox.get()
            message["To"] = self.receiver_email
            purpose = self.data[3]
            technician = self.data[4]
            urgent = self.data[5]
            phone = self.data[5]
            notes = self.data[7]
            copier_id = self.data[8]

            html = f"""\
                <html>
                    <body>
            <p><b>Ημερομηνία:  </b>  {date} <br> <b>Πελάτης: </b>  {customer}  <br> <b>Φωτοτυπικό: </b>  {copier}  
            <br><b>Σκοπός: </b> {purpose} <br><b>Τεχνικός : </b>  {technician}<br><b>Επείγων: </b>  {urgent} 
            <br><b>Τηλέφωνο:  </b> {phone} <br><b>Σημειώσεις: </b>  {notes}  <br><b>Copier_ID: </b>   {copier_id} 
            <b>Χρήστης:  </b>{user}
                    </body>
                </html>
                """
        # Turn these into plain/html MIMEText objects
        # part1 = MIMEText(text, "plain")
        self.progress['value'] = 40
        self.progress.update()
        part2 = MIMEText(html, "html")
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part2)
        # message.attach(part1)

        # Create a secure SSL context
        context = ssl.create_default_context()

        self.get_server_settings(self.senders_combobox.get())
        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(self.smtp_server, self.port)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(self.senders_combobox.get(), self.password)
            self.progress['value'] = 80
            self.progress.update()
            server.sendmail(self.senders_combobox.get(), self.receiver_email, message.as_bytes())  # Send email here

        except Exception as e:
            # Print any error messages to stdout
            messagebox.showerror("Σφάλμα", f'{e}')
            print(f'{__name__}', e)
        finally:
            server.quit()

            try:

                # Διαγραφή αρχείων μετά το κλείσημο του παραθύρου
                shutil.rmtree("prints/screen_shot", ignore_errors=True)
                if os.path.exists(images_path):
                    shutil.rmtree(images_path, ignore_errors=True)

            except UnboundLocalError:  # Δεν υπάρχουν αρχεία για διαγραφή
                pass
            self.progress['value'] = 100
            self.progress.update()
            self.progress.stop()
            self.top.destroy()






