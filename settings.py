#  -*- coding: utf-8 -*-
import getpass
user = getpass.getuser()

# ML Shop dbases
dbase = "\\\\192.168.1.200\\Public\\DROPBOX\\ΕΓΓΡΑΦΑ\\6.  ΒΙΒΛΙΟ SERVICE\\Service_book.db"
spare_parts_db = "\\\\192.168.1.200\\Public\\DROPBOX\\ΕΓΓΡΑΦΑ\\2.  ΑΠΟΘΗΚΗ\\3. ΚΑΙΝΟΥΡΙΑ_ΑΠΟΘΗΚΗ.db"

# spare_parts_db = "3. ΚΑΙΝΟΥΡΙΑ_ΑΠΟΘΗΚΗ.db"

service_book_version = "V 1.2.2 ML Shop"
# dbase = "Service_book.db"  # Local Dbase

demo = 0  # 0 Demo Disabled 1 Demo enabled

# -------------------------------- Email -------------------------------------------
smtp_server = "smtp.gmail.com"
ssl_port = 465  # For SSL
port = 587  # For starttls
sender_email = "mlcopier10@gmail.com"
password = '3714000000'

