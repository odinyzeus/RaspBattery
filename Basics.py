from tkinter import Misc
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Constants import *
import Header as hdr

class options(ttk.Frame):
    # creates the ribbon section 
    btnOptions :ttk.Button
    btnTools   :ttk.Button
    btnMethod  :ttk.Button
     
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack(fill=BOTH,
                  side=LEFT,
                  padx=PADX,
                  pady=PADY,
                  ipadx=PADX,
                  ipady=PADY
                )
   
        self.imgOptions = ttk.PhotoImage(name='options', file=PATH / 'icons8_settings_64px.png')    
        self.imgTools   = ttk.PhotoImage(name='tools', file=PATH / 'icons8_wrench_64px.png')
        self.imgMethod  = ttk.PhotoImage(name='method', file=PATH /'icons8_registry_editor_64px.png')
        
        self.btnOptions = ttk.Button(master=self,
                                    image=self.imgOptions,
                                    text='options',
                                    compound=TOP,
                                    bootstyle=INFO
                                    )
        self.btnOptions.pack(fill=BOTH,side=TOP,ipadx=PADX,ipady=PADY)
        
        self.btnTools = ttk.Button(master=self,
                                    image=self.imgTools,
                                    text='Tools',
                                    compound=TOP,
                                    bootstyle=INFO
                                    )
        self.btnTools.pack(fill=BOTH,side=TOP,ipadx=PADX,ipady=PADY)
        
        self.Method = ttk.Button(master=self,
                                    image=self.imgMethod,
                                    text='Method',
                                    compound=TOP,
                                    bootstyle=INFO
                                    )
        self.Method.pack(fill=BOTH,side=TOP,ipadx=PADX,ipady=PADY)
                    
class process(ttk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack(fill=BOTH,
                  side=LEFT,
                  padx=PADX,
                  pady=PADY,
                  expand=YES
                )

class info(ttk.Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack(fill=BOTH,
                  side=RIGHT,
                  padx=PADX,
                  pady=PADY
                )

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
        self.pack(fill=BOTH,
                  side=TOP,
                  padx=PADX,
                  pady=PADY
                )
            
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
                            text='Developed by PhD. Eduardo Vargas Bernardino.....\nsistema de prueba...............\n es una prueba',
                            font=('TkDefaultFixed', 12),
                            padding=kwargs['padding'],
                            bootstyle=(INVERSE, SECONDARY),
                            justify=CENTER,
                            anchor=CENTER
                            )
        self.txtHeader.pack(fill=BOTH,expand=YES)
        self.columnconfigure(1, weight=1)
     
class main_body(ttk.Frame):
    Options: options
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pack(fill=BOTH,
                  expand=YES,
                  padx=PADX,
                  pady=PADY
                )
        
        self.Options = options(master = self, relief=kwargs['relief'],bootstyle=LIGHT)
        self.Process = process(master=self,relief=kwargs['relief'],bootstyle=SUCCESS)
        self.Info=info(master=self,relief=kwargs['relief'],bootstyle=INFO,width=100)
        self.rowconfigure(1,weight=1)
        
class main_footer(ttk.Frame):
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
        
        StatusBar = ttk.Label(
                    master = frmStatus,
                    textvariable='Status',
                    font=('bold',10),
                    bootstyle=INFO,
                    ) 
        StatusBar.pack(fill=BOTH,padx=PADX,pady=PADY)#,ipadx=PADX,ipady=PADY)
                
        ProgressBar = ttk.Progressbar(
            master=frmProgress,
            mode=DETERMINATE,
            orient=HORIZONTAL,
            variable='progress'
            )
        ProgressBar.place(relx=0.02,rely=0.5,relwidth=0.95,anchor=W)
        
        ttk.Label(frmProgress, text='%').pack(side=RIGHT,padx=PADX)
        ttk.Label(frmProgress, textvariable='progress').pack(side=RIGHT)

        self.columnconfigure(1, weight=1)
        
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
                            relief= kwargs['relief'],
                            padding= kwargs['padding'],
                            bootstyle=ttk.SECONDARY
                            )
        
        self.body = main_body(master=self,                          # Initialize the program's body
                            relief= kwargs['relief'],
                            padding= kwargs['padding'],
                            bootstyle=SECONDARY
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
            name='registry',
            file=PATH  / 'icons8_registry_editor_64px.png'),
            ttk.PhotoImage(
            name='tools',
            file=PATH  / 'icons8_wrench_64px.png'),
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
       