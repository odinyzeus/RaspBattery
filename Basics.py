from tkinter import Misc
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Constants import *
import Header as hdr


"""images = [                                     # Creates the  list of icons to use into the programm
        ttk.PhotoImage(
            name='logo',
            file=PATH / 'icons8_broom_64px_1.png'),
        ttk.PhotoImage(
            name='cleaner',
            file=PATH / 'icons8_broom_64px.png'),
        ttk.PhotoImage(
            name='registry',
            file=PATH / 'icons8_registry_editor_64px.png'),
        ttk.PhotoImage(
            name='tools',
            file=PATH / 'icons8_wrench_64px.png'),
        ttk.PhotoImage(
            name='options',
            file=PATH / 'icons8_settings_64px.png'),
        ttk.PhotoImage(
            name='privacy',
            file=PATH / 'icons8_spy_80px.png'),
        ttk.PhotoImage(
            name='junk',
            file=PATH / 'icons8_trash_can_80px.png'),
        ttk.PhotoImage(
            name='protect',
            file=PATH / 'icons8_protect_40px.png')
        ]
 """           

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

        imgLogo = ttk.PhotoImage(name='logo', file=PATH / 'icons8_broom_64px_1.png')
        
        self.columnconfigure(1, weight=1)
        self.pack(fill=BOTH,
                  side=TOP,
                  padx=PADX,
                  pady=PADY
                )
            
        frmLogo = ttk.Frame(master=self,
                            padding=kwargs['padding'],
                            bootstyle=DEFAULT_THEME,
                            relief=SOLID,
                            height=kwargs['height'],
                            width=120
                            )
        
        frmLogo.grid(row=0,column=0,ipadx=PADX,ipady=PADY,sticky=NSEW)
        
        txtLogo=ttk.Label(master=frmLogo,image=imgLogo, bootstyle=(INVERSE, SECONDARY))
        txtLogo.image = imgLogo
        txtLogo.pack(fill=BOTH,expand=YES)                         
        
        frmCenter = ttk.Frame(master=self,
                            padding=kwargs['padding'],
                            bootstyle=DEFAULT_THEME,
                            relief=SOLID,
                            height=kwargs['height'],
                            )
        frmCenter.grid(row=0,column=1,ipadx=PADX,ipady=PADY,sticky=NSEW)
        
        txtHeader=ttk.Label(master=frmCenter,
                            text='Developed by PhD. Eduardo Vargas Bernardino.....\nsistema de prueba...............\n es una prueba',
                            font=('TkDefaultFixed', 12),
                            padding=kwargs['padding'],
                            bootstyle=(INVERSE, SECONDARY),
                            justify=CENTER,
                            anchor=CENTER
                            )
        txtHeader.pack(fill=BOTH,expand=YES)
        
        
class main_body(ttk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack(fill=BOTH,
                  side=TOP,
                  expand=YES,
                  padx=PADGRAL,
                  pady=PADGRAL
                )
        
class main_footer(ttk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack(fill=X,
                  side=BOTTOM,
                  padx=5,
                  pady=5
                )    
        
class main_frame(ttk.Frame):
    """
        This Class allow to create and manipuling the principal frame of the application
        its a Frame herencied 
    Args:
        ttk.Frame args: 
    """
    header : ttk.Frame
    body:ttk.Frame
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.hdr = main_header(master=self,                         # Initialize the program's header
                            height=100,
                            relief= kwargs['relief'],
                            padding= kwargs['padding'],
                            bootstyle=ttk.SECONDARY
                            )
        
        self.body = main_body(master=self,                          # Initialize the program's body
                            relief= kwargs['relief'],
                            padding= kwargs['padding'],
                            bootstyle=kwargs['bootstyle']
                            )
        
        self.body = main_footer(master=self,                        # Initialize the program's footer
                            height = 20,
                            relief= kwargs['relief'],
                            padding= kwargs['padding'],
                            bootstyle=ttk.INFO
                            )
        
        self.pack(fill=BOTH,expand=YES)
  
class Application(ttk.Window):
    
    window: ttk.Frame
    
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)                   
        
        hdr.init_header(self.window)
        
        # application images
        self.window.images = [
            ttk.PhotoImage(
            name='logo',
            file=PATH / 'icons8_broom_64px_1.png'),
            ttk.PhotoImage(
            name='cleaner',
            file=PATH  / 'icons8_broom_64px.png'),
            ttk.PhotoImage(
            name='registry',
            file=PATH  / 'icons8_registry_editor_64px.png'),
            ttk.PhotoImage(
            name='tools',
            file=PATH  / 'icons8_wrench_64px.png'),
            ttk.PhotoImage(
            name='options',
            file=PATH  / 'icons8_settings_64px.png'),
            ttk.PhotoImage(
            name='privacy',
            file=PATH  / 'icons8_spy_80px.png'),
            ttk.PhotoImage(
            name='junk',
            file=PATH  / 'icons8_trash_can_80px.png'),
            ttk.PhotoImage(
            name='protect',
            file=PATH  / 'icons8_protect_40px.png')
        ]

    
    
        