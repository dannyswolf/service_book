#  -*- coding: utf-8 -*-
import datetime
import getpass
import hashlib
import logging
import os
import sqlite3
import sys

user = getpass.getuser()

mlshop = 1


if mlshop:
    if sys.platform == "linux":
        # ML Shop dbases Linux
        dbase = "/home/dannys/qnap/GOOGLE-DRIVE/ΕΓΓΡΑΦΑ/6.  ΒΙΒΛΙΟ SERVICE/Service_book.db"
        spare_parts_db = "/home/dannys/qnap/GOOGLE-DRIVE/ΕΓΓΡΑΦΑ/2.  ΑΠΟΘΗΚΗ/3. ΚΑΙΝΟΥΡΙΑ_ΑΠΟΘΗΚΗ.db"
    else:

        # ML Shop dbases
        dbase = "\\\\192.168.1.200\\Public\\GOOGLE-DRIVE\\ΕΓΓΡΑΦΑ\\6.  ΒΙΒΛΙΟ SERVICE\\Service_book.db"
        spare_parts_db = "\\\\192.168.1.200\\Public\\GOOGLE-DRIVE\\ΕΓΓΡΑΦΑ\\2.  ΑΠΟΘΗΚΗ\\3. ΚΑΙΝΟΥΡΙΑ_ΑΠΟΘΗΚΗ.db"

 # VPN
else:
    spare_parts_db = "ΑΠΟΘΗΚΗ.db"
    # dbase = "\\\\10.8.0.1\\Public\\GOOGLE-DRIVE\\ΕΓΓΡΑΦΑ\\6.  ΒΙΒΛΙΟ SERVICE\\Service_book.db"  #  VPN Windows
    dbase = "Service_book.db"  # Local Dbase

db_path = os.path.dirname(os.path.realpath(dbase))


def check_if_demo():
    con = sqlite3.connect(dbase)
    c = con.cursor()
    c.execute("SELECT seq from sqlite_sequence WHERE name ='demo'")
    data = c.fetchall()
    con.close()
    try:
        if data[0][0] == 0 or data[0][0] == "0":
            con = sqlite3.connect(dbase)
            c = con.cursor()
            c.execute("SELECT seq from sqlite_sequence WHERE name ='key'")
            key_data = c.fetchall()
            c.execute("SELECT seq from sqlite_sequence WHERE name ='customer_email'")
            email_data = c.fetchall()
            con.close()
            key = key_data[0][0]
            email = email_data[0][0]
            email_key = hashlib.md5(email.encode())

            if key != "" and email != "" and key == email_key.hexdigest():

                version = 0  # Its Not Demo
                return version
            else:
                version = 1  # Its  Demo
                return version
        else:
            version = 1  # Its  Demo
            return version
    except IndexError:  # list index out of range Δεν υπάρχει το demo στην βάση
        return 1  # Its  Demo


demo = check_if_demo()
#demo = 0
if demo:

    service_book_version = "V 1.9.7 Demo"
else:

    service_book_version = "V 1.9.7"


today = datetime.datetime.today().strftime("%d %m %Y")
# -------------ΔΗΜΗΟΥΡΓΕΙΑ LOG FILE και Ημερομηνία ------------------

log_dir = "logs" + "/" + today + "/"
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

