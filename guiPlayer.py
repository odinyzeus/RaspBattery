import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Constants import *

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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid(row=0,column=0,sticky=EW)
        
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

class VideoPlayer(ttk.Frame):
    media :ttk.Label
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.grid(row=1,column=0,sticky=NSEW)
        
        """Create frame to contain media"""
        self.imgAtras = ttk.PhotoImage(name='Player', file=PATH / 'mp_background.png')
        self.media = ttk.Label(master=self, image=self.imgAtras)
        self.media.pack(padx=PADX,pady=PADY)
 