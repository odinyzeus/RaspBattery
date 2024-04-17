import ttkbootstrap as ttk
import cv2
from ttkbootstrap.constants import *
from Constants import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import guiPlayer


class Event:
    def __init__(self):
        self._observers = []

    def register(self, observer):
        self._observers.append(observer)

    def unregister(self, observer):
        self._observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer(*args, **kwargs)

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

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config(relief=FRM_BORDER)
        self.config(padding=PADGRAL)
        self.config(bootstyle=ttk.SECONDARY)
        self.grid(row=0,column=0,columnspan=3,sticky=NSEW)
        self.columnconfigure(1,weight=1)

        self.frmLogo = ttk.Frame(master = self)
        self.frmCenter = ttk.Frame(master = self)
        self.imgLogo = ttk.PhotoImage(name='logo', file=PATH / 'icons8_broom_64px_1.png')
        self.txtLogo = ttk.Label(master=self.frmLogo,image=self.imgLogo, bootstyle=(INVERSE, SECONDARY))
        self.txtHeader = ttk.Label(master=self.frmCenter) 
        
        self.frmLogo.config(relief=FRM_BORDER)
        self.frmLogo.config(bootstyle=DEFAULT_THEME)
        self.frmLogo.config(padding= self.cget('padding'))
        self.frmLogo.grid(row=0,column=0,sticky=NSEW)
        
        self.txtLogo.image = self.imgLogo
        self.txtLogo.pack(fill=BOTH,expand=YES)

        self.frmCenter.config(relief=FRM_BORDER)
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
    
    __status    : ttk.Variable
    __progress  : ttk.Variable

    __lblStatus : ttk.Label
    
    @property
    def lblStatus(self)->ttk.Label:
        return self.__lblStatus
    
    @lblStatus.setter
    def lblStatus(self,value):
        self.__lblStatus = value

    def update_status(self, status):
        self.__status.set(status)

    def update_progress(self,progress):
        self.__progress.set(progress)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config(relief=FRM_BORDER)
        self.config(padding=PADGRAL)
        self.config(bootstyle=ttk.SECONDARY)
        self.grid(row=3,column=0,sticky=NSEW,columnspan=3)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0,weight=1)
        
        frmStatus      = ttk.Frame(master = self)
        frmProgress    = ttk.Frame(master= self)
        
        progressBar    = ttk.Progressbar(master=frmProgress)
        
        self.__lblStatus    = ttk.Label(master = frmStatus)
        self.__status       = ttk.StringVar(master = frmStatus, name = 'status', value = 'This is the initial message' )
        self.__progress     = ttk.Variable(master = frmProgress, name = 'progress', value = 10)


        frmStatus.config(relief=FRM_BORDER)
        # frmStatus.config(bootstyle=ttk.SECONDARY)
        frmStatus.grid(row=0,column=0,sticky=NSEW)

        frmProgress.config(relief=FRM_BORDER)
        frmProgress.grid(row=0,column=1,sticky=NSEW)

        ttk.Label(master=frmProgress,font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP), text='%').pack(side=RIGHT,padx=PADX)
        ttk.Label(master=frmProgress,font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP), textvariable='progress').pack(side=RIGHT,padx=PADX)

        self.__lblStatus.config(text= txt_Status_Default)
        self.__lblStatus.config(font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP))
        self.__lblStatus.config(padding= self.cget('padding'))
        self.__lblStatus.config(bootstyle=INFO)
        self.__lblStatus.config(textvariable=self.__status)
        self.__lblStatus.pack(fill=BOTH,expand=YES)

        progressBar.config(mode=DETERMINATE)
        progressBar.config(orient=HORIZONTAL)
        progressBar.config(variable=self.__progress)
        progressBar.place(relx=0.02,rely=0.5,relwidth=0.92,anchor=W)

        # settings of control's variables
        self.update_status(txt_Status_Default)
        self.update_progress(35)

