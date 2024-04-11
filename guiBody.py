import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Constants import *
from guiPlayer import VideoControls as vc
from guiPlayer import VideoMeter    as vm
from guiPlayer import VideoPlayer   as vp
from guiProcess import Experiment   as de


class Body_Process(ttk.Frame): 
    footer          : mf    
    VideoControls   : vc
    videoMeter      : vm
    videoPlayer     : vp
    Experiment      : de
    notebook        : ttk.Notebook
    tabPlayer       : ttk.Frame
    tabProcess      : ttk.Frame

    # processData     : TabProcess
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.footer = kwargs['master'].footer
        self.grid(row=0,column=1,sticky=NSEW)
        # Lockin Processing, it depends of method selected
        self.notebook = ttk.Notebook(master=self,height=600)
        self.notebook.pack(expand=YES,padx=PADX,pady=PADY,fill=BOTH)

        self.create_tabs(**kwargs)
    
    def create_tabs(self,**kwargs):
        # creation and configuration of the tab of fouriers's method
        tabFourier = ttk.Frame(self.notebook, padding=PADGRAL,bootstyle = kwargs['bootstyle'])
        self.notebook.add(tabFourier, text=txtTabFourier)
        
        # creation and configuration of the tab of four point's method  
        tabFourPoints = ttk.Frame(self.notebook, padding=PADGRAL,bootstyle = kwargs['bootstyle'])
        self.notebook.add(tabFourPoints, text=txtFourPoints)
        
        # creation and configuration of the tab of geometrical's method
        tabGeometrical = ttk.Frame(self.notebook, padding=PADGRAL,bootstyle = kwargs['bootstyle'])
        self.notebook.add(tabGeometrical, text=txtGeometrical)

        # creation and configuration of the play's source of video        
        self.tabPlayer = ttk.Frame(self.notebook, padding=PADGRAL,bootstyle = kwargs['bootstyle'])
        self.notebook.add(self.tabPlayer, text=txtTabPlayer)
        
        # Creation and configuration of process's tab
        self.tabProcess = ttk.Frame(self.notebook,padding=PADGRAL,bootstyle = kwargs['bootstyle'])
        self.notebook.add(self.tabProcess, text = txtTabProcess)

        # event's controller section
        self.notebook.bind('<<NotebookTabChanged>>', self.on_tabSelected)   

        self.create_tab_player(**kwargs)
        self.create_tab_experiment(**kwargs)

    def create_tab_player(self,**kwargs):
        # Creation and configuration of video's player into play's source tab
        self.tabPlayer.columnconfigure(0,weight=1)
        self.tabPlayer.rowconfigure(1,weight=1)
        self.videoMeter    = vm(master = self.tabPlayer,relief= kwargs['relief'],bootstyle =DEFAULT_THEME)
        self.videoPlayer   = vp(master = self.tabPlayer,relief=kwargs['relief'],bootstyle=DEFAULT_THEME)
        self.VideoControls = vc(master = self.tabPlayer,relief=kwargs['relief'],bootstyle=DEFAULT_THEME)    
        
    def create_tab_experiment(self,**kwargs):
        # Creation and configuration of process's tab
        self.tabProcess.columnconfigure(1,weight=1)
        self.tabProcess.rowconfigure(1,weight=1)
        self.Experiment = de(footer=self.footer,master=self.tabProcess,relief=kwargs['relief'],bootstyle=PRIMARY,text=frm_txt_Process) 
        self.Experiment.register(self)

    # Event handler method for the NotebookTabChanged event
    def on_tabSelected(self, event):
        selected_index = event.widget.index('current')
        selected_tab = event.widget.tab(selected_index, 'text')
        # This code shows text into status bar 
        self.footer.setvar('prg_status',f'Se seleccionó la pestaña: {selected_tab}')


    def Modulation_Changed(self,event):
        self.footer.setvar('prg_status',f'Nuevo Valor de Modulacion: {event}')





      

