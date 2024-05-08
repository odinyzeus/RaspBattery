import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Constants import *





class Experiment(ttk.LabelFrame):
    
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

    def __init__(self, **kwargs):
        self.footer = kwargs['footer']
        if 'footer' in kwargs:
            del kwargs['footer']
        super().__init__(**kwargs)
        self.grid(row=0,column=0,sticky=NSEW)
        # Declaración de la variable de instancia
        self._var_mod = ttk.StringVar()
        
        self.create_modulation_row()