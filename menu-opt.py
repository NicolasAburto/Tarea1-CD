########################################### Descripción del proyecto: ###########################################
#   Programa en Python que simula una carrera de caballos.
#   Descipción:
#    - Se creará un programa que simule una carrera de caballos con avance aleatorio.
#    - Código desarrollado mediante metodología de programación modular, con el objetivo de reutilizar bibliotecas de funciones y/o métodos.
#    -
#
#   Autores:
#       - José Avilán (https://github.com/JoseAvilan)
#       - Nicolas Aburto (https://github.com/NicolasAburto)
#       - Franco Avilés (https://github.com/FrancoAv1)
#
#   Licencia:
#       - Abril 2022. Apache 2.0.
#
#################################################################################################################

import random
import tkinter as tk
import tkinter as tk
from secrets import choice
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *
from tkinter import ttk

from itertools import count
from logging import root
from operator import length_hint
from struct import pack
import tkinter as tk
from tkinter import HORIZONTAL, Button, Label, Tk, ttk
from threading import Thread
from urllib.request import urlretrieve, urlcleanup
import time

def callback(*args):
    #DEVUELVE LA VARIABLE SELECCIONADA EN EL MENU DESPLEGABLE "CABALLOS"
    labelTest.configure(text="Va a apostar al {}".format(variable.get()))

def carrera():
    #SE SIMULA LA CARRERA CON LOS 4 CABALLOS Y MUESTRA EN UNA NUEVA VENTANA SI ES QUE EL CABALLO ELEGIDO PERDIÓ O GANÓ
    

    opcion = variable.get()
    caballo1 = 0
    caballo2 = 0
    caballo3 = 0
    caballo4 = 0
    
    while caballo1 < 100 and caballo2 < 100 and caballo3 < 100 and caballo4 < 100:

        caballo1 += random.randrange(1, 10)
        caballo2 += random.randrange(1, 10)
        caballo3 += random.randrange(1, 10)
        caballo4 += random.randrange(1, 10)
            
        
        print("Caballo 1: " + str(caballo1))
        print("Caballo 2: " + str(caballo2)) 
        print("Caballo 3: " + str(caballo3)) 
        print("Caballo 4: " + str(caballo4)) 

    if opcion == 'Caballo 1' and caballo1 > 99:
        pop_label = Label(pop, text="El caballo 1 Ganó")
        pop_label.pack(pady=10)
    elif opcion == 'Caballo 1' and caballo1 < 99:
        pop_label = Label(pop, text="El caballo 1 perdió")
        pop_label.pack(pady=10)

    if opcion == 'Caballo 2' and caballo2 > 99:
        pop_label = Label(pop, text="El caballo 2 Ganó")
        pop_label.pack(pady=10)
    elif opcion == 'Caballo 2' and caballo2 < 99:    
        pop_label = Label(pop, text="El caballo 2 perdió")
        pop_label.pack(pady=10)

    if opcion == 'Caballo 3' and caballo3 > 99:
        pop_label = Label(pop, text="El caballo 3 Ganó")
        pop_label.pack(pady=10)
    elif opcion == 'Caballo 3' and caballo3 < 99:    
        pop_label = Label(pop, text="El caballo 3 perdió")
        pop_label.pack(pady=10)
        
    if opcion == 'Caballo 4' and caballo4 > 99:
        pop_label = Label(pop, text="El caballo 4 Ganó")
        pop_label.pack(pady=10)
    elif opcion == 'Caballo 4' and caballo4 < 99:    
        pop_label = Label(pop, text="El caballo 4 perdió") 
        pop_label.pack(pady=10)

        

#label boton
def click():
    #AQUÍ SE MUESTRA LA VENTANA DEL FINAL DE LA CARRERA JUNTO AL TEXTO DE QUE SI GANÓ O PERDIÓ
    global pop
    pop = Toplevel(root) 
    pop.title("Final de la carrera")
    pop.geometry("350x200")

    carrera()

    my_frame = Frame(pop)
    my_frame.pack(pady=5)

OptionList = [
"Caballo 1",
"Caballo 2",
"Caballo 3",
"Caballo 4"
] 

root = tk.Tk()

bit = root.iconbitmap('cab-vec.ico')
root.geometry('800x800')
root.resizable(False, False)
root.title('Hipódromo')

# label
label = ttk.Label(text="A qué caballo desea apostar:")
label.pack(fill=tk.X, padx=5, pady=5)

variable = tk.StringVar(root)
variable.set(OptionList[0])

opt = tk.OptionMenu(root, variable, *OptionList)
opt.config(width=90)
opt.pack(side="top")


labelTest = tk.Label(text="")
labelTest.pack(side="top")

variable.trace("w", callback)

# label 2
label = ttk.Label(text="Cuanto desea apostar al caballo: ")
label.pack(fill=tk.X, padx=5, pady=5)

#campo de texto
apuesta=tk.StringVar()
apuesta=tk.Entry(root,textvariable=apuesta)
apuesta.pack(fill=tk.X, padx=5, pady=5)

button = tk.Button(root, text='Apostar', width=5, command=click)
button.pack(fill=tk.X, padx=5, pady=5)

my_label = Label(root, text="")
my_label.pack(pady=20)


root.mainloop()