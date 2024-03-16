from tkinter import Misc
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Constants import *
import Header as hdr

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
    
    imgLogo : ttk.PhotoImage
    txtLogo : ttk.Label
    txtHeader:ttk.Label
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.imgLogo = ttk.PhotoImage(name='logo', file=PATH / 'icons8_broom_64px_1.png')
               
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
        
        self.txtLogo=ttk.Label(master=frmLogo,image=self.imgLogo, bootstyle=(INVERSE, SECONDARY))
        self.txtLogo.image = self.imgLogo
        self.txtLogo.pack(fill=BOTH,expand=YES)                         
        
        frmCenter = ttk.Frame(master=self,
                            padding=kwargs['padding'],
                            bootstyle=DEFAULT_THEME,
                            relief=SOLID,
                            height=kwargs['height'],
                            )
        frmCenter.grid(row=0,column=1,ipadx=PADX,ipady=PADY,sticky=NSEW)
        
        self.txtHeader=ttk.Label(master=frmCenter,
                            text='Developed by PhD. Eduardo Vargas Bernardino.....\nsistema de prueba...............\n es una prueba',
                            font=('TkDefaultFixed', 12),
                            padding=kwargs['padding'],
                            bootstyle=(INVERSE, SECONDARY),
                            justify=CENTER,
                            anchor=CENTER
                            )
        self.txtHeader.pack(fill=BOTH,expand=YES)
              
class main_body(ttk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack(fill=BOTH,
                  side=TOP,
                  expand=YES,
                  padx=PADX,
                  pady=PADY
                )
        
class main_footer(ttk.Frame):
    StatusBar  : ttk.Label
    ProgressBar: ttk.Progressbar
        
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack(fill=BOTH,padx=PADX,pady=PADY,side=BOTTOM)
       
        frmStatus = ttk.Frame(master=self,
                            relief=kwargs['relief'],
                            height=kwargs['height']-(PADY*2)
                            )
        frmStatus.grid(row=0,column=0,sticky=NSEW)
        
        frmProgress = ttk.Frame(master=self,
                            height=kwargs['height']-(PADY*2),
                            relief=kwargs['relief']
                            )
        frmProgress.grid(row=0,column=1,sticky=NSEW)
    
        self.StatusBar = ttk.Label(
                    master = frmStatus,
                    text='Program Status',
                    font=('bold',10),
                    bootstyle=INFO
                    ) 
        self.StatusBar.pack(fill=BOTH,padx=PADX,pady=PADY)#,ipadx=PADX,ipady=PADY)
        
        self.ProgressBar = ttk.Progressbar(
            master=frmProgress,
            mode=DETERMINATE,
            orient=HORIZONTAL,
            value=75,
            )
        self.ProgressBar.place(relx=0.02,rely=0.5,relwidth=0.95,anchor=W)
        
        self.columnconfigure(1, weight=1)
        # self.columnconfigure(0, weight=0)
        # self.rowconfigure(0,weight=1)
        
        
        
        
        
        
        
class main_frame(ttk.Frame):
    """
        This Class allow to create and manipuling the principal frame of the application
        its a Frame herencied 
    Args:
        ttk.Frame args: 
    """
    
    header  :main_header
    body    :main_body
    footer  :main_footer
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.header = main_header(master=self,                         # Initialize the program's header
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
        
        self.footer = main_footer(master=self,                        # Initialize the program's footer
                            height = 30,
                            relief= kwargs['relief'],
                            padding= kwargs['padding']
                            )
        
        self.pack(fill=BOTH,expand=YES)
  
class Application(ttk.Window):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)                   
        
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
       