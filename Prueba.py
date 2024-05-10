import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttks

def seleccionar(value):
    print(f"Has seleccionado: {value}")

def main():
    # Crear la ventana principal
    ventana = ttks.Style().master
    ventana.geometry('300x200')

    # Crear un labelframe con ttkbootstrap
    labelframe = ttks.LabelFrame(ventana, text="Menú")
    labelframe.pack(fill='both', expand='yes')

    # Crear las opciones del menú
    opciones = ['Opción 1', 'Opción 2', 'Opción 3']

    # Crear una variable para almacenar la opción seleccionada
    opcion_seleccionada = tk.StringVar()

    # Crear los radiobuttons
    for opcion in opciones:
        radiobutton = ttk.Radiobutton(labelframe, text=opcion, variable=opcion_seleccionada, value=opcion, command=lambda: seleccionar(opcion_seleccionada.get()))
        radiobutton.pack(anchor='w')

    ventana.mainloop()

if __name__ == "__main__":
    main()
