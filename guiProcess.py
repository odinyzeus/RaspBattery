import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Constants import *
from guiFooter import main_footer as mf

class Experiment(ttk.LabelFrame):
    __listener      = []                    # Se inicializa el controlador de receptores de eventos
    __footer        : mf
    __modulation    = 0.0
    _var_mod = None

    @property
    def Footer(self) -> mf:
        return self.__footer
    
    @Footer.setter
    def Footer(self , value:mf):
        self.__footer = value
    
    @property
    def Modulation(self)-> float:
        return self.__modulation
    
    @Modulation.setter
    def Modulation(self, value:float):
        self.__modulation = value
        for watcher in self.__listener:
            watcher.Modulation_Changed(self.Modulation)

    def register(self, listener):               # Mètodo que registra a los receptores de eventos de esta clase
        self.__listener.append(listener)
    
    def unregister(self, listener):             # Mètodo que elimina el registro de los receptores de eventos
        self.__listener.remove(listener)
 
    def create_modulation_row(self):
        """Add experiment's modulation row to Tab Process data experiment frame"""     
        modulation_row = ttk.Frame(self)
        modulation_row.pack(fill=X, expand=YES,anchor=CENTER)
        
        modulation_lbl = ttk.Label(modulation_row, text="Modulation:")
        modulation_lbl.grid(row=0,column=0,sticky=EW)

        modulation_ent = ttk.Entry(modulation_row, textvariable=self._var_mod,width=10)
        modulation_ent.grid(row=0,column=1,sticky=EW)
        
        modulation_hz_lbl = ttk.Label(modulation_row, text="Hz:",width=5)
        modulation_hz_lbl.grid(row=0,column=2,sticky=EW)

    def setModulation(self, *args):
        try:
            self.Modulation =  float(self._var_mod.get())
        except ValueError:
            # Maneja el caso en que el valor no sea un número válido
            self.Modulation = 0.0

    def __init__(self, **kwargs):
        self.footer = kwargs['footer']
        if 'footer' in kwargs:
            del kwargs['footer']
        super().__init__(**kwargs)
        self.grid(row=0,column=0,sticky=NSEW)
        # Declaración de la variable de instancia
        self._var_mod = ttk.StringVar()
        self._var_mod.trace_add("write", self.setModulation)
        self.create_modulation_row()