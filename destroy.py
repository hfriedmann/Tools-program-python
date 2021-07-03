import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo
import os
import glob
#sprit for destroying last label.

from tkinter import filedialog
from tkinter import *
import glob
from tkinter import Tk, Button
from PIL import Image
import os
from PIL import ImageTk, Image

# root window
root = tk.Tk()
root.geometry('490x370')
root.resizable(False, False)
root.title('Diogenes')
#root > frame
#frame = ttk.Frame(root)
#frame = Canvas(root)
#frame.grid()
image = Image.open("bg1.png")
photo = ImageTk.PhotoImage(image)
label = Label(root, image=photo)
label.image = photo
label.place(x=90, y=90, in_=root)


def none():

    print("hey")

def top_menu():
    menu_widget = tk.Menu(root)
    submenu_widget = tk.Menu(menu_widget, tearoff=False)
    submenu_widget.add_command(label="Main",
                               command=main_t)
    submenu_widget.add_command(label="Convert images",
                               command=main_2)
    submenu_widget.add_command(label="bugs",
                               command=none)
    menu_widget.add_cascade(label="Item1", menu=submenu_widget)
    menu_widget.add_command(label="Item2",
                            command=none)
    menu_widget.add_command(label="Item3",
                            command=none)
    root.config(menu=menu_widget)

def main_t():
    global label
    label.destroy()
    image = Image.open("bg1.png")
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo)
    label.image = photo
    label.place(x=70, y=10, in_=root)

def main_2():
    global label
    label.destroy()
    image = Image.open("bg1.png")
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo)
    label.image = photo
    label.place(x=70, y=70, in_=root)

top_menu()
root.mainloop()
