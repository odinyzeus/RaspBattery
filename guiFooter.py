import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Constants import *

class main_footer(ttk.Frame):
    # application variables

    def create_row(self, **args):
        frmStatus = ttk.Frame(master=self,
                            relief=args['relief'],
                            height=args['height']-(PADY)
                            )
        frmStatus.grid(row=0,column=0,sticky=NSEW)

        frmProgress = ttk.Frame(master=self,
                            height=args['height']-(PADY),
                            relief=args['relief']
                            )
        frmProgress.grid(row=0,column=1,sticky=NSEW)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0,weight=1)

        self.lblStatus = ttk.Label(
                    master = frmStatus,
                    font=('Helvetica', 10, 'italic'),
                    bootstyle=INFO,
                    textvariable= 'prg_status'
                    ) 
        self.lblStatus.pack(fill=BOTH,padx=PADX,pady=PADY)

        self.progressBar = ttk.Progressbar(
            master=frmProgress,
            mode=DETERMINATE,
            orient=HORIZONTAL,
            variable='Progress'
            )
        self.progressBar.place(relx=0.02,rely=0.5,relwidth=0.92,anchor=W)
        ttk.Label(frmProgress,font=('Helvetica', 10, 'italic'), text='%').pack(side=RIGHT,padx=PADX)
        ttk.Label(frmProgress,font=('Helvetica', 10, 'italic'), textvariable='Progress').pack(side=RIGHT)


    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.grid(row=2,column=0,sticky=NSEW)
        self.create_row(**kwargs)
        self.setvar('prg_status',txt_Status_Default)
        self.setvar('Progress',25)

        
