#  -*- coding: utf-8 -*-
import getpass
import os
import logging
import datetime
import sqlite3
import sys


user = getpass.getuser()

mlshop = 0


if mlshop:
    if sys.platform == "linux":
        # ML Shop dbases Linux
        dbase = "/home/dannys/qnap/DROPBOX/ΕΓΓΡΑΦΑ/6.  ΒΙΒΛΙΟ SERVICE/Service_book.db"
        spare_parts_db = "/home/dannys/qnap/DROPBOX/ΕΓΓΡΑΦΑ/2.  ΑΠΟΘΗΚΗ/3. ΚΑΙΝΟΥΡΙΑ_ΑΠΟΘΗΚΗ.db"
    else:

        # ML Shop dbases
        dbase = "\\\\192.168.1.200\\Public\\DROPBOX\\ΕΓΓΡΑΦΑ\\6.  ΒΙΒΛΙΟ SERVICE\\Service_book.db"
        spare_parts_db = "\\\\192.168.1.200\\Public\\DROPBOX\\ΕΓΓΡΑΦΑ\\2.  ΑΠΟΘΗΚΗ\\3. ΚΑΙΝΟΥΡΙΑ_ΑΠΟΘΗΚΗ.db"


else:
    spare_parts_db = "ΑΠΟΘΗΚΗ.db"
    dbase = "Service_book.db"  # Local Dbase


def check_if_demo():
    con = sqlite3.connect(dbase)
    c = con.cursor()
    c.execute("SELECT seq from sqlite_sequence WHERE name ='demo'")
    data = c.fetchall()
    con.close()
    if data[0][0] == "1":
        version = 1  # Its Demo
    else:
        version = 0  # Its not Demo
    return version


demo = check_if_demo()

if demo:
    service_book_version = "V 1.7.7 Demo"
else:
    service_book_version = "V 1.7.7"


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
