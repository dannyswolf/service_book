#  -*- coding: utf-8 -*-
import getpass
import os
import logging
import sys
from urllib.request import urlopen
from tkinter import messagebox
user = getpass.getuser()

mlshop = 1

if mlshop:
    # ML Shop dbases
    dbase = "\\\\192.168.1.200\\Public\\DROPBOX\\ΕΓΓΡΑΦΑ\\6.  ΒΙΒΛΙΟ SERVICE\\Service_book.db"
    spare_parts_db = "\\\\192.168.1.200\\Public\\DROPBOX\\ΕΓΓΡΑΦΑ\\2.  ΑΠΟΘΗΚΗ\\3. ΚΑΙΝΟΥΡΙΑ_ΑΠΟΘΗΚΗ.db"

else:
    spare_parts_db = "3. ΚΑΙΝΟΥΡΙΑ_ΑΠΟΘΗΚΗ.db"
    dbase = "Service_book.db"  # Local Dbase

service_book_version = "V 1.4.7 ML Shop"

demo = 0  # 0 Demo Disabled 1 Demo enabled

# -------------------------------- Email -------------------------------------------
smtp_server = "smtp.gmail.com"
ssl_port = 465  # For SSL
port = 587  # For starttls
sender_email = "mlcopier10@gmail.com"
password = '3714000000'

# Ημερομηνία
try:
    res = urlopen('http://just-the-time.appspot.com/')
    result = res.read().strip()
    result_str = result.decode('utf-8')  # 2020-01-08 22:30:56
    only_date = result_str[:11]
    day = only_date[8:10]
    month = only_date[5:7]
    year = only_date[:4]
    today = day + " " + month + " " + year  # 08 01 2020

except:
    messagebox.showerror("Σφάλμα στην σύνδεση σας", "Παρακαλω ελέγξτε την σύνδεση σας στο διαδίκτυο")

# -------------ΔΗΜΗΟΥΡΓΕΙΑ LOG FILE και Ημερομηνία ------------------

log_dir = "logs" + "\\" + today + "\\"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
else:
    pass

log_file_name = "Service Book " + today + ".log"
log_file = os.path.join(log_dir, log_file_name)

# log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)  # or whatever
handler = logging.FileHandler(log_file, 'a', 'utf-8')  # or whatever
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # or whatever
handler.setFormatter(formatter)  # Pass handler as a parameter, not assign
root_logger.addHandler(handler)
sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info

