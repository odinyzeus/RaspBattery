import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Constants import *

class VideoPlayer(ttk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack(side=TOP,
                  padx=PADX,
                  pady=PADY,
                  expand=YES,
                  fill=BOTH
                )
        
        """Create frame to contain media"""
        self.imgAtras = ttk.PhotoImage(name='Player', file=PATH / 'mp_background.png')
        
        self.media = ttk.Label(self, image=self.imgAtras)
        self.media.pack(fill=BOTH, expand=YES)
    
class VideoMeter(ttk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack(side=TOP,
                  padx=PADX,
                  pady=PADY,
                  fill=X
                )       
        
        """Create frame with progress meter with lables"""
        container = ttk.Frame(master = self,relief=kwargs['relief'])
        container.pack(side=TOP,fill=X, expand=YES, pady=10)
             
        self.elapse = ttk.Label(container, text='00:00')
        self.elapse.pack(side=LEFT, padx=10)

        self.scale = ttk.Scale(
            master=container, 
            command=self.on_progress, 
            bootstyle=SECONDARY
        )
        self.scale.pack(side=LEFT, fill=X, expand=YES)

        self.remain = ttk.Label(container, text='03:10')
        self.remain.pack(side=LEFT, fill=X, padx=10)
        
    def on_progress(self, val: float):
        """Update progress labels when the scale is updated."""
        elapsed = self.elapsed_var.get()
        remaining = self.remain_var.get()
        total = int(elapsed + remaining)
        
        elapse = int(float(val) * total)
        elapse_min = elapse // 60
        elapse_sec = elapse % 60
        
        remain_tot = total - elapse
        remain_min = remain_tot // 60
        remain_sec = remain_tot % 60

        self.elapsed_var.set(elapse)
        self.remain_var.set(remain_tot)

        self.elapse.configure(text=f'{elapse_min:02d}:{elapse_sec:02d}')
        self.remain.configure(text=f'{remain_min:02d}:{remain_sec:02d}')

class VideoControls(ttk.Frame):
    btnAtras :ttk.Button
    btnPlay :ttk.Button
    btnPause: ttk.Button
    btnAdelante: ttk.Button
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack(side=BOTTOM,
                  padx=PADX,
                  pady=PADY,
                  anchor=CENTER
                )
        self.imgAtras = ttk.PhotoImage(name='Rewind', file=PATH / 'hacia-atras.png')
        self.imgAtras = self.imgAtras.subsample(16)
        self.imgPlay = ttk.PhotoImage(name='Play', file=PATH / 'video.png')
        self.imgPlay = self.imgPlay.subsample(16)
        self.imgPause = ttk.PhotoImage(name='Pause', file=PATH / 'pausa.png')
        self.imgPause = self.imgPause.subsample(16)
        self.imgAdelante = ttk.PhotoImage(name='Adelante', file=PATH / 'adelante.png')
        self.imgAdelante = self.imgAdelante.subsample(16)
        
        
        self.btnAtras = ttk.Button(master=self,
                                   image = self.imgAtras,
                                   compound=CENTER,
                                   bootstyle=DEFAULT_THEME
                                   )
        self.btnAtras.pack(fill=BOTH,side=LEFT,ipadx=PADX,ipady=PADY)
        
        self.btnPlay = ttk.Button(master=self,
                                   image = self.imgPlay,
                                   compound=CENTER,
                                   bootstyle=DEFAULT_THEME
                                   )
        self.btnPlay.pack(fill=BOTH,side=LEFT,ipadx=PADX,ipady=PADY)
        
        self.btnPause = ttk.Button(master=self,
                                   image = self.imgPause,
                                   compound=CENTER,
                                   bootstyle=DEFAULT_THEME
                                   )
        self.btnPause.pack(fill=BOTH,side=LEFT,ipadx=PADX,ipady=PADY)
        
        self.btnAdelante = ttk.Button(master=self,
                                   image = self.imgAdelante,
                                   compound=CENTER,
                                   bootstyle=DEFAULT_THEME
                                   )
        self.btnAdelante.pack(fill=BOTH,side=LEFT,ipadx=PADX,ipady=PADY)
            
class options(ttk.Frame):
    # creates the ribbon section 
    btnOptions :ttk.Button
    btnTools   :ttk.Button
    btnMethod  :ttk.Button
     
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack(fill=BOTH,
                  side=LEFT,
                  padx=PADX,
                  pady=PADY,
                  ipadx=PADX,
                  ipady=PADY
                )
   
        self.imgOptions = ttk.PhotoImage(name='options', file=PATH / 'icons8_settings_64px.png')    
        self.imgTools   = ttk.PhotoImage(name='tools', file=PATH / 'icons8_wrench_64px.png')
        self.imgMethod  = ttk.PhotoImage(name='method', file=PATH /'icons8_registry_editor_64px.png')
        
        self.btnOptions = ttk.Button(master=self,
                                    image=self.imgOptions,
                                    text=self.imgOptions.name,
                                    compound=TOP,
                                    bootstyle=INFO
                                    )
        self.btnOptions.pack(fill=BOTH,side=TOP,ipadx=PADX,ipady=PADY)
        
        self.btnTools = ttk.Button(master=self,
                                    image=self.imgTools,
                                    text=self.imgTools.name,
                                    compound=TOP,
                                    bootstyle=INFO
                                    )
        self.btnTools.pack(fill=BOTH,side=TOP,ipadx=PADX,ipady=PADY)
        
        self.Method = ttk.Button(master=self,
                                    image=self.imgMethod,
                                    text=self.imgMethod.name,
                                    compound=TOP,
                                    bootstyle=INFO
                                    )
        self.Method.pack(fill=BOTH,side=TOP,ipadx=PADX,ipady=PADY)
                    
class process(ttk.Frame):     
    controlsVideo : VideoControls
    videoPlayer   : VideoPlayer
    videoMeter    : VideoMeter
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack(fill=BOTH,
                  side=LEFT,
                  padx=PADX,
                  pady=PADY,
                  expand=YES
                )
        
        # Lockin Processing, it depends of method selected
        notebook = ttk.Notebook(self)
        notebook.pack(fill=BOTH,expand=YES,padx=PADX,pady=PADY)
        
        # creation and configuration of the tab of fouriers's method
        tabFourier = ttk.Frame(notebook, padding=PADGRAL,bootstyle = kwargs['bootstyle'])
        notebook.add(tabFourier, text='Fourier')
        
        # creation and configuration of the tab of four point's method  
        tabFourPoints = ttk.Frame(notebook, padding=PADGRAL,bootstyle = kwargs['bootstyle'])
        notebook.add(tabFourPoints, text='Four Points')
        
        # creation and configuration of the tab of geometrical's method
        tabGeometrical = ttk.Frame(notebook, padding=PADGRAL,bootstyle = kwargs['bootstyle'])
        notebook.add(tabGeometrical, text='Geometrical')

        # creation and configuration of the tab for play source of video        
        self.tabPlayer = ttk.Frame(notebook, padding=PADGRAL,bootstyle = kwargs['bootstyle'])
        notebook.add(self.tabPlayer, text='Play Source')
        
        self.videoMeter    = VideoMeter(master = self.tabPlayer,relief= kwargs['relief'],bootstyle =DEFAULT_THEME)
        self.controlsVideo = VideoControls(master = self.tabPlayer,relief=kwargs['relief'],bootstyle=DEFAULT_THEME)
        self.videoPlayer   = VideoPlayer(master = self.tabPlayer,relief=kwargs['relief'],bootstyle=DEFAULT_THEME)
        
        notebook.bind('<<NotebookTabChanged>>', self.on_tabSelected)
        
        
        # Configures the scroll bar that its inserted in tabProcess
        # wtScrollbar = ttk.Scrollbar(tabProcess)
        # wtScrollbar.pack(side=RIGHT, fill=Y)
        # wtScrollbar.set(0, 1)
        
        # wtCanvas = ttk.Canvas(
        #     master=tabProcess,
        #     relief=FLAT,
        #     borderwidth=0,
        #     selectborderwidth=0,
        #     highlightthickness=0,
        #     yscrollcommand=wtScrollbar.set
        # )
        # wtCanvas.pack(side=LEFT, fill=BOTH)
        # wtCanvas.create_window((0, 0), window=scroll_frame, anchor=NW)
        
        
    def create_player_buttons(self): 
        """Create buttonbox with media controls"""
        container = ttk.Frame(self.tabPlayer)
        container.pack(side=BOTTOM,fill=BOTH)
                
        










    # Event handler method for the NotebookTabChanged event
    def on_tabSelected(self, event):
        selected_index = event.widget.index('current')
        selected_tab = event.widget.tab(selected_index, 'text')
        # This code shows text into status bar 
        self.master.master.footer.setvar('Status',f'Se seleccionó la pestaña: {selected_tab}')
        
        

class info(ttk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack(fill=BOTH,
                  side=RIGHT,
                  padx=PADX,
                  pady=PADY
                )

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
    
class main_header(ttk.Frame):
    
    imgLogo : ttk.PhotoImage
    txtLogo : ttk.Label
    txtHeader:ttk.Label
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.imgLogo = ttk.PhotoImage(name='logo', file=PATH / 'icons8_broom_64px_1.png')
        self.pack(fill=BOTH,
                  side=TOP,
                  padx=PADX,
                  pady=PADY
                )
            
        frmLogo = ttk.Frame(master=self,
                            padding=kwargs['padding'],
                            bootstyle=DEFAULT_THEME,
                            relief=SOLID,
                            )
        
        frmLogo.grid(row=0,column=0,ipadx=PADX,ipady=PADY,sticky=NSEW)
        
        self.txtLogo=ttk.Label(master=frmLogo,image=self.imgLogo, bootstyle=(INVERSE, SECONDARY))
        self.txtLogo.image = self.imgLogo
        self.txtLogo.pack(fill=BOTH,expand=YES)                         
        
        frmCenter = ttk.Frame(master=self,
                            padding=kwargs['padding'],
                            bootstyle=DEFAULT_THEME,
                            relief=SOLID,
                            )
        frmCenter.grid(row=0,column=1,ipadx=PADX,ipady=PADY,sticky=NSEW)
        
        self.txtHeader=ttk.Label(master=frmCenter,
                            text='Developed by PhD. Eduardo Vargas Bernardino.....\nsistema de prueba...............\n es una prueba',
                            font=('TkDefaultFixed', 12),
                            padding=kwargs['padding'],
                            bootstyle=(INVERSE, SECONDARY),
                            justify=CENTER,
                            anchor=CENTER
                            )
        self.txtHeader.pack(fill=BOTH,expand=YES)
        self.columnconfigure(1, weight=1)
     
class main_body(ttk.Frame):
    Options: options
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack(fill=BOTH,
                  expand=YES,
                  padx=PADX,
                  pady=PADY
                )
        
        self.Options = options(master = self, relief=kwargs['relief'],bootstyle=LIGHT)
        self.Process = process(master=self,relief=kwargs['relief'],bootstyle=LIGHT)
        self.Info=info(master=self,relief=kwargs['relief'],bootstyle=INFO,width=100)
        self.rowconfigure(1,weight=1)
        
class main_footer(ttk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack(fill=BOTH,padx=PADX,pady=PADY,side=BOTTOM)
       
        frmStatus = ttk.Frame(master=self,
                            relief=kwargs['relief'],
                            height=kwargs['height']-(PADY*2)
                            )
        frmStatus.grid(row=0,column=0,sticky=NSEW)
        
        frmProgress = ttk.Frame(master=self,
                            height=kwargs['height']-(PADY*2),
                            relief=kwargs['relief']
                            )
        frmProgress.grid(row=0,column=1,sticky=NSEW)
        
        StatusBar = ttk.Label(
                    master = frmStatus,
                    textvariable='Status',
                    font=('Helvetica', 10, 'italic'),
                    bootstyle=INFO,
                    ) 
        StatusBar.pack(fill=BOTH,padx=PADX,pady=PADY)#,ipadx=PADX,ipady=PADY)
                
        ProgressBar = ttk.Progressbar(
            master=frmProgress,
            mode=DETERMINATE,
            orient=HORIZONTAL,
            variable='progress'
            )
        ProgressBar.place(relx=0.02,rely=0.5,relwidth=0.95,anchor=W)
        
        ttk.Label(frmProgress, text='%').pack(side=RIGHT,padx=PADX)
        ttk.Label(frmProgress, textvariable='progress').pack(side=RIGHT)

        self.columnconfigure(1, weight=1)
        
class main_frame(ttk.Frame):
    """
        This Class allow to create and manipuling the principal frame of the application
        its a Frame herencied 
    Args:
        ttk.Frame args: 
    """
    
    header  :main_header
    body    :main_body
    footer  :main_footer
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.header = main_header(master=self,                         # Initialize the program's header
                            relief= kwargs['relief'],
                            padding= kwargs['padding'],
                            bootstyle=ttk.SECONDARY
                            )
        
        self.body = main_body(master=self,                          # Initialize the program's body
                            relief= kwargs['relief'],
                            padding= kwargs['padding'],
                            bootstyle=SECONDARY
                            )
        
        self.footer = main_footer(master=self,                        # Initialize the program's footer
                            height = 30,
                            relief= kwargs['relief'],
                            padding= kwargs['padding']
                            )
        
        self.pack(fill=BOTH,expand=YES)      