import tkinter as tk
import ttkbootstrap as ttk
import Header as Hdr
import Footer as Ftr
import Body as Bdy 
from pathlib import Path
from Constants import *

PATH = Path(__file__).parent / 'assets'

def dummy(self):
        pass
    
def set_win2center(self:ttk.Frame):
    # Configurar ventana en el centro de la pantalla
    screen_width = self.winfo_screenwidth()     # gets the screen's width
    screen_height = self.winfo_screenheight()   # gets the screen's height
    window_width = self.winfo_width()           # gets the window's width
    window_height = self.winfo_height()         # gets the window's height
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    self.geometry(f'{window_width}x{window_height}+{x}+{y}')

def get_contained_frames(master_frame):
    contained_frames = []
    for widget in master_frame.pack_slaves():
        if isinstance(widget, ttk.Frame):
            contained_frames.append(widget)
    return contained_frames
    
def set_menu(self:ttk.Frame):
    """
    Creates the principal menu of the application
    """
    _mnu = ttk.Menu(self)
    _mnu.add_command(label="Archivo", command=dummy(self))
    _mnu.add_command(label="Editar", command=dummy(self))
    _mnu.add_command(label="Ayuda", command=dummy(self))
    self.config(menu=_mnu)

def set_gui(self:ttk.Frame):
    # application images
    self.images = [
    ttk.PhotoImage(
        name='logo',
        file=PATH / 'icons8_broom_64px_1.png'),
    ttk.PhotoImage(
        name='cleaner',
        file=PATH  / 'icons8_broom_64px.png'),
    ttk.PhotoImage(
        name='registry',
        file=PATH  / 'icons8_registry_editor_64px.png'),
    ttk.PhotoImage(
        name='tools',
        file=PATH  / 'icons8_wrench_64px.png'),
    ttk.PhotoImage(
        name='options',
        file=PATH  / 'icons8_settings_64px.png'),
    ttk.PhotoImage(
        name='privacy',
        file=PATH  / 'icons8_spy_80px.png'),
    ttk.PhotoImage(
        name='junk',
        file=PATH  / 'icons8_trash_can_80px.png'),
    ttk.PhotoImage(
        name='protect',
        file=PATH  / 'icons8_protect_40px.png')
    ]

    Hdr.header_create(self)
    Bdy.body_create(self)
    Ftr.footer_create(self)









class Application(ttk.Frame):
    # Body Section Configure
    # creates the ribbon section 
    def _create_ribbon_left(self):
        # acción para el botón "Options"
        _options_btn = ttk.Button(
            master=self._body_left_frame,
            image='options',
            text='options',
            compound=TOP,
            bootstyle=INFO,
            command=self._show_methods_tab  # Llamará a la función cuando se presione el botón
        )
        _options_btn.pack(side=TOP, fill=BOTH)
    
    # Initializing body frame
    def _init_body(self):
        # header initializer
        self._body_frame = ttk.Frame(self, padding=self.Frame_Padding, bootstyle=DEFAULT_THEME,borderwidth=1, relief=SOLID, height=50)
        self._body_frame.grid(row=1, column=0, sticky=NSEW)
        # Creates the ribbon left section.
        
        self._body_left_frame = ttk.Frame(
            self._body_frame, 
            padding=self.Frame_Padding, 
            bootstyle = SECONDARY,
            borderwidth=1,
            relief=SOLID,
            width=250
            )
        self._body_left_frame.pack(fill=BOTH,side=LEFT,padx=5)
        
        self._body_right_frame = ttk.Frame(
            self._body_frame, 
            padding=self.Frame_Padding, 
            bootstyle = SECONDARY,
            borderwidth=1,
            relief=SOLID,
            width=250
            )
        self._body_right_frame.pack(fill=BOTH,side=RIGHT, padx=5)
        
        self._body_center_frame = ttk.Frame(
            self._body_frame,
            padding=self.Frame_Padding,
            bootstyle = SECONDARY,
            borderwidth=1,
            relief=SOLID
            )
        self._body_center_frame.pack(fill=BOTH,side=LEFT,padx=5,expand=TRUE)
        self._create_ribbon_left()  

    
    # Constructor 
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.pack(fill=BOTH, expand=YES)
        
                                
        
        master.bind("<Configure>", self.adjust_content)     # bind "configure" event to adjust's method

        
        # Creates the menu
        self._init_menu()
        # Header section of application
        self._init_hdr()
        
        # Body section of application
        self._init_body()
        
        # Footer section of application
        self._init_footer()
    
    def _show_methods_tab(self):
        self._status_bar.config(text=f'Presionaste el boton de configurar')
            

    
    # Properties section   
    @property
    def Frame_Padding(self) -> int:
        return self._frame_padding
        
    @Frame_Padding.setter
    def Frame_Padding(self,value:int):
        self._frame_padding = value
    
    
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
    
    def __init__(self, theme:str = "superhero") -> None:    
        #self.Win.iconbitmap()
        
       
        
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



"""
class AplicacionTkinter:
        
        
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

    

    def dany(self):
         # Makes the application body section
        self.frame_body   = tk.Frame(self.Win,padx=self.PadX,pady=self.PadY)
        self.frame_body.grid(row=1, column=0, columnspan=self.total_columns, padx=self.PadX, pady=self.PadY)

        # Makes the application footer section 
        self.frame_footer  = tk.Frame(self.Win,padx=self.PadX,pady=self.PadY)
        self.frame_footer.grid(row=2, column=0, columnspan=self.total_columns, padx=self.PadX, pady=self.PadY)

        
        
        
        self.add_body()


        
"""