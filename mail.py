#  -*- coding: utf-8 -*-
import sys
import os
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from os.path import basename
from settings import smtp_server, port, sender_email, password, ssl_port, user, root_logger, dbase  # settings
from tkinter import Tk, ttk, messagebox
from tkinter.ttk import Progressbar
import time
import sqlite3
import shutil  # για διαγραφη των φακέλων με τις εικόνες
# -------------ΔΗΜΗΟΥΡΓΕΙΑ LOG FILE  ------------------
sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info
print(f"{100 * '*'}\n\t\t\t\t\t\t\t\t\t\tFILE {__name__}")


# ssl_port = 465  # For SSL
# port = 587  # For starttls


def send_mail(data):

    root = Tk()
    root.geometry("350x150+50+50")
    root.title("Αποστολή e-mail")
    email_label = ttk.Label(root, text="Εισάγεται e-mail")
    email_label.pack()
    email_entry = ttk.Entry(root, width=30)
    email_entry.pack()

    # Progress bar widget

    progress = Progressbar(root, orient='horizontal', length=100, mode='determinate')
    progress["maximum"] = 100
    # Function responsible for the updation
    # of the progress bar value

    def set_receiver(receiver_email=None):

        if not receiver_email:
            receiver_email = str(email_entry.get())

        message = MIMEMultipart()

        progress.start()
        progress['value'] = 20
        progress.update()
        if len(data) > 10:
            date = data[0]
            customer = data[1]
            copier = data[2]
            message["Subject"] = "Service Book " + " " + customer + " " + copier
            message["From"] = sender_email
            message["To"] = receiver_email
            purpose = data[3]
            technician = data[4]
            actions = data[5]
            counter = data[6]
            next_service = data[7]
            files = data[8]
            spare_parts = data[9]
            urgent = data[10]
            phone = data[11]
            notes = data[12]
            dte = data[13]
            copier_id = data[14]
            finish_date = data[15]
            customer_id = data[17]
            service_id = data[18]
            if data[16] == 0:
                status = "Δεν έχει ολοκληρωθεί"
                finish_date = ""
            else:
                status = "Ολοκληρώθηκε"

                # Προσθήκη αρχείων
            if files:
                for file in files:
                    with open(file, "rb") as fil:
                        ext = file.split('.')[-1:]
                        attached_file = MIMEApplication(fil.read(), _subtype=ext)
                        attached_file.add_header('content-disposition', 'attachment', filename=basename(file))
                        message.attach(attached_file)

            # get_images_from_db():
            con = sqlite3.connect(dbase)
            cursor = con.cursor()
            cursor.execute("SELECT * FROM Service_images WHERE Service_ID =?", (service_id,))
            images = cursor.fetchall()
            cursor.close()
            con.close()
            if images:
                files = []
                images_path = "Service images/Service_ID_" + str(service_id) + "/"
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
        else:
            date = data[0]
            customer = data[1]
            copier = data[2]
            message["Subject"] = "Service Book " + " " + customer + " " + copier
            message["From"] = sender_email
            message["To"] = receiver_email
            purpose = data[3]
            technician = data[4]
            urgent = data[5]
            phone = data[5]
            notes = data[7]
            copier_id = data[8]

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
        progress['value'] = 40
        progress.update()
        part2 = MIMEText(html, "html")
        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        message.attach(part2)
        # message.attach(part1)

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Try to log in to server and send email
        try:
            server = smtplib.SMTP(smtp_server, port)
            server.ehlo()  # Can be omitted
            server.starttls(context=context)  # Secure the connection
            server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            progress['value'] = 80
            progress.update()
            server.sendmail(sender_email, receiver_email, message.as_bytes())  # Send email here

        except Exception as e:
            # Print any error messages to stdout
            messagebox.showerror("Σφάλμα", f'{e}')
            print(f'{__name__}', e)
        finally:
            server.quit()

            try:
                # Διαγραφή αρχείων μετά το κλείσημο του παραθύρου
                if os.path.exists(images_path):
                    shutil.rmtree(images_path, ignore_errors=True)
            except UnboundLocalError:  # Δεν υπάρχουν αρχεία για διαγραφή
                pass
            progress['value'] = 100
            progress.update()
            progress.stop()
            root.destroy()

    email_entry.focus()

    send_btn = ttk.Button(root, text="Αποστολή", command=set_receiver)
    send_btn.pack()

    send_to_mlcopier_btn = ttk.Button(root, text="Αποστολή στο mlcopier", command=lambda: set_receiver("mlcopier@mail.com"))
    send_to_mlcopier_btn.pack()
    progress.pack(pady=10)





