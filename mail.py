#  -*- coding: utf-8 -*-
import sys
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from settings import smtp_server, port, sender_email, password, ssl_port, user, root_logger  # settings


# -------------ΔΗΜΗΟΥΡΓΕΙΑ LOG FILE  ------------------
sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info
print(f"{100 * '*'}\n\t\t\t\t\t\t\t\t\t\tFILE {__name__}")


# ssl_port = 465  # For SSL
# port = 587  # For starttls


def send_mail(data):

    receiver_email = 'mlcopier@mail.com'

    message = MIMEMultipart("alternative")

    message["Subject"] = "Service Book " + user
    message["From"] = sender_email
    message["To"] = receiver_email

    date = data[0]
    customer = data[1]
    copier = data[2]
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
        print(e)
    finally:
        server.quit()



