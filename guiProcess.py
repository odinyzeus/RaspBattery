import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Constants import *
from guiFooter import main_footer as mf

class Experiment(ttk.LabelFrame):
    _footer  = mf
    _var_mod = None

    # Define la función que se ejecutará cuando el valor cambie
    def modulation_calculate(self,*args):
        self._footer.lblStatus.config(text=f'Nuevo valor: {float(self._var_mod.get())}' )
        pass
        
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

    def __init__(self, **kwargs):
        self._footer = kwargs['footer']
        if 'footer' in kwargs:
            del kwargs['footer']
        super().__init__(**kwargs)
        self.grid(row=0,column=0,sticky=NSEW)
        # Declaración de la variable de instancia
        self._var_mod = ttk.StringVar()
        self._var_mod.trace_add("write", self.modulation_calculate)
        self.create_modulation_row()