import tkinter as tk

import Header as Hdr
import Footer as Ftr
import Body as Bdy 

from Constants import *



get_progress = lambda value: round((value/300)*100) 
    

def get_contained_frames(master_frame):
    contained_frames = []
    for widget in master_frame.pack_slaves():
        if isinstance(widget, ttk.Frame):
            contained_frames.append(widget)
    return contained_frames


def set_gui(self:ttk.Frame):
    Hdr.header_create(self)
    Bdy.body_create(self)
    Ftr.footer_create(self)









class Application(ttk.Frame):
    # Body Section Configure
    
   
    # Constructor 
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill=BOTH, expand=YES)
        master.bind("<Configure>", self.adjust_content)     # bind "configure" event to adjust's method
    
        """_summary_          
        # option notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.grid(row=1, column=1, sticky=NSEW, pady=(5, 0))

        # windows tab
        self.windows_tab = ttk.Frame(notebook, padding=PADDING)
        wt_scrollbar = ttk.Scrollbar(windows_tab)
        wt_scrollbar.pack(side=RIGHT, fill=Y)
        wt_scrollbar.set(0, 1)

        wt_canvas = ttk.Canvas(
            master=windows_tab,
            relief=FLAT,
            borderwidth=0,
            selectborderwidth=0,
            highlightthickness=0,
            yscrollcommand=wt_scrollbar.set
        )
        wt_canvas.pack(side=LEFT, fill=BOTH)

        # adjust the scrollregion when the size of the canvas changes
        wt_canvas.bind(
            sequence='<Configure>',
            func=lambda e: wt_canvas.configure(
                scrollregion=wt_canvas.bbox(ALL))
        )
        wt_scrollbar.configure(command=wt_canvas.yview)
        scroll_frame = ttk.Frame(wt_canvas)
        wt_canvas.create_window((0, 0), window=scroll_frame, anchor=NW)
        
        method_options = [
            'Fourier', 'Geometrical', 'four points'
        ]
        
        device_options = ['File video','Camera device']
        
        edge_method = ttk.Labelframe(
            master=scroll_frame,
            text='Processing data method',
            padding= PADDING
        )
        edge_method.pack(fill=BOTH, expand=YES)
        
        # Variable de control para el grupo de botones de radio
        self.Method_selected = StringVar()
        # add radio buttons to each label frame section
        for section in [edge_method]:
            for i,opt in enumerate(method_options):
                cb = ttk.Radiobutton(section, text=opt, state=NORMAL,variable=self.Method_selected,value=i)
                #cb.invoke()
                cb.pack(side=TOP, pady=2, fill=X)
                
        self.notebook.add(self.windows_tab, text='Methods')
        
        
        
    def show_methods_tab(self):
        # Mostrar el tab "Methods" cuando se presione el botón "Options"
        self.notebook.select(self.windows_tab)
        """





class ApplicationTkinter:
    total_columns = 3               # Defines the maximum number of columns of app's grid
    Win: any
    Title:str
    wpadX = 3
    wpadY = 3
    border = 2

"""
class AplicacionTkinter:    
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

    def dany(self):
         # Makes the application body section
        self.frame_body   = tk.Frame(self.Win,padx=self.PadX,pady=self.PadY)
        self.frame_body.grid(row=1, column=0, columnspan=self.total_columns, padx=self.PadX, pady=self.PadY)

        # Makes the application footer section 
        self.frame_footer  = tk.Frame(self.Win,padx=self.PadX,pady=self.PadY)
        self.frame_footer.grid(row=2, column=0, columnspan=self.total_columns, padx=self.PadX, pady=self.PadY)

        
        
        
        self.add_body()     
"""