import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Constants import *

class main_header(ttk.Frame):
    
    imgLogo : ttk.PhotoImage
    txtLogo : ttk.Label
    txtHeader:ttk.Label
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.imgLogo = ttk.PhotoImage(name='logo', file=PATH / 'icons8_broom_64px_1.png')
        self.grid(row=0,column=0,ipadx=PADX,ipady=PADY,sticky=NSEW)
            
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
                            text= PRG_HDR_TEXT,
                            font=('TkDefaultFixed', 12),
                            padding=kwargs['padding'],
                            bootstyle=(INVERSE, SECONDARY),
                            justify=CENTER,
                            anchor=CENTER
                            )
        self.txtHeader.pack(fill=BOTH,expand=YES)
        self.columnconfigure(1, weight=1)
     
