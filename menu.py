from secrets import choice
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from tkinter import *
from tkinter import ttk


root = tk.Tk()

bit = root.iconbitmap('cab-vec.ico')
# config ventana raiz
root.geometry('800x800')
root.resizable(False, False)
root.title('Hipódromo')

# label
label = ttk.Label(text="A qué caballo desea apostar:")
label.pack(fill=tk.X, padx=5, pady=5)

# combobox
caballo = tk.StringVar()
options = ttk.Combobox(root, textvariable=caballo)

options['values'] = ["Caballo 1", "Caballo 2", "Caballo 3", "Caballo 4"]

# evita escribir en el menú combobox
options['state'] = 'readonly'

# ubicacion combobox
options.pack(fill=tk.X, padx=5, pady=5)

# label 2
label = ttk.Label(text="Cuanto desea apostar al caballo: ")
label.pack(fill=tk.X, padx=5, pady=5)

#campo de texto
apuesta=tk.StringVar()
apuesta=tk.Entry(root,textvariable=apuesta)
apuesta.pack(fill=tk.X, padx=5, pady=5)

#label boton

def click():
    global pop
    pop = Toplevel(root) 
    pop.title("Final de la carrera")
    pop.geometry("350x200")

    pop_label = Label(pop, text="El caballo ganador es tu mamá")
    pop_label.pack(pady=10)

    my_frame = Frame(pop)
    my_frame.pack(pady=5)

button = tk.Button(root, text='Apostar', width=5, command=click)
button.pack(fill=tk.X, padx=5, pady=5)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()