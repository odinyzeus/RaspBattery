from .utilities import Event
import ttkbootstrap as ttk
import math, cv2
from ttkbootstrap.constants import *
from PIL import Image, ImageTk
from pathlib import Path

PATH                = Path(__file__).parent
PRGMAIN             = 'Fourier Method'
PRGTHEME            = 'cosmo'
FRM_BORDER          = SOLID
PADGRAL             = 3
COLSPAN             = 3
FRM_BORDER          = SOLID
PRG_FONT            = 'Helvetica'
PRG_FONT_SIZE       = 10
PRG_FONT_PROP       = 'italic'

def prepare_image(image: str)->ImageTk.PhotoImage:
        """Create frame to contain media"""
        __img_path = PATH / image
        __original = Image.open(__img_path)
        ancho_objetivo = 320
        proporcion = ancho_objetivo / __original.width
        altura_objetivo = int(__original.height * proporcion)
        __final = __original.resize((ancho_objetivo, altura_objetivo), Image.LANCZOS)
        return ImageTk.PhotoImage(__final)    

class video_frame(ttk.LabelFrame):
    """
        This Class creates the frame for all video's information
    Args:
        ttk.Frame args: 
    """
    __status            = 'Method of Fourier for Digital Image Lock-In-Amplifier processing...'
    __status_event      = Event()               # Creates the event's controller for show the status related to Fourier's Method process
    modulation_event    = Event()
    __grid_value        = {'row':0, 'column':0, 'sticky':EW}
    __varFrame_Rate     : ttk.IntVar            # Represents the frame Rate of the video that will be used by lock-in method    (fs)
    __varPeriod         : ttk.DoubleVar         # Represents the period related to frame Rate of the video that will be used by lock-in method

    @property
    def Frame_Rate(self)->int:
        return self.__varFrame_Rate.get()

    @Frame_Rate.setter
    def Frame_Rate(self,value:int):
        self.__varFrame_Rate.set(value)

    @property
    def Period(self)->float:
        return self.__varPeriod.get()

    @Period.setter
    def Period(self, value:float):
        self.__varPeriod.set(value)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self,value:str):
        self.__status = value
        self.__status_event.notify(self.__status) # Raises the status's info changed event

    @property
    def gridValue(self)->dict:
        return self.__grid_value
    
    @gridValue.setter
    def gridValue(self, value:dict):
        self.__grid_value = value
        self.grid(row=value['row'],column=value['column'],sticky=value['sticky'])

    def create_template(self):
        # It Creates the video source information applied to process
        frmVideo    = ttk.Frame(master=self, padding=PADGRAL)
        frmVideo.pack(side=TOP,fill=X,expand=YES)
        frmVideo.columnconfigure(0,weight=1)

        # Creates the Frames Rate row fields
        lblFrame = ttk.Label(master=frmVideo,
                             text='Frame Rate:',
                                  font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                                  )
        lblFrame.grid(row=0, column=0,sticky=EW)

        inFrames = ttk.Entry(master=frmVideo, 
                             textvariable=self.__varFrame_Rate,
                             width=8,
                             justify=CENTER,
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        inFrames.grid(row=0,column=1,sticky=EW)

        lblUnits = ttk.Label(master=frmVideo,
                             text='FPS',
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        lblUnits.grid(row=0, column=2,sticky=EW)

        # Creates the row fields of Period related to frame rate 
        lblPeriod = ttk.Label(master=frmVideo,
                             text='Period:',
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        lblPeriod.grid(row=1, column=0,sticky=EW)
        
        inPeriod = ttk.Entry(master=frmVideo, 
                             textvariable=self.__varPeriod,
                             width=8,
                             justify=CENTER,
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP),
                             state=READONLY
                             )
        inPeriod.grid(row=1,column=1,sticky=EW)

        lblSeconds = ttk.Label(master=frmVideo,
                             text='s',
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        lblSeconds.grid(row=1, column=2,sticky=EW)

    def frameChanged(self,*args):
        try:
            self.__varPeriod.set(1 / self.__varFrame_Rate.get())

        except ValueError:
            self.__varPeriod.set(0)

    def periodChanged(self,*args):
        self.modulation_event.notify(self.Period)

    def __init__(self,**kargs):
        super().__init__(**kargs)
        self.config(relief=FRM_BORDER)
        self.config(padding=PADGRAL)
        self.config(bootstyle=ttk.SECONDARY)
        self.config(text='Video Source')
        self.grid(row=self.__grid_value['row'],column=self.__grid_value['column'],sticky=self.__grid_value['sticky'])

        self.__varFrame_Rate    = ttk.IntVar(master = self, name = 'varFPS', value = '24')
        self.__varPeriod        = ttk.DoubleVar(master = self, name = 'varPeriod', value = '0.01')
        
        self.create_template()
        
        self.__varFrame_Rate.trace_add('write', self.frameChanged)
        self.__varPeriod.trace_add('write', self.periodChanged)

class lockin_frame(ttk.LabelFrame):
    """
        This Class creates the frame for all Lock-In's information
    Args:
        ttk.Frame args: 
    """
    __status            = 'Method of Fourier for Digital Image Lock-In-Amplifier processing...'
    __status_event      = Event()               # Creates the event's controller for show the status related to Fourier's Method process 
    __grid_value        = {'row':1, 'column':0, 'sticky':EW}
    __varModulation     : ttk.DoubleVar         # Represents the modulation's frequency of the reference signal                 (fe)
    __varPeriodMod      : ttk.DoubleVar         # Represents the period related to frame Rate of the video that will be used by lock-in method
    __varFrames         : ttk.IntVar            # Represents the value of total frames will be process  
    __varInit_frame     : ttk.IntVar            # Represents the number of the initial's frame of the video that will be process
    __varFinal_frame    : ttk.IntVar            # Represents the number of the final's frame of the video that will be process
    __varFramesByPeriod : ttk.IntVar            # Represents the N's factor, it is knowed like frames by lock-in periods        (N)
    __varKFactor        : ttk.DoubleVar         # Represents the K's factor, defined by this Method like                        [N(fe/fs)+1]
    __W                 : complex               # Represents the W's Factor used in this Method
                                                # pow( W, (n - 1) * (K - 1))
    __frame_period      = 0.1                   # Represents the period of frame rate of video source
    __frame_rate        = 24                    # Represents the frame rate of video source                                     (fs)
    __Image_full        : bool                  # Indicates if the thermal image has 2 images or just has a full size one

    @property
    def ImgFull(self)->bool:
        return self.__Image_full
    
    @ImgFull.setter
    def ImgFull(self,value:bool):
        self.__Image_full = value

    @property
    def W_value(self)->complex:
        return self.__W
    
    @W_value.setter
    def W_value(self, value:complex):
        self.__W =value

    @property
    def SourcePeriod(self)->float:
        return self.__frame_period
    
    @SourcePeriod.setter
    def SourcePeriod(self, value:float):
        self.__frame_period = value
        self.__frame_rate = 1 / value
        self.modulationChanged()

    @property
    def KFactor(self)->float:
        return self.__varKFactor.get()
    
    @KFactor.setter
    def KFactor(self, value:float):
        self.__varKFactor.set(value)

    @property
    def FramesByPeriod(self)->int:
        return self.__varFramesByPeriod.get()

    @FramesByPeriod.setter
    def FramesByPeriod(self, value:int):
        self.__varFramesByPeriod.set(value)

    @property
    def FinalFrame(self)->int:
        return self.__varFinal_frame.get()
    
    @FinalFrame.setter
    def FinalFrame(self, value:int):
        self.__varFinal_frame.set(value)

    @property
    def InitFrame(self)->int:
        return self.__varInit_frame.get()

    @InitFrame.setter
    def InitFrame(self,value:int):
        self.__varInit_frame.set(value)

    @property
    def Frames(self)->int:
        return self.__varFrames.get()
    
    @Frames.setter
    def Frames(self,value:int):
        self.__varFrames.set(value)

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self,value:str):
        self.__status = value
        self.__status_event.notify(self.__status) # Raises the status's info changed event

    @property
    def gridValue(self)->dict:
        return self.__grid_value
    
    @gridValue.setter
    def gridValue(self, value:dict):
        self.__grid_value = value
        self.grid(row=value['row'],column=value['column'],sticky=value['sticky'])

    @property
    def Modulation(self)->float:
        return self.__varModulation.get()

    @Modulation.setter
    def Modulation(self, value:float):
        self.__varModulation.set(value)

    @property
    def Period(self)->float:
        return self.__varPeriodMod.get()
    
    @Period.setter
    def Period(self, value:float):
        self.__varPeriodMod.set(value)

    def create_template(self):
        # It Creates the video source information applied to process
        frmLockIn    = ttk.Frame(master=self, padding=PADGRAL)
        frmLockIn.pack(side=TOP,fill=X,expand=YES)
        frmLockIn.columnconfigure(0,weight=1)

        # Creates the Frames Rate row fields
        lblModulation = ttk.Label(master=frmLockIn,
                             text='Modulation:',
                                  font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                                  )
        lblModulation.grid(row=0, column=0,sticky=EW)

        inModulation = ttk.Entry(master=frmLockIn, 
                             textvariable=self.__varModulation,
                             width=8,
                             justify=CENTER,
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        inModulation.grid(row=0,column=1,sticky=EW)

        lblUnits = ttk.Label(master=frmLockIn,
                             text='Hz',
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        lblUnits.grid(row=0, column=2,sticky=EW)

        # Creates the row fields of Period related to frame rate 
        lblPeriod = ttk.Label(master=frmLockIn,
                             text='Period:',
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        lblPeriod.grid(row=1, column=0,sticky=EW)
        
        inPeriod = ttk.Entry(master=frmLockIn, 
                             textvariable=self.__varPeriodMod,
                             width=8,
                             justify=CENTER,
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP),
                             state=READONLY
                             )
        inPeriod.grid(row=1,column=1,sticky=EW)

        lblSeconds = ttk.Label(master=frmLockIn,
                             text='s',
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        lblSeconds.grid(row=1, column=2,sticky=EW)

        lblFrames = ttk.Label(master=frmLockIn,
                             text='Frames:',
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        lblFrames.grid(row=2, column=0,sticky=EW)

        inFrames = ttk.Entry(master=frmLockIn, 
                             textvariable=self.__varFrames,
                             width=12,
                             justify=CENTER,
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        inFrames.grid(row=2,column=1,sticky=EW)

        lblInitframe = ttk.Label(master=frmLockIn,
                             text='Init Frame:',
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        lblInitframe.grid(row=3, column=0,sticky=EW)

        inInitFrame = ttk.Entry(master=frmLockIn, 
                             textvariable=self.__varInit_frame,
                             width=12,
                             justify=CENTER,
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        inInitFrame.grid(row=3,column=1,sticky=EW)

        lblFinalframe = ttk.Label(master=frmLockIn,
                             text='Final Frame:',
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        lblFinalframe.grid(row=4, column=0,sticky=EW)

        inFinalFrame = ttk.Entry(master=frmLockIn, 
                             textvariable=self.__varFinal_frame,
                             width=12,
                             justify=CENTER,
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        inFinalFrame.grid(row=4,column=1,sticky=EW)

        lblFramesbyPeriod = ttk.Label(master=frmLockIn,
                             text='Frames by Period:',
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        lblFramesbyPeriod.grid(row=5, column=0,sticky=EW)

        inFramesbyPeriod = ttk.Entry(master=frmLockIn, 
                             textvariable=self.__varFramesByPeriod,
                             width=8,
                             justify=CENTER,
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        inFramesbyPeriod.grid(row=5,column=1,sticky=EW)

        lblKFactor = ttk.Label(master=frmLockIn,
                             text='K Factor:',
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        lblKFactor.grid(row=6, column=0,sticky=EW)

        inKFactor = ttk.Entry(master=frmLockIn, 
                             textvariable=self.__varKFactor,
                             width=8,
                             justify=CENTER,
                             font=(PRG_FONT, PRG_FONT_SIZE, PRG_FONT_PROP)
                             )
        inKFactor.grid(row=6,column=1,sticky=EW)

    def modulationChanged(self,*args):
        try:
            self.__varPeriodMod.set(1 / self.__varModulation.get())
            self.__varFramesByPeriod.set(round(self.__varPeriodMod.get() / self.__frame_period))

        except ValueError:
            self.__varPeriodMod.set(0)
            self.__varFramesByPeriod.set(-1)

    def framesChanged(self,*args):
        try:
            print(f'El numero total de frames es: {self.__varFrames.get()}')
        except:
            print('Error')

    def framesUpdate(self,*args):
        self.Frames = max(0, self.FinalFrame - self.InitFrame)

    def kFactorUpdate(self, *args):
        self.__varKFactor.set((self.__varFramesByPeriod.get() * self.Modulation / self.__frame_rate) + 1) 

    def __init__(self,**kargs):
        super().__init__(**kargs)
        self.config(relief=FRM_BORDER)
        self.config(padding=PADGRAL)
        self.config(bootstyle=ttk.SECONDARY)
        self.config(text='Lock-In-Amplifier')
        self.grid(row=self.__grid_value['row'],column=self.__grid_value['column'],sticky=self.__grid_value['sticky'])

        self.__Image_full       = False
        self.__varModulation    = ttk.DoubleVar(master = self, name = 'varModulation', value = '0.1')
        self.__varPeriodMod     = ttk.DoubleVar(master = self, name = 'varPeriodMod', value = '0.01')
        self.__varFrames        = ttk.IntVar(master=self, name='varNumFrames',value=1000)
        self.__varInit_frame    = ttk.IntVar(master=self, name='varInitFrame',value=0)
        self.__varFinal_frame   = ttk.IntVar(master=self, name='varFinalFrame',value=1000)
        self.__varFramesByPeriod= ttk.IntVar(master=self, name='varFramesByPeriod',value=10)
        self.__varKFactor       = ttk.DoubleVar(master = self, name = 'varKFactor', value = '0.01')

        self.create_template()

        self.__varModulation.trace_add('write', self.modulationChanged)
        self.__varFrames.trace_add('write',self.framesChanged)
        self.__varInit_frame.trace_add('write',self.framesUpdate)
        self.__varFinal_frame.trace_add('write',self.framesUpdate)
        self.__varFramesByPeriod.trace_add('write',self.kFactorUpdate)

class images_frame(ttk.LabelFrame):
    """
        This Class creates the frame for all Lock-In's information
    Args:
        ttk.Frame args: 
    """
    __status            = 'Method of Fourier for Digital Image Lock-In-Amplifier processing...'
    __status_event      = Event()               # Creates the event's controller for show the status related to Fourier's Method process 
    __grid_value        = {'row':0, 'column':1, 'sticky':NSEW}
    __last_image_Frame  : ImageTk.PhotoImage    # Represents the last image processed by by openCV
    __original_image    : ttk.Label
    __processed_image   : ttk.Label
    __phase_image       : ttk.Label
    __amplitude_image   : ttk.Label


    @property
    def imgOriginal(self)->ttk.Label:
        return self.__original_image
    
    @imgOriginal.setter
    def imgOriginal(self,value:ttk.Label):
        img = value.cget('image')
        self.__original_image.configure(image=img)
        self.__original_image.image = img

    @property
    def imgProcessed(self)->ttk.Label:
        return self.__processed_image
    
    @imgProcessed.setter
    def imgProcessed(self, value:ttk.Label):
        self.__processed_image = value

    @property
    def imgPhase(self)->ttk.Label:
        return self.__phase_image
    
    @imgPhase.setter
    def imgPhase(self, value:ttk.Label):
        self.__phase_image = value

    @property
    def imgAmplitude(self)->ttk.Label:
        return self.__amplitude_image
    
    @imgAmplitude.setter
    def imgAmplitude(self,value:ttk.Label):
        self.__amplitude_image = value

    def create_template(self):
        
        # It Creates the labelframe to original image capturated by opencv.read
        frmOriginal         = ttk.LabelFrame(master=self, padding=PADGRAL,text='Original')
        frmOriginal.grid(row=0,column=0,sticky=NSEW)

        frmToProcess        = ttk.LabelFrame(master=self, padding=PADGRAL,text='Processed')
        frmToProcess.grid(row=0,column=1,sticky=NSEW)

        frmPhase            = ttk.LabelFrame(master=self, padding=PADGRAL,text='Phase Result')
        frmPhase.grid(row=1,column=0,sticky=NSEW)
        
        frmAmplitude        = ttk.LabelFrame(master=self, padding=PADGRAL,text='Amplitude Result')
        frmAmplitude.grid(row=1,column=1,sticky=NSEW)

        # widget of Original Image configuration
        self.__original_image   = ttk.Label(master=frmOriginal)
        self.__original_image.pack(padx=PADGRAL,pady=PADGRAL, expand=YES, fill=BOTH)

        self.__processed_image  = ttk.Label(master=frmToProcess)
        self.__processed_image.pack(padx=PADGRAL,pady=PADGRAL, expand=YES, fill=BOTH)

        self.__phase_image  = ttk.Label(master=frmPhase)
        self.__phase_image.pack(padx=PADGRAL,pady=PADGRAL, expand=YES, fill=BOTH)

        self.__amplitude_image  = ttk.Label(master=frmAmplitude)
        self.__amplitude_image.pack(padx=PADGRAL,pady=PADGRAL, expand=YES, fill=BOTH)

    def __init__(self,**kargs):
        super().__init__(**kargs)
        self.config(relief=FRM_BORDER)
        self.config(padding=PADGRAL)
        self.config(bootstyle=ttk.SECONDARY)
        self.config(text='Images of process')
        self.grid(row=self.__grid_value['row'],column=self.__grid_value['column'],sticky=self.__grid_value['sticky'],rowspan=3)
        self.columnconfigure(1,weight=1)

        self.create_template()

class Fourier_Frame(ttk.Frame):
    """
        This Class allow to create and manipuling the principal frame of the method of processing
        its a Frame herencied 
    Args:
        ttk.Frame args: 
    """
    __status = 'Method of Fourier for Digital Image Lock-In-Amplifier processing...'
    __status_event      = Event()               # Creates the event's controller for show the status related to Fourier's Method process 
    __video_frame       : video_frame
    __Lockin_frame      : lockin_frame
    __images_frame      : images_frame
    
    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self,value:str):
        self.__status = value
        self.__status_event.notify(self.__status) # Raises the status's info changed event

    @property
    def LockinTemplate(self)->lockin_frame:
        return self.__Lockin_frame

    @LockinTemplate.setter
    def LockinTemplate(self, value:lockin_frame):
        self.__Lockin_frame = value

    @property
    def videoTemplate(self)->video_frame:
        return self.__video_frame
    
    @videoTemplate.setter
    def videoTemplate(self, value:video_frame):
        self.__video_frame = value

    @property
    def imagesTemplate(self)-> images_frame:
        return self.__images_frame
    
    @imagesTemplate.setter
    def imagesTemplate(self, value:images_frame):
        self.__images_frame =value

    def onVideoPeriodChanged(self, value):
        self.LockinTemplate.SourcePeriod = value

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.config(relief=FRM_BORDER)
        self.config(padding=PADGRAL)
        self.config(bootstyle=ttk.SECONDARY)
        self.pack(fill=BOTH,expand=YES)

        self.__video_frame  = video_frame(master = self)
        self.__Lockin_frame = lockin_frame(master = self)
        self.__images_frame = images_frame(master = self)
        self.__video_frame.modulation_event.register(self.onVideoPeriodChanged)
        self.columnconfigure(1,weight=1)
        self.rowconfigure(2,weight=1)
        