class Body_Options(ttk.Frame):
    # creates the ribbon section 
    btnOptions :ttk.Button
    btnTools   :ttk.Button
    btnMethod  :ttk.Button

    def putButtons(self):
        self.btnOptions = ttk.Button(master=self,
                                    image=self.imgOptions,
                                    text=self.imgOptions.name,
                                    compound=TOP,
                                    bootstyle=INFO
                                    )
        self.btnTools = ttk.Button(master=self,
                                    image=self.imgTools,
                                    text=self.imgTools.name,
                                    compound=TOP,
                                    bootstyle=INFO
                                    )
        self.Method = ttk.Button(master=self,
                                    image=self.imgMethod,
                                    text=self.imgMethod.name,
                                    compound=TOP,
                                    bootstyle=INFO
                                    )
        
        self.btnOptions.grid(row=0,column=0,sticky=EW)
        self.btnTools.grid(row=1,column=0,sticky=EW)
        self.Method.grid(row=2,column=0,sticky=EW) 
     
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid(row=1,column=0,sticky=NS, rowspan=2)
        self.columnconfigure(0,weight=1)
        self.rowconfigure(3,weight=1)  
        self.config(relief=ttk.SOLID)
        self.config(padding=3)
        self.config(bootstyle=ttk.INFO)

        self.imgOptions = ttk.PhotoImage(name='options', file=PATH / 'icons8_settings_64px.png')    
        self.imgTools   = ttk.PhotoImage(name='tools', file=PATH / 'icons8_wrench_64px.png')
        self.imgMethod  = ttk.PhotoImage(name='method', file=PATH /'icons8_registry_editor_64px.png')
        self.putButtons()

class body_Info(ttk.Labelframe):

    frmexperiment   : ttk.Labelframe  # Creates the  experiment's information frame, it contains all info related to experiment
    frmVideo        : ttk.Labelframe 
    varModulation   : ttk.Variable    # Creates the  control's variable for modulation frecuency
    varFrames       : ttk.Variable
    varPeriod       : ttk.Variable
    varSizeX        : ttk.Variable
    varSizeY        : ttk.Variable
    varPeriodEx     : ttk.Variable

    _frames         : int             # Creates the frames per second of video source
    _period         : float           # Contains the period of frames per second value
    _milisecond     : int
    _modulation     : float           # Creates the modulation's frequency variable, it used for Lock-In operation
    _status         = 'Info area is creating'
    _size           = dict()
    _status_event   = Event()         # Creates the event of status controller
    _modulation_event= Event()      # Creates the modulation's frequency event controller
    _frames_event   = Event()         # Creates the frames per second of sources video event controller

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self,value:str):
        self._status = value
        self._status_event.notify(self._status) # Raises the status's info changed event

    @property
    def FramesperSecond(self)->int:
        return self._frames
    
    @FramesperSecond.setter
    def FramesperSecond(self, value:int):
        self._frames = value
        self._frames_event.notify(self._frames) #Raises the frecuency of frames of sources video 

    @property
    def Period(self)->float:
        return self._period

    @property
    def Size(self)->dict:
        return self._size
    
    @Size.setter
    def Size(self, args: dict):
        self._size = args
        self.varSizeX.set(args['X'])  
        self.varSizeY.set(args['Y'])
        
    @property
    def Modulation(self)->float:
        return self._modulation    
    
    @Modulation.setter
    def Modulation(self, value:float):
        self._modulation = value
        self._modulation_event.notify(self._modulation) #Raises the modulation frecuency value changed event
    
    def modulation_changed(self, *args):
        try:
            self._modulation = float(self.varModulation.get())
            _periodex = (1 / self._modulation) if self._modulation != 0 else 0
            self.varPeriodEx.set(round(_periodex, 4))
        except ValueError:
            self._modulation = 0.0
        
        self._modulation_event.notify(self._modulation) #Raises the modulation frecuency value changed event
        self._status_event.notify(f'The new value of modulation is : {self._modulation}')

    def frames_changed(self, *args):
        try:
            self.FramesperSecond = int(self.varFrames.get())
            self._period = (1 / self.FramesperSecond) if self.FramesperSecond != 0 else 0
            self.varPeriod.set(round(self._period, 4))

        except ValueError:
            self._frames = 9

    # This Function creates the info's template
    def push_widgets(self):
        # It creates the video's information fields inside
        self.frmVideo = ttk.LabelFrame(master = self, 
                                        text='Video:',
                                        relief=ttk.SOLID,
                                        padding=3,
                                        bootstyle=ttk.INFO
                                        )
        self.frmVideo.grid(row=0,column=0,sticky=EW)
        # self.frmVideo.pack(side=TOP,expand=YES,fill=X)

        # It create's the experiment information's frame 
        self.frmexperiment = ttk.LabelFrame(master = self, 
                                        text='Experiment:',
                                        relief=ttk.SOLID,
                                        padding=3,
                                        bootstyle=ttk.INFO
                                        )
        self.frmexperiment.grid(row=2,column=0,sticky=EW)
        # self.frmexperiment.pack(side=TOP,expand=YES,fill=X)

        # It Creates the video source information
        frmVideoData = ttk.Frame(master=self.frmVideo,padding=3)
        frmVideoData.pack(side=TOP,fill=X,expand=YES)
        frmVideoData.columnconfigure(0,weight=1)
        lblFrames = ttk.Label(master=frmVideoData,
                                  text='Frequency:',
                                  font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                                  )
        lblFrames.grid(row=0, column=0,sticky=EW)
        self.varFrames = ttk.Variable(master = frmVideoData, name = 'varFPS', value = '30' )
        inFrames = ttk.Entry(frmVideoData, 
                                 textvariable=self.varFrames,
                                 width=8,
                                 justify=CENTER,
                                 font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                                 )
        inFrames.grid(row=0,column=1,sticky=EW)

        lblFPS = ttk.Label(master=frmVideoData,text='FPS')
        lblFPS.grid(row=0,column=2,sticky=EW)


        frmVideoFrames = ttk.Frame(master=self.frmVideo,padding=3)
        frmVideoFrames.pack(side=TOP,fill=X,expand=YES)
        frmVideoFrames.columnconfigure(0,weight=1)

        lblNumFrames = ttk.Label(master=frmVideoFrames,
                                  text='Frames:',
                                  font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                                  )
        lblNumFrames.grid(row=0,column=0,sticky=EW)

        self.varNumFrames = ttk.Variable(master = frmVideoFrames, name = 'varNumFrames', value = '30' )
        inNumFrames = ttk.Entry(frmVideoFrames, 
                                 textvariable=self.varNumFrames,
                                 width=8,
                                 justify=CENTER,
                                 font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP),
                                 state='readonly'
                                 )
        inNumFrames.grid(row=0,column=1,sticky=EW)


        frmVideoPeriod = ttk.Frame(master=self.frmVideo,padding=3)
        frmVideoPeriod.pack(side=TOP,fill=X,expand=YES)
        frmVideoPeriod.columnconfigure(0,weight=1)

        lblPeriod = ttk.Label(master=frmVideoPeriod,
                                  text='Period:',
                                  font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                                  )
        lblPeriod.grid(row=0,column=0,sticky=EW)
        self.varPeriod = ttk.Variable(master = frmVideoPeriod, name = 'varPeriod', value = '30' )
        inPeriod = ttk.Entry(frmVideoPeriod, 
                                 textvariable=self.varPeriod,
                                 width=8,
                                 justify=CENTER,
                                 font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP),
                                 state='readonly'
                                 )
        inPeriod.grid(row=0,column=1,sticky=EW)
        lblPeriodTime = ttk.Label(master=frmVideoPeriod,
                                  text='s',
                                  font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                                  )
        lblPeriodTime.grid(row=0,column=2,sticky=EW)

        # It Creates the video source information
        frmVideoSize = ttk.Frame(master=self.frmVideo,padding=3)
        frmVideoSize.pack(side=TOP,fill=X,expand=YES)
        frmVideoSize.columnconfigure(0,weight=1)

        lblSize = ttk.Label(master=frmVideoSize,
                                  text='Size:',
                                  font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                                  )
        lblSize.grid(row=0,column=0,sticky=EW)

        lblSizeX = ttk.Label(master=frmVideoSize,
                                  text='X:',
                                  font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                                  )
        lblSizeX.grid(row=0,column=1)
        self.varSizeX = ttk.Variable(master = frmVideoSize, name = 'varSizeX', value = '30' )
        inSizeX = ttk.Entry(frmVideoSize, 
                                 textvariable=self.varSizeX,
                                 width=4,
                                 justify=CENTER,
                                 font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP),
                                 state='readonly'
                                 )
        inSizeX.grid(row=0,column=2)
        lblSizeY = ttk.Label(master=frmVideoSize,
                                  text='Y:',
                                  font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                                  )
        lblSizeY.grid(row=0,column=3)
        self.varSizeY = ttk.Variable(master = frmVideoSize, name = 'varSizeY', value = '30' )
        inSizeY = ttk.Entry(frmVideoSize, 
                                 textvariable=self.varSizeY,
                                 width=4,
                                 justify=CENTER,
                                 font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP),
                                 state='readonly'
                                 )
        inSizeY.grid(row=0,column=4,sticky=EW)



        # It create the information's fields inside  
        frmModulation = ttk.Frame(master=self.frmexperiment,padding=3)
        frmModulation.pack(side=TOP,fill=X,expand=YES)

        lblModulation = ttk.Label(master=frmModulation,
                                  text='Modulation:',
                                  font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                                  )
        lblModulation.pack(side=LEFT,padx=PADX)

        self.varModulation = ttk.Variable(master = frmModulation, name = 'varModulation', value = '0.0' )
        inModulation = ttk.Entry(frmModulation, 
                                 textvariable=self.varModulation,
                                 width=8,
                                 justify=CENTER,
                                 font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                                 )
        inModulation.pack(side=LEFT,padx=PADX,expand=YES,fill=X)

        lblHz = ttk.Label(master=frmModulation,text='Hz')
        lblHz.pack(padx=PADX)

        frmVideoPeriodEx = ttk.Frame(master=self.frmexperiment,padding=3)
        frmVideoPeriodEx.pack(side=TOP,fill=X,expand=YES)
        frmVideoPeriodEx.columnconfigure(0,weight=1)

        lblPeriodEx = ttk.Label(master=frmVideoPeriodEx,
                                  text='Period:',
                                  font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                                  )
        lblPeriodEx.grid(row=0,column=0,sticky=EW)
        self.varPeriodEx = ttk.Variable(master = frmVideoPeriodEx, name = 'varPeriodex', value = '30' )
        inPeriodEx = ttk.Entry(frmVideoPeriodEx, 
                                 textvariable=self.varPeriodEx,
                                 width=8,
                                 justify=CENTER,
                                 font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP),
                                 state='readonly'
                                 )
        inPeriodEx.grid(row=0,column=1,sticky=EW)
        lblPeriodTimeEx = ttk.Label(master=frmVideoPeriodEx,
                                  text='s',
                                  font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                                  )
        lblPeriodTimeEx.grid(row=0,column=2,sticky=EW)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config(relief=ttk.SOLID)
        self.config(text='Information')
        self.config(padding=3)
        self.config(bootstyle=ttk.INFO)
        self.grid(row=2,column=1,sticky=NSEW)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1,weight=1)
        self.push_widgets()
        self.varModulation.trace_add("write", self.modulation_changed)
        self.varFrames.trace_add('write',self.frames_changed)

    def __str__(self) -> str:
        return self._status 
        
    # self.info = body_Info(master = self, footer = self.footer)
    # self.info.register(self.modulation_changed)
            
    # self.body_options = Body_Options(master = self)
    # self.Process = Body_Process(master=self,relief=kwargs['relief'],bootstyle=LIGHT)

class Body_Source(ttk.Labelframe):

    btnOpenFile     : ttk.Button            # Creates the Open file Button
    frmDevice       : ttk.Labelframe        # Creates the experiment's device select 
    varSource       : ttk.Variable          # Creates the control's variable for modulation frecuency
    
    _cvCapture       : cv2.VideoCapture      # Creates the opencv capture object
    _status         = 'The devices info area is creating'
    _status_event   = Event()         # Creates the event of status controller
    _opened_event   = Event()
    _opened         : bool                  # Indicate if the source video is opened

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self,value:str):
        self._status = value
        self._status_event.notify(self._status) # Raises the status's info changed event

    @property
    def Video(self)->cv2.VideoCapture:
        return self._cvCapture
    
    @Video.setter
    def Video(self,value:cv2.VideoCapture):
        self._cvCapture = value
    
    def isVideoOpen(self)->bool:
        return self._opened

    def open_video_file(self):
        # Esto abrirá el cuadro de diálogo para seleccionar el archivo
        video_file = askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mkv")]) 
        if video_file:
            self.varSource.set(video_file)
        else:
            self.status = 'The name file can not be empty'

        self._cvCapture = cv2.VideoCapture(video_file)

        if self._cvCapture.isOpened():
            self.status = 'Video File opened correctly'
            self._opened = True
            self._opened_event.notify(self._opened) # Raises the status's info changed event
        else:
            self.status = 'Video File can not be opened'
        # while(self._cvCapture.isOpened()):
        #     ret, frame = self._cvCapture.read()
        #     if ret:
        #         pass
                
        # #         cv2.imshow('Video', frame)
        # #         if cv2.waitKey(1) & 0xFF == ord('q'):
        # #             break
        #     else:
        #         break

    def push_widgets(self):
        # It create's the experiment information's frame 
        self.frmDevice = ttk.Label(master = self,
                                        relief=ttk.SOLID,
                                        padding=3,
                                        bootstyle=ttk.INFO
                                        )
        self.frmDevice.pack(side=TOP,expand=YES,fill=X)

        # It create the information's fields inside  
        frmSource = ttk.Frame(master=self.frmDevice,
                                       padding=3)
        frmSource.pack(side=TOP,fill=X,expand=YES)

        lblSource = ttk.Label(master=frmSource,
                                  text='Source:',
                                  font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                                  )
        lblSource.pack(side=LEFT,padx=PADX,anchor='center')

        self.varSource = ttk.Variable(master = frmSource, name = 'varSource', value = PATH )
        
        inSource = ttk.Entry(frmSource, 
                                 textvariable=self.varSource,
                                 width=50,
                                 justify=LEFT,
                                 font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                                 )
        inSource.pack(side=LEFT,padx=PADX,expand=YES,fill=X,anchor='center')

        self.btnOpenFile = ttk.Button(master=frmSource,
                                    image=self.imgOpenFile,
                                    command=self.open_video_file
                                    )
        self.btnOpenFile.pack(side=RIGHT,padx=PADX,anchor='center')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config(relief=ttk.SOLID)
        self.config(text='Source of video information')
        self.config(padding=3)
        self.config(bootstyle=ttk.INFO)
        self.grid(row=1,column=1,sticky=EW,columnspan=2)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0,weight=1)

        self.imgOpenFile = ttk.PhotoImage(name='OpenFile', file=PATH / 'OpenFile.png')
        
        self.push_widgets()

    def __str__(self) -> str:
        return self._status 

class Body_Process(ttk.Frame):
    
    _status         = 'The process area is creating'
    _status_event   = Event()         # Creates the event of status controller
    _notebook       : ttk.Notebook
    _video          : cv2.VideoCapture
    videoMeter      : guiPlayer.VideoMeter
    videoPlayer     : guiPlayer.VideoPlayer
    
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self,value:str):
        self._status = value
        self._status_event.notify(self._status) # Raises the status's info changed event

    @property
    def video(self)->cv2.VideoCapture:
        return self._video
    
    @video.setter
    def video(self, value:cv2.VideoCapture):
        self._video = value

    def onPositionChanged(self, value):
        self._status_event.notify(f'The position is {value}')

    def create_tabPlayer(self, player:ttk.Frame):
        # Creation and configuration of video's player into play's source tab
        player.columnconfigure(0,weight=1)
        player.rowconfigure(1,weight=1)
        self.videoMeter     = guiPlayer.VideoMeter(master = player)
        self.videoPlayer    = guiPlayer.VideoPlayer(master = player)
        self.videoControl   = guiPlayer.VideoControls(master = player)


    def create_tabs(self):
        # creation and configuration of the tab of fouriers's method
        tabPlayer = ttk.Frame(self._notebook, padding=PADGRAL,bootstyle = SUCCESS)
        self._notebook.add(tabPlayer, text=txtTabPlayer)
        self.create_tabPlayer(tabPlayer)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config(relief=ttk.SOLID)
        self.config(padding=3)
        self.config(bootstyle=ttk.INFO)
        self.grid(row=2,column=2,sticky=NSEW)

        # Lockin Processing, it depends of method selected
        self._notebook = ttk.Notebook(master=self,height=600)
        self._notebook.pack(expand=YES,fill=BOTH)
        self.create_tabs()
        self.videoMeter._status_event.register(self.onPositionChanged)
        # self.columnconfigure(1, weight=1)
        # self.rowconfigure(0,weight=1)

        # self.imgOpenFile = ttk.PhotoImage(name='OpenFile', file=PATH / 'icons8_settings_64px.png')
        # self.varSource.trace_add("write", self.source_changed)

    def __str__(self) -> str:
        return self._status 

class main_frame(ttk.Frame):
    """
        This Class allow to create and manipuling the principal frame of the application
        its a Frame herencied 
    Args:
        ttk.Frame args: 
    """
    _status = 'Program initializing.......'
    _status_event   = Event()
    _info_section   : body_Info
    _option_section : Body_Options
    _info_source    : Body_Source
    _process_section: Body_Process

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self,value:str):
        self._status = value
        self._status_event.notify(self._status) # Raises the status's info event
    
    def reproducir_video(self):
        if self._info_source.Video is not None:
            ret, frame = self._info_source.Video.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                im = Image.fromarray(frame)
                img = ImageTk.PhotoImage(image=im)

                # lblVideo.configure(image=img)
                # lblVideo.image = img
                # lblVideo.after(10, visualizar)
            else:
                # lblVideo.image = ""
                self._info_source.Video.set(cv2.CAP_PROP_POS_FRAMES,0)

    def onOpened(self, value):
        if value:
            self._info_section.varFrames.set(self._info_source.Video.get(cv2.CAP_PROP_FPS))
            self._process_section.video = self._info_source.Video
            numFrames = int(self._info_source.Video.get(cv2.CAP_PROP_FRAME_COUNT))
            self._info_section.varNumFrames.set(numFrames)
            self._process_section.videoMeter.scale.config(to=numFrames)
            # sets the x and y dimension of video source
            x = int(self._info_source.Video.get(cv2.CAP_PROP_FRAME_WIDTH))
            y = int(self._info_source.Video.get(cv2.CAP_PROP_FRAME_HEIGHT))
            self._info_section.Size = {'X':x, 'Y': y}
            self.reproducir_video()
            self._process_section.videoMeter.update_remain(guiPlayer.getDuration(self._info_source.Video))

    def onStatusChanged(self,status):
        self._status_event.notify(status) # Raises the status's info event

    def onModulationChanged(self,modulation):
        print(modulation)

    def onVideoFPSChanged(self, frames):
        self.status = f'FPS of source video: {frames}'

    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config(relief=FRM_BORDER)
        self.config(padding=PADGRAL)
        self.config(bootstyle=ttk.PRIMARY)
        self.columnconfigure(2,weight=1)
        self.rowconfigure(2,weight=1)
        self.pack(fill=BOTH,expand=YES)

        # This section configure the info's area
        self._info_section = body_Info(master = self)
        self._info_section._status_event.register(self.onStatusChanged)
        self._info_section._modulation_event.register(self.onModulationChanged)
        self._info_section._frames_event.register(self.onVideoFPSChanged)

        # This section configure the options (buttons) area
        self._option_section = Body_Options(master = self)

        # This section configure the devices of video's sources 
        self._info_source   = Body_Source(master = self)
        self._info_source._status_event.register(self.onStatusChanged)
        self._info_source._opened_event.register(self.onOpened)

        # This section configure the Experiment Process area
        self._process_section= Body_Process(master=self)
        self._process_section._status_event.register(self.onStatusChanged)

    def __str__(self) -> str:
        return self._status 



if __name__ == "__main__":
    __app = ttk.Window(PRG_NAME, PRG_THEME)         # Creates the principal window for application
    frm = main_frame(master=__app)
    __app.config(menu=main_menu(master=__app))      # Defines that principal menu in principal application
    __app.minsize(width=800, height=600)            # Sets the minimum size of GUI   
    __app.mainloop()                                # event's loop















# self.footer = kwargs.pop('footer',None)
# self.footer.setvar('Status',f'the new value is: {value}')













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