#from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ApplicationTkinter:
    total_columns = 3               # Defines the maximum number of columns of app's grid
    Win: any
    Title:str
    wpadX = 3
    wpadY = 3
    border = 2
    
    def __init__(self, theme:str = "superhero") -> None:
        # the principal window parameters are setting here
        self.Win = ttk.Window(themename=theme)      # Defines the graphic window and theme for app's GUI
        self.Win.title('Digital Lock-In Amplifier for Thermography Applications')       
        #self.Win.iconbitmap()
        self.Win.minsize(width=800, height=600)     # Set minsize of GUI
        self.Win.resizable(True,True)               # The App can be resized
        
        # Makes the application menu
        self.menu_principal = ttk.Menu(self.Win)
        self.menu_principal.add_command(label="Archivo", command=self.dummy)
        self.menu_principal.add_command(label="Editar", command=self.dummy)
        self.menu_principal.add_command(label="Ayuda", command=self.dummy)
        self.Win.config(menu=self.menu_principal)
        
        # Creates principal frame 
        self.main_frame = ttk.Frame(self.Win)
        self.main_frame.pack(side=TOP, fill=BOTH, expand=True)
        
        # Creates status bar frame
        self.statusbar = ttk.Label(self.Win, text="Estado: Listo", style="info.TLabel")
        self.statusbar.pack(side=BOTTOM,fill=X,expand=True)
        #self.statusbar.grid(row=3, column=0, columnspan=self.total_columns, sticky=EW,pady=(0, 5),ipady = 15)
        
    
        self.frame_header = ttk.Frame(self.main_frame,bootstyle=SECONDARY,borderwidth=self.border)
        self.frame_header.grid(row=0, column=0, columnspan=self.total_columns, sticky=EW)
        #self.frame_header.pack(side=ttk.TOP, fill=ttk.BOTH, expand=True, padx=self.wpadX, pady=self.wpadY)
        
        self.frame_body = ttk.Frame(self.main_frame, bootstyle=SECONDARY,borderwidth=self.border)
        self.frame_body.grid(row=1, column=0, columnspan=self.total_columns, sticky=EW)
        #self.frame_body.pack(side=ttk.TOP, fill=ttk.BOTH, expand=True, padx=self.wpadX, pady=self.wpadY)
        
        self.frame_footer = ttk.Frame(self.main_frame,bootstyle=SECONDARY,borderwidth=self.border)
        self.frame_footer.grid(row=2, column=0, columnspan=self.total_columns, sticky=EW)
        #self.frame_footer.pack(side=ttk.TOP, fill=ttk.BOTH, expand=True, padx=self.wpadX, pady=self.wpadY)    
        
        
        
        self.add_header()
        
        self.Win.mainloop()

    def add_header(self):
        # Crear el frame para el header
        pass

    def dummy(self):
        pass

"""
class AplicacionTkinter:
    
    Win = tk.Tk()                   
    
    def __init__(self):                
                     
        self.Win.resizable(True,True)                         
        self.Win.bind("<Configure>", self.adjust_content)     # bind "configure" event to adjust's method
        
        
        
        # Makes the application header section 
        self.frame_header = tk.Frame(self.Win,height= 150,padx=self.PadX,pady=self.PadY) 
        self.frame_header.grid(row=0, column=0, columnspan=self.total_columns, padx=self.PadX, pady=self.PadY)
        self.add_border(self.frame_header)
        
       
        self.Win.mainloop()
        
        
    def add_body(self):
        _summary_
        This function makes the body appeareance and format desired
        
        
        self.frame_camara_usb = tk.Frame(self.frame_body, bg="lightblue", padx=self.PadX, pady=self.PadY)
        self.frame_camara_usb.grid(row=0, column=0, padx=self.PadX, pady=self.PadY, sticky="nsew")
        self.add_border(self.frame_camara_usb)
        
        self.frame_video_archivo = tk.Frame(self.frame_body, bg="lightgreen", padx=self.PadX, pady=self.PadY)
        self.frame_video_archivo.grid(row=1, column=0, padx=self.PadX, pady=self.PadY, sticky="nsew")
        self.add_border(self.frame_video_archivo)
        
        self.frame_campos_texto = tk.Frame(self.frame_body, bg="lightyellow", padx=self.PadX, pady=self.PadY)
        self.frame_campos_texto.grid(row=0, column=1, padx=self.PadX, pady=self.PadY, sticky="nsew")
        self.add_border(self.frame_campos_texto)
        
        self.frame_info_sistema = tk.Frame(self.frame_body, bg="lightcoral", padx=self.PadX, pady=self.PadY)
        self.frame_info_sistema.grid(row=1, column=1, padx=self.PadX, pady=self.PadY, sticky="nsew")
        self.add_border(self.frame_info_sistema)

        # Agregar contenido a los frames
        self.add_content()
        

    def add_border(self, frame):
    # Agregar un borde alrededor del frame
        border = tk.Frame(frame, borderwidth=2, relief="groove")
        border.pack(expand=True, fill="both")

        
        
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
        num_filas = self.Win.grid_size()[1] 
        for i in range(1, num_filas):  # Puedes ajustar este rango según la cantidad de filas en tu diseño
            self.Win.grid_rowconfigure(i, weight=1)
               
        self.Win.grid_columnconfigure(0, weight=1)


    def dany(self):
         # Makes the application body section
        self.frame_body   = tk.Frame(self.Win,padx=self.PadX,pady=self.PadY)
        self.frame_body.grid(row=1, column=0, columnspan=self.total_columns, padx=self.PadX, pady=self.PadY)

        # Makes the application footer section 
        self.frame_footer  = tk.Frame(self.Win,padx=self.PadX,pady=self.PadY)
        self.frame_footer.grid(row=2, column=0, columnspan=self.total_columns, padx=self.PadX, pady=self.PadY)

        
        
        
        self.add_body()


        
"""