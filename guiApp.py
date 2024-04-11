import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Constants import *

class Body_Options(ttk.Frame):
    # creates the ribbon section 
    btnOptions :ttk.Button
    btnTools   :ttk.Button
    btnMethod  :ttk.Button
     
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid(row=0,column=0,sticky=NSEW)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(3,weight=1)
   
        self.imgOptions = ttk.PhotoImage(name='options', file=PATH / 'icons8_settings_64px.png')    
        self.imgTools   = ttk.PhotoImage(name='tools', file=PATH / 'icons8_wrench_64px.png')
        self.imgMethod  = ttk.PhotoImage(name='method', file=PATH /'icons8_registry_editor_64px.png')
        
        self.btnOptions = ttk.Button(master=self,
                                    image=self.imgOptions,
                                    text=self.imgOptions.name,
                                    compound=TOP,
                                    bootstyle=INFO
                                    )
        self.btnOptions.grid(row=0,column=0,sticky=EW)
        self.btnTools = ttk.Button(master=self,
                                    image=self.imgTools,
                                    text=self.imgTools.name,
                                    compound=TOP,
                                    bootstyle=INFO
                                    )
        self.btnTools.grid(row=1,column=0,sticky=EW)
        self.Method = ttk.Button(master=self,
                                    image=self.imgMethod,
                                    text=self.imgMethod.name,
                                    compound=TOP,
                                    bootstyle=INFO
                                    )
        self.Method.grid(row=2,column=0,sticky=EW)        
  
class main_menu(ttk.Menu):
    """
        Creates the principal menu of the application
    """    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.add_command(label="Archivo", command= self.dummy)
        self.add_command(label="Editar", command= self.dummy)
        self.add_command(label="Ayuda",command=self.dummy)
    
    def dummy(self):
        print(f'presionaste el menu')
  
class main_frame(ttk.Frame):
    """
        This Class allow to create and manipuling the principal frame of the application
        its a Frame herencied 
    Args:
        ttk.Frame args: 
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config(relief=ttk.SOLID)
        self.config(padding=3)
        self.config(bootstyle=ttk.PRIMARY)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(1,weight=1)
        self.pack(fill=BOTH,expand=YES)

class main_header(ttk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config(relief=ttk.SOLID)
        self.config(padding=3)
        self.config(bootstyle=ttk.SECONDARY)
        self.grid(row=0,column=0,sticky=NSEW)
        self.columnconfigure(1,weight=1)

        self.frmLogo = ttk.Frame(master = self)
        self.frmCenter = ttk.Frame(master = self)
        self.imgLogo = ttk.PhotoImage(name='logo', file=PATH / 'icons8_broom_64px_1.png')
        self.txtLogo = ttk.Label(master=self.frmLogo,image=self.imgLogo, bootstyle=(INVERSE, SECONDARY))
        self.txtHeader = ttk.Label(master=self.frmCenter) 
        
        self.frmLogo.config(relief=SOLID)
        self.frmLogo.config(bootstyle=DEFAULT_THEME)
        self.frmLogo.config(padding= self.cget('padding'))
        self.frmLogo.grid(row=0,column=0,sticky=NSEW)
        
        self.txtLogo.image = self.imgLogo
        self.txtLogo.pack(fill=BOTH,expand=YES)

        self.frmCenter.config(relief=SOLID)
        self.frmCenter.config(bootstyle=DEFAULT_THEME)
        self.frmCenter.config(padding= self.cget('padding'))
        self.frmCenter.grid(row=0,column=1,sticky=NSEW)

        self.txtHeader.config(text= PRG_HDR_TEXT)
        self.txtHeader.config(font=('TkDefaultFixed', 12))
        self.txtHeader.config(padding= self.cget('padding'))
        self.txtHeader.config(bootstyle=(INVERSE, SECONDARY))
        self.txtHeader.config(justify=CENTER)
        self.txtHeader.config(anchor=CENTER)
        self.txtHeader.pack(fill=BOTH,expand=YES)

class main_footer(ttk.Frame):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config(relief=ttk.SOLID)
        self.config(padding=3)
        self.config(bootstyle=ttk.SECONDARY)
        self.grid(row=2,column=0,sticky=NSEW)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0,weight=1)
        
        self.frmStatus = ttk.Frame(master = self)
        self.frmProgress=ttk.Frame(master= self)
        self.lblStatus = ttk.Label(master = self.frmStatus)
        self.progressBar = ttk.Progressbar(master=self.frmProgress)

        ttk.Label(self.frmProgress,font=('Helvetica', 10, 'italic'), text='%').pack(side=RIGHT,padx=PADX)
        ttk.Label(self.frmProgress,font=('Helvetica', 10, 'italic'), textvariable='Progress').pack(side=RIGHT)

        self.frmStatus.config(relief=ttk.SOLID)
        self.frmStatus.config(bootstyle=ttk.SECONDARY)
        self.frmStatus.grid(row=0,column=0,sticky=NSEW)

        self.frmProgress.config(relief=ttk.SOLID)
        self.frmProgress.config(bootstyle=ttk.SECONDARY) 
        self.frmProgress.grid(row=0,column=1,sticky=NSEW)

        self.lblStatus.config(text= txt_Status_Default)
        self.lblStatus.config(font=('Helvetica', 10, 'italic'))
        self.lblStatus.config(padding= self.cget('padding'))
        self.lblStatus.config(bootstyle=INFO)
        self.lblStatus.config(textvariable= 'Status')
        self.lblStatus.pack(fill=BOTH,expand=YES)

        self.progressBar.config(mode=DETERMINATE)
        self.progressBar.config(orient=HORIZONTAL)
        self.progressBar.config(variable='Progress')
        self.progressBar.place(relx=0.02,rely=0.5,relwidth=0.92,anchor=W)

        # settings of control's variables
        self.setvar('Status',txt_Status_Default)
        self.setvar('Progress',25)

class main_body(ttk.Frame):
    footer : main_footer
    body_options: Body_Options

    def __init__(self, **kwargs):
        self.footer = kwargs.pop('footer',None)
        super().__init__(**kwargs)
        self.config(relief=ttk.SOLID)
        self.config(padding=3)
        self.config(bootstyle=ttk.SECONDARY)
        self.grid(row=1,column=0,sticky=NSEW)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0,weight=1)
            
        self.body_options = Body_Options(master = self)
        # self.Process = Body_Process(master=self,relief=kwargs['relief'],bootstyle=LIGHT)
                  




if __name__ == "__main__":
    __app = ttk.Window(PRG_NAME, PRG_THEME)         # Creates the principal window for application
    frm = main_frame(master=__app)
    __app.config(menu=main_menu(master=__app))      # Defines that principal menu in principal application
    __app.minsize(width=800, height=600)            # Sets the minimum size of GUI   
    __app.mainloop()                                # event's loop





























get_progress = lambda value: round((value/300)*100) 
    

def get_contained_frames(master_frame):
    contained_frames = []
    for widget in master_frame.pack_slaves():
        if isinstance(widget, ttk.Frame):
            contained_frames.append(widget)
    return contained_frames










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