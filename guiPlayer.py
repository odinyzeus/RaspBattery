import ttkbootstrap as ttk
import cv2
from ttkbootstrap.constants import *
from Constants import *
from PIL import Image, ImageTk

def getDuration(video:cv2.VideoCapture)->str:
    # Obtiene la cantidad total de frames
    frames = video.get(cv2.CAP_PROP_FRAME_COUNT)
    
    # Obtiene los frames por segundo
    fps = video.get(cv2.CAP_PROP_FPS)

    # Calcula la duración en segundos
    duration_seconds = frames / fps

    # Convierte la duración a minutos y segundos
    minutes = int(duration_seconds // 60)
    seconds = int(duration_seconds % 60)

    # Formatea la duración como una cadena 'mm:ss'
    duration_str = f'{minutes:02d}:{seconds:02d}'

    return duration_str

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

class VideoControls(ttk.Frame):
    btnAtras :ttk.Button
    btnPlay :ttk.Button
    btnPause: ttk.Button
    btnAdelante: ttk.Button
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid(row=2,column=0,sticky=NSEW)
        self.columnconfigure(0,weight=1)
        
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
        self.btnAtras.grid(column=1,row=0,sticky=EW,padx=PADX,pady=3)
        
        self.btnPlay = ttk.Button(master=self,
                                   image = self.imgPlay,
                                   compound=CENTER,
                                   bootstyle=DEFAULT_THEME
                                   )
        self.btnPlay.grid(column=2,row=0,sticky=EW,padx=PADX,pady=3)
        
        self.btnPause = ttk.Button(master=self,
                                   image = self.imgPause,
                                   compound=CENTER,
                                   bootstyle=DEFAULT_THEME
                                   )
        self.btnPause.grid(column=3,row=0,sticky=EW,padx=PADX,pady=3)
        
        self.btnAdelante = ttk.Button(master=self,
                                   image = self.imgAdelante,
                                   compound=CENTER,
                                   bootstyle=DEFAULT_THEME
                                   )
        self.btnAdelante.grid(column=4,row=0,sticky=EW,padx=PADX,pady=3)
        self.columnconfigure(5,weight=1)
        
class VideoMeter(ttk.Frame):

    remain_var : ttk.DoubleVar
    elapsed_var: ttk.DoubleVar
    _status_event   = Event()         # Creates the event of status controller
    

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self,value:str):
        self._status = int(value)
        self._status_event.notify(self._status) # Raises the status's info changed event

    def update_remain(self, value):
        self.remain_var.set(value)

    def update_position(self, value:int):
        self.scale.set(value)

    def push_widget(self):
        """Create frame with progress meter with lables"""
        container = ttk.Frame(master = self)
        container.pack(side=TOP,fill=X, expand=YES, pady=10)
             
        self.elapse = ttk.Label(container, text='00:00')
        self.elapse.pack(side=LEFT, padx=10)

        self.scale = ttk.Scale(
            master=container, 
            command=self.on_progress, 
            bootstyle=SECONDARY,
            from_=0,
            to=100
        )
        self.scale.pack(side=LEFT, fill=X, expand=YES)
        self.remain_var = ttk.DoubleVar(master=container,name='varRemain', value=190)
        self.remain = ttk.Label(container, text='03:10',textvariable = self.remain_var)
        self.remain.pack(side=LEFT, fill=X, padx=10)
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config(relief=FRM_BORDER)
        self.config(padding=PADGRAL)
        self.config(bootstyle=ttk.DEFAULT_THEME)
        self.grid(row=0,column=0,sticky=EW)
        self.push_widget()
        self.scale.set(50)
    
        
    def on_progress(self, val: float):
        """Update progress labels when the scale is updated."""
        # elapsed = self.elapsed_var.get()
        # remaining = self.remain_var.get()
        # total = int(elapsed + remaining)
        self.status = self.scale.get()

class VideoPlayer(ttk.Frame):

    media :ttk.Label
    _status_event   = Event()         # Creates the event of status controller
    _status         = 'Modulo de reproductor'

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value:str):
        self._status = int(value)
        self._status_event.notify(self._status) # Raises the status's info changed event

    def push_widget(self):
        """Create frame to contain media"""
        img_path = PATH / 'mp_background.png'
        img_original = Image.open(img_path)

        # Calcular la altura proporcional
        ancho_objetivo = 480
        proporcion = ancho_objetivo / img_original.width
        altura_objetivo = int(img_original.height * proporcion)
        
        # Redimensionar la imagen
        img_redimensionada = img_original.resize((ancho_objetivo, altura_objetivo), Image.ANTIALIAS)
        
        self.imgAtras = ImageTk.PhotoImage(img_redimensionada)

        # self.imgAtras = ttk.PhotoImage(name='Player', file=PATH / )
        self.media = ttk.Label(master=self, image=self.imgAtras)
        self.media.pack(padx=PADX,pady=PADY)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config(relief=FRM_BORDER)
        self.config(padding=PADGRAL)
        self.config(bootstyle=ttk.DEFAULT_THEME)
        self.grid(row=1,column=0,sticky=NSEW)
        self.push_widget()
        
        
 