#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 27, 2019 08:58:37 PM EET  platform: Windows NT

import os
import subprocess

import PIL.Image
from PIL import ImageTk
import sqlite3
import tkinter as tk
from tkinter import messagebox, filedialog
import image_viewer_support
import shutil  # για διαγραφη των φακέλων με τις εικόνες
import sys
from settings import dbase, root_logger  # settings

# -------------ΔΗΜΗΟΥΡΓΕΙΑ LOG FILE  ------------------
sys.stderr.write = root_logger.error
sys.stdout.write = root_logger.info
print(f"{100 * '*'}\n\t\t\t\t\t\t\t\t\t\tFILE {__name__}")


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    image_viewer_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt, selected_service_ID, images_path
    selected_service_ID = args[0]
    # Δημιουργία φακέλου για τις εικόνες
    images_path = "Service images/Service_ID_" + str(selected_service_ID) + "/"
    if not os.path.exists(images_path):
        os.makedirs(images_path)
    rt = root
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    image_viewer_support.init(w, top, *args, **kwargs)
    return (w, top)


def get_images_from_db():
    con = sqlite3.connect(dbase)
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Service_images WHERE Service_ID =?", (selected_service_ID,))
    images = cursor.fetchall()
    cursor.close()
    con.close()

    # Δημιουργεία εικόνων
    # images[num][4] ==> Η εικόνα σε sqlite3.Binary
    # images[num][2 ] =>> Ονομα αρχείου
    for num, i in enumerate(images):
        with open(images_path + images[num][1] + images[num][2], 'wb') as image_file:
            image_file.write(images[num][4])
    images = os.listdir(images_path)

    return images


def convert_bytes(size):
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return "%3.1f %s" % (size, x)
        size /= 1024.0

    return size


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        self.selected_image = ""  # Εικόνα που προβάλεται PIL instance
        self.selected_service_ID = selected_service_ID
        self.images = get_images_from_db()
        self.image = ""  # Ονομα αρχείου που προβάλεται "icon_resized.jpg"  "icon.png"
        self.image_size = ""  # Μέγεθος αρχείου
        self.images_path = images_path
        self.filenames = os.listdir(self.images_path)

        self.index = 0
        self.new_size = (800, 600)
        self.top = top
        top.geometry("950x859+558+77")
        top.minsize(120, 1)
        top.maxsize(1980, 1980)
        top.resizable(1, 1)
        top.title("Εικόνες")
        top.configure(background="#f6f6ee")
        top.bind('<Escape>', self.quit)
        top.protocol("WM_DELETE_WINDOW", self.del_files)
        top.focus()

        self.previous_btn = tk.Button(top)
        self.previous_btn.place(relx=0.323, rely=0.955, height=30, relwidth=0.200)
        self.previous_btn.configure(activebackground="#ececec")
        self.previous_btn.configure(activeforeground="#000000")
        self.previous_btn.configure(background="#6b6b6b")
        self.previous_btn.configure(disabledforeground="#a3a3a3")
        self.previous_btn.configure(foreground="#ffffff")
        self.previous_btn.configure(highlightbackground="#d9d9d9")
        self.previous_btn.configure(highlightcolor="black")
        self.previous_btn.configure(pady="0")
        self.previous_btn.configure(text='''Προηγούμενη''')
        self.previous_btn.configure(command=self.show_previous)

        self.next_btn = tk.Button(top)
        self.next_btn.place(relx=0.508, rely=0.955, height=30, relwidth=0.200)
        self.next_btn.configure(activebackground="#ececec")
        self.next_btn.configure(activeforeground="#000000")
        self.next_btn.configure(background="#6b6b6b")
        self.next_btn.configure(disabledforeground="#a3a3a3")
        self.next_btn.configure(foreground="#ffffff")
        self.next_btn.configure(highlightbackground="#d9d9d9")
        self.next_btn.configure(highlightcolor="black")
        self.next_btn.configure(pady="0")
        self.next_btn.configure(text='''Επόμενη''')
        self.next_btn.configure(command=self.show_next)

        self.image_label = tk.Label(top)
        self.image_label.place(relx=0.042, rely=0.012, height=800, relwidth=0.929)
        self.image_label.configure(background="#006291")
        self.image_label.configure(disabledforeground="#a3a3a3")
        self.image_label.configure(text="")
        file = self.images_path + self.filenames[0]
        if file[-3:] != "pdf":
            self.image = self.filenames[0][:-4]
            self.selected_image = PIL.Image.open(file)
            image = self.selected_image.resize(self.new_size)
            photo = ImageTk.PhotoImage(image)
            self.image_label.configure(image=photo)
            self.image_label.image = photo

        else:
            subprocess.Popen(self.images_path + self.filenames[self.index], shell=True)

        # Αποθύκευση
        self.save_btn = tk.Button(top)
        self.save_btn.place(relx=0.046, rely=0.955, height=30, relwidth=0.200)
        self.save_btn.configure(activebackground="#ececec")
        self.save_btn.configure(activeforeground="#000000")
        self.save_btn.configure(background="#63b057")
        self.save_btn.configure(disabledforeground="#a3a3a3")
        self.save_btn.configure(foreground="#ffffff")
        self.save_btn.configure(highlightbackground="#d9d9d9")
        self.save_btn.configure(highlightcolor="black")
        self.save_btn.configure(pady="0")
        self.save_btn.configure(text='''Αποθήκευση''')
        self.save_btn.configure(command=self.save_img)

        # Διαγραφή
        self.save_btn = tk.Button(top)
        self.save_btn.place(relx=0.750, rely=0.955, height=30, relwidth=0.200)
        self.save_btn.configure(activebackground="#ececec")
        self.save_btn.configure(activeforeground="#000000")
        self.save_btn.configure(background="red")
        self.save_btn.configure(disabledforeground="#a3a3a3")
        self.save_btn.configure(foreground="#ffffff")
        self.save_btn.configure(highlightbackground="#d9d9d9")
        self.save_btn.configure(highlightcolor="black")
        self.save_btn.configure(pady="0")
        self.save_btn.configure(text='''Διαγραφή''')
        self.save_btn.configure(command=self.del_from_db)

        self.image_name_label = tk.Label(top)
        self.image_name_label.place(relx=0.046, rely=0.910, height=30, relwidth=0.800)
        self.image_name_label.configure(background="#006291")
        self.image_name_label.configure(foreground="white")
        self.image_name_label.configure(disabledforeground="#a3a3a3")

        self.get_size_of_files()


    def quit(self, event=None):
        self.del_files()
        self.top.destroy()

    def get_size_of_files(self):
        # Μέγεθος αρχείου
        self.image = self.filenames[self.index][:-4]
        con = sqlite3.connect(dbase)
        c = con.cursor()
        c.execute("SELECT File_size FROM Service_images WHERE Filename =?", (self.image,))
        size = c.fetchall()
        con.close()
        try:
            self.image_size = convert_bytes(float(size[0][0]))
        except IndexError:
            self.image_size = convert_bytes(float(size[0]))

        self.image_name_label.configure(text="Αρχείο : " + self.filenames[self.index] +
                                             "  Μέγεθος: " + self.image_size)

    # Αποθήκευση επιλεγμένης εικόνας
    def save_img(self, ):
        ext = self.filenames[self.index][-4:]

        if ext != ".pdf":

            files = [('Εικόνα', ext),
                     ('All Files', '*.*')]

            im = PIL.Image.open(self.images_path + self.filenames[self.index])
            file = filedialog.asksaveasfile(mode='wb', filetypes=files, defaultextension=files)
            if file:
                im.save(file)
            self.top.focus()
            return
            # Εμφάνιση εικόνας
            # self.selected_image.show()
        else:
            # pdf_file => το αρχείο για save
            pdf_file = self.images_path + self.filenames[self.index]
            files = [('Pdf', '*.pdf*')]
            file = filedialog.asksaveasfile(mode='wb', filetypes=files, defaultextension=files)
            # get binary from pdf file
            with open(pdf_file, "rb") as pdf_reader:  # opening for [r]eading as [b]inary
                data = pdf_reader.read()
            # file.name =>> αρχείο που επέλεξε ο χρήστης
            with open(file.name, 'wb') as new_pdf_file:  # Εγραφή στο αρχείο
                new_pdf_file.write(data)
            self.top.focus()

    # Εμφάνηση επόμενης
    def show_next(self):
        self.index = self.index + 1

        try:
            file_ext = self.filenames[self.index][-3:]

            if file_ext != "pdf":  # Αν δεν είναι pdf
                self.selected_image = PIL.Image.open(self.images_path + self.filenames[self.index])
                self.image = self.filenames[self.index][:-4]
                # Μέγεθος αρχείου
                con = sqlite3.connect(dbase)
                c = con.cursor()
                c.execute("SELECT File_size FROM Service_images WHERE Filename =?", (self.image,))
                size = c.fetchall()
                print("self.image", self.image, size)
                con.close()
                self.image_size = convert_bytes(float(size[0][0]))
                self.image_name_label.configure(text="Αρχείο : " + self.filenames[self.index] +
                                                     "  Μέγεθος: " + self.image_size)

            else:  # Αν είναι pdf
                self.selected_image = PIL.Image.open("icons/pdf.png")

                self.image = self.filenames[self.index][:-4]

                # Μέγεθος αρχείου
                con = sqlite3.connect(dbase)
                c = con.cursor()
                c.execute("SELECT File_size FROM Service_images WHERE Filename =?", (self.image,))
                size = c.fetchall()
                print("self.image", self.image, size)
                con.close()
                self.image_size = convert_bytes(float(size[0][0]))

                self.image_name_label.configure(text="Αρχείο : " + self.filenames[self.index] +
                                                     "  Μέγεθος: " + self.image_size)

                subprocess.Popen([self.images_path + self.filenames[self.index]], shell=True)

        except FileNotFoundError:
            messagebox.showinfo("Προσοχή", "Το αρχείο δεν βρέθηκε")
        except IndexError:
            messagebox.showinfo("Προσοχή", " Δεν υπάρχουν αλλα  αρχεία για προβολή")
            self.index -= 1
            self.top.focus()
            return
        image = self.selected_image.resize(self.new_size)
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

    # Εμφάνηση προηγούμενης
    def show_previous(self):
        try:
            if self.index > 0:
                self.index = self.index - 1
            else:
                raise IndexError

            file_ext = self.filenames[self.index][-3:]

            if file_ext != "pdf":
                self.selected_image = PIL.Image.open(self.images_path + self.filenames[self.index])
                self.image = self.filenames[self.index][:-4]

                # Μέγεθος αρχείου
                con = sqlite3.connect(dbase)
                c = con.cursor()
                c.execute("SELECT File_size FROM Service_images WHERE Filename =?", (self.image,))
                size = c.fetchall()
                print("self.image", self.image, size)
                con.close()
                self.image_size = convert_bytes(float(size[0][0]))

                self.image_name_label.configure(text="Αρχείο : " + self.filenames[self.index] +
                                                     "  Μέγεθος: " + self.image_size)

            else:
                self.selected_image = PIL.Image.open("icons/pdf.png")
                self.image = self.filenames[self.index][:-4]

                # Μέγεθος αρχείου
                con = sqlite3.connect(dbase)
                c = con.cursor()
                c.execute("SELECT File_size FROM Service_images WHERE Filename =?", (self.image,))
                size = c.fetchall()
                print("self.image", self.image, size)
                con.close()
                self.image_size = convert_bytes(float(size[0][0]))

                self.image_name_label.configure(text="Αρχείο : " + self.filenames[self.index] +
                                                     "  Μέγεθος: " + self.image_size)

                subprocess.Popen([self.images_path + self.filenames[self.index]], shell=True)

        except FileNotFoundError:
            messagebox.showinfo("Προσοχή", "Το αρχείο δεν βρέθηκε")
        except IndexError:
            messagebox.showinfo("Προσοχή", " Δεν υπάρχουν αλλα αρχεία για προβολή")
            self.index += 1
            self.top.focus()
            return

        image = self.selected_image.resize(self.new_size)
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo

    # Διαγραφή αρχείων μετά το κλείσημο του παραθύρου
    def del_files(self):
        shutil.rmtree(self.images_path, ignore_errors=True)
        self.top.destroy()

    # Διαγραφή αρχείου απο την βαση
    def del_from_db(self):
        con = sqlite3.connect(dbase)
        cur = con.cursor()
        cur.execute("DELETE FROM Service_images WHERE Filename =?", (self.image,))
        con.commit()
        cur.close()
        con.close()
        messagebox.showinfo("Προσοχή", f"Το {self.image} διαγράφηκε")

        os.remove(self.images_path + self.filenames[self.index])

        self.filenames.remove(self.filenames[self.index])
        self.top.focus()
        self.show_next()
        return

if __name__ == '__main__':
    vp_start_gui()
