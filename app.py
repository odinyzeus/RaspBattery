import tkinter as tk
import Thermography as tg

# Función que se ejecutará al hacer clic en el botón
def on_button_click():
    label.config(text="¡Hola, Mundo!")

# Crear la ventana
root = tk.Tk()
root.title(tg.Video_Device)

# Crear un widget de etiqueta (label) y colocarlo en la ventana
label = tk.Label(root, text="¡Hola!")
label.pack()

# Crear un widget de botón y colocarlo en la ventana
button = tk.Button(root, text="Haz clic aquí", command=on_button_click)
button.pack()

# Bucle principal de la ventana
root.mainloop()
