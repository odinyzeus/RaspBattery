import tkinter as tk

class AplicacionTkinter:
    total_columns = 3
    def __init__(self, ventana_principal:tk):        
        # the principal window parameters are setting here
        self.ventana_principal = ventana_principal
        # Establecer dimensiones mínimas de la ventana principal
        self.ventana_principal.minsize(width=800, height=600) 
        self.ventana_principal.title("Digital Lock-In Amplifier for Thermography Applications")
        self.ventana_principal.resizable(True,True)
        self.ventana_principal.bind("<Configure>", self.adjust_content)
        
        # Makes the application header 
        self.frame_header = tk.Frame(self.ventana_principal,height= 150,padx=5,pady=5)
        self.frame_header.pack(expand=True,fill=tk.BOTH) 
        self.frame_header.grid(row=0, column=0, columnspan=self.total_columns, padx=5, pady=5)
    
   
   
   
        # Crear la cuadrícula de 4 celdas
        self.frame_camara_usb = tk.Frame(self.ventana_principal, bg="lightblue", padx=10, pady=10)
        self.frame_camara_usb.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        self.frame_video_archivo = tk.Frame(self.ventana_principal, bg="lightgreen", padx=10, pady=10)
        self.frame_video_archivo.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
        
        self.frame_campos_texto = tk.Frame(self.ventana_principal, bg="lightyellow", padx=10, pady=10)
        self.frame_campos_texto.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        
        self.frame_info_sistema = tk.Frame(self.ventana_principal, bg="lightcoral", padx=10, pady=10)
        self.frame_info_sistema.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        # Barra de estado
        self.barra_estado = tk.Label(self.ventana_principal, text="Barra de estado", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.barra_estado.grid(row=3, columnspan=2, sticky="ew")
        
        # Menú principal
        self.menu_principal = tk.Menu(self.ventana_principal)
        self.menu_principal.add_command(label="Archivo", command=self.dummy)
        self.menu_principal.add_command(label="Editar", command=self.dummy)
        self.menu_principal.add_command(label="Ayuda", command=self.dummy)
        self.ventana_principal.config(menu=self.menu_principal)

        # Agregar contenido a los frames
        self.add_content()
        
    def add_content(self):
        # Campos de texto para datos del sistema
        tk.Label(self.frame_campos_texto, text="Datos de la cámara web").pack()
        tk.Entry(self.frame_campos_texto).pack()
        tk.Entry(self.frame_campos_texto).pack()
        
        tk.Label(self.frame_campos_texto, text="Información del sistema").pack()
        tk.Entry(self.frame_campos_texto).pack()
        tk.Entry(self.frame_campos_texto).pack()

        # Frames para reproducción de video
        tk.Label(self.frame_camara_usb, text="Video de cámara USB").pack()
        # Aquí puedes agregar el código para capturar video de la cámara USB
        
        tk.Label(self.frame_video_archivo, text="Video cargado desde archivo").pack()
        # Aquí puedes agregar el código para reproducir un video desde un archivo

    def adjust_content(self, event):
    # Adjust the size of application in real time
        num_filas = self.ventana_principal.grid_size()[1] 
        for i in range(1, num_filas):  # Puedes ajustar este rango según la cantidad de filas en tu diseño
            self.ventana_principal.grid_rowconfigure(i, weight=1)
               
        self.ventana_principal.grid_columnconfigure(0, weight=1)


    def dummy(self):
        pass
    
ventana_principal = tk.Tk()