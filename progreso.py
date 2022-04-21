from itertools import count
from logging import root
from operator import length_hint
from struct import pack
import tkinter as tk
from tkinter import HORIZONTAL, Button, Label, Tk, ttk
from threading import Thread
from urllib.request import urlretrieve, urlcleanup
import time

root = Tk()

bit = root.iconbitmap('cab-vec.ico')
root.geometry('800x800')
root.resizable(False, False)
root.title('Carrera')

def step():
    
    count=0
    while count < 100:
        count +=20
        for x in range(1):
            my_label.config(text=my_progress['value'])
            my_progress['value'] +=2
            my_progress2['value'] +=10
            my_progress3['value'] +=15
            my_progress4['value'] +=2
            root.update_idletasks()
            time.sleep(1)
        
def stop():
    my_progress.stop()

my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
my_progress.pack(pady=20)

my_progress2 = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
my_progress2.pack(pady=20)

my_progress3 = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
my_progress3.pack(pady=20)

my_progress4 = ttk.Progressbar(root, orient=HORIZONTAL, length=400, mode='determinate')
my_progress4.pack(pady=20)

my_button = Button(root, text="Iniciar carrera", command=step)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)


root.mainloop()