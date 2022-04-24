########################################### Descripción del proyecto: ###########################################
#   Programa en Python que simula una carrera de caballos.
#   Descipción:
#    - Se creará un programa que simule una carrera de caballos con avance aleatorio.
#    - Código desarrollado mediante metodología de programación modular, con el objetivo de reutilizar bibliotecas de funciones y/o métodos.
#    - Versión: 0.1 (Prueba y demostración)
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

def __init__( self, nombre = None, maxPasosPorTurno = 10):
    """
    Constructor.
    @param nombre Nombre del caballo.
    @param maxPasosPorTurno Máximo de pasos que puede alcanzar en un turno.
    """
    self.nombre = nombre
    self.maxPasosPorTurno = 10
    self.__carreras = []
    self.__pasosCarreraActual = 0

def stop():
    #REINICIA LAS BARRAS DE PROGRESO PARA COMENZAR OTRA CARRERA
    my_progress.stop()
    my_progress2.stop()
    my_progress3.stop()
    my_progress4.stop()

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

    while caballo1 < 30 and caballo2 < 30 and caballo3 < 30 and caballo4 < 30:

        caballo1 += random.randrange(1, 10)
        caballo2 += random.randrange(1, 10)      
        caballo3 += random.randrange(1, 10)
        caballo4 += random.randrange(1, 10)
            
        for x in range(1):
            my_progress['value'] += caballo1
            my_progress2['value'] += caballo2
            my_progress3['value'] += caballo3
            my_progress4['value'] += caballo4
            root.update_idletasks()
            time.sleep(0.5)
        
        print("Caballo 1: " + str(caballo1))
        print("Caballo 2: " + str(caballo2)) 
        print("Caballo 3: " + str(caballo3)) 
        print("Caballo 4: " + str(caballo4)) 

    if opcion == 'Caballo 1' and caballo1 > 30:
        pop_label = Label(pop, text="El caballo 1 Ganó")
        pop_label.pack(pady=10)
    elif opcion == 'Caballo 1' and caballo1 < 30:
        pop_label = Label(pop, text="El caballo 1 perdió")
        pop_label.pack(pady=10)

    if opcion == 'Caballo 2' and caballo2 > 30:
        pop_label = Label(pop, text="El caballo 2 Ganó")
        pop_label.pack(pady=10)
    elif opcion == 'Caballo 2' and caballo2 < 30:    
        pop_label = Label(pop, text="El caballo 2 perdió")
        pop_label.pack(pady=10)

    if opcion == 'Caballo 3' and caballo3 > 30:
        pop_label = Label(pop, text="El caballo 3 Ganó")
        pop_label.pack(pady=10)
    elif opcion == 'Caballo 3' and caballo3 < 30:    
        pop_label = Label(pop, text="El caballo 3 perdió")
        pop_label.pack(pady=10)
        
    if opcion == 'Caballo 4' and caballo4 > 30:
        pop_label = Label(pop, text="El caballo 4 Ganó")
        pop_label.pack(pady=10)
    elif opcion == 'Caballo 4' and caballo4 < 30:    
        pop_label = Label(pop, text="El caballo 4 perdió") 
        pop_label.pack(pady=10)

        
#label boton
def click():
    #AQUÍ SE MUESTRA LA VENTANA DEL FINAL DE LA CARRERA JUNTO AL TEXTO DE QUE SI GANÓ O PERDIÓ
    
    global pop
    pop = Toplevel(root) 
    pop.iconbitmap('cab-vec.ico')
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

###############################################     INTERFAZ   ######################################################################################################
root = tk.Tk()

bit = root.iconbitmap('cab-vec.ico')
root.geometry('800x1000')
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
#######################################################################################################################################################################

###############################################     BARRA DE PROGRESO    ##############################################################################################

label = ttk.Label(text="Caballo 1 ")
label.pack(fill=tk.X, padx=100, pady=5)

my_progress = ttk.Progressbar(root, orient=HORIZONTAL, length=600, mode='determinate')
my_progress.pack(pady=20)

label = ttk.Label(text="Caballo 2 ")
label.pack(fill=tk.X, padx=100, pady=5)

my_progress2 = ttk.Progressbar(root, orient=HORIZONTAL, length=600, mode='determinate')
my_progress2.pack(pady=20)


label = ttk.Label(text="Caballo 3 ")
label.pack(fill=tk.X, padx=100, pady=5)

my_progress3 = ttk.Progressbar(root, orient=HORIZONTAL, length=600, mode='determinate')
my_progress3.pack(pady=20)


label = ttk.Label(text="Caballo 4 ")
label.pack(fill=tk.X, padx=100, pady=5)

my_progress4 = ttk.Progressbar(root, orient=HORIZONTAL, length=600, mode='determinate')
my_progress4.pack(pady=20)

label = ttk.Label(text="Caballo 5 ")
label.pack(fill=tk.X, padx=100, pady=5)

my_progress4 = ttk.Progressbar(root, orient=HORIZONTAL, length=600, mode='determinate')
my_progress4.pack(pady=20)

label = ttk.Label(text="Caballo 6 ")
label.pack(fill=tk.X, padx=100, pady=5)

my_progress4 = ttk.Progressbar(root, orient=HORIZONTAL, length=600, mode='determinate')
my_progress4.pack(pady=20)

label = ttk.Label(text="Caballo 7 ")
label.pack(fill=tk.X, padx=100, pady=5)

my_progress4 = ttk.Progressbar(root, orient=HORIZONTAL, length=600, mode='determinate')
my_progress4.pack(pady=20)

my_button = Button(root, text="Reiniciar", command=stop)
my_button.pack(pady=20)

my_label = Label(root, text="")
my_label.pack(pady=20)
########################################################################################################################################################################
root.mainloop()