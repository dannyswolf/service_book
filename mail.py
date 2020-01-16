#  -*- coding: utf-8 -*-
import sys
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from settings import smtp_server, port, sender_email, password, ssl_port, user, root_logger  # settings
from tkinter import Tk, ttk, messagebox

# -------------ΔΗΜΗΟΥΡΓΕΙΑ LOG FILE  ------------------
sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info
print(f"{100 * '*'}\n\t\t\t\t\t\t\t\t\t\tFILE {__name__}")


# ssl_port = 465  # For SSL
# port = 587  # For starttls


def send_mail(data):

    root = Tk()
    root.geometry("250x100+50+50")
    root.title("Αποστολή e-mail")
    email_label = ttk.Label(root, text="Εισάγεται e-mail")
    email_label.pack()
    email_entry = ttk.Entry(root, width=30)
    email_entry.pack()

    def set_receiver(receiver_email=None):
        if not receiver_email:
            receiver_email = str(email_entry.get())

        message = MIMEMultipart("alternative")

        if len(data) == 17:
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
            if data[16] == 1:
                status = "Ολοκληρώθηκε"
            else:
                status = "Δεν έχει ολοκληρωθεί"
            html = f"""\
                            <html>
                                <body>
<p><b>Ημερομηνία:  </b>  {date} <br> <b>Πελάτης: </b>  {customer}  <br> <b>Φωτοτυπικό: </b>  {copier}  
<br><b>Copier_ID: </b>   {copier_id} <br><b>Σκοπός: </b> {purpose} <br><b>Τεχνικός : </b>  {technician} 
<br><b>Ενέργιες:  </b>{actions} <br><b>Επείγων: </b>  {urgent} <br><b>Τηλέφωνο:  </b> {phone} 
<br><b>ΔΤΕ:  </b>{dte} <br><b>Κατάσταση:  </b>{status}<br> <br><b>Ημ_Ολοκλ: </b>   {finish_date}   
<br><b>Μετρητής:  </b>{counter} <br><b>Επόμενο Service:  </b>{next_service}<br> <br><b>Αρχεία: </b>   {files}   
<br><b>Ανταλλακτικά:  </b>{spare_parts}<br> <br><b>Σημειώσεις: </b>  {notes} <b><br>Χρήστης:  </b>{user}
                                </body>
                            </html>
                            """
        else:
            date = data[0]
            customer = data[1]
            copier = data[2]
            message["Subject"] = "Service Book " + customer + copier
            message["From"] = sender_email
            message["To"] = receiver_email
            purpose = data[3]
            technician = data[4]
            finish_date = data[5]
            urgent = data[6]
            phone = data[7]
            notes = data[8]
            copier_id = data[9]
            dte = data[10]
            status = data[11]


            html = f"""\
                <html>
                    <body>
            <p><b>Ημερομηνία:  </b>  {date} <br> <b>Πελάτης: </b>  {customer}  <br> <b>Φωτοτυπικό: </b>  {copier}  
            <br><b>Σκοπός: </b> {purpose} <br><b>Τεχνικός : </b>  {technician} <br><b>Ημ_Ολοκλ:  </b>{finish_date}
             <br><b>Επείγων: </b>  {urgent} <br><b>Τηλέφωνο:  </b> {phone} <br><b>Σημειώσεις: </b>  {notes} 
             <br><b>Copier_ID: </b>   {copier_id}   <br><b>ΔΤΕ:  </b>{dte} <br><b>Κατάσταση:  </b>{status}<br>
            <b>Χρήστης:  </b>{user}
                    </body>
                </html>
                """
        # Turn these into plain/html MIMEText objects
        # part1 = MIMEText(text, "plain")
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
            server.sendmail(sender_email, receiver_email, message.as_bytes())  # Send email here
        except Exception as e:
            # Print any error messages to stdout
            messagebox.showerror("Σφάλμα", f'{e}')
            print(f'{__name__}', e)
        finally:
            server.quit()
            root.destroy()
    email_entry.focus()

    send_btn = ttk.Button(root, text="Αποστολή", command=set_receiver)
    send_btn.pack()
    send_to_mlcopier_btn = ttk.Button(root, text="Αποστολή Στο mlcopier", command=lambda:set_receiver("mlcopier@mail.com"))
    send_to_mlcopier_btn.pack()


