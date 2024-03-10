import ttkbootstrap as ttk
from Constants import *

# header
def header_create(self:ttk.Frame):
    hdr_frame = ttk.Frame(self, height=150, border=FRAME_BORDER_WIDTH,relief='raised',padding=PADDING, bootstyle=DEFAULT_THEME)
    hdr_frame.pack(fill=BOTH)

    hdr_logo_left = ttk.Label(
            master=hdr_frame,
            image='logo',
            bootstyle=(INVERSE,PRIMARY),
            border=FRAME_BORDER_WIDTH,
            relief=RAISED
        )
    hdr_logo_left.grid(row=0, column=0, sticky=NSEW)

    hdr_tittle = ttk.Frame(
        master=hdr_frame,
        bootstyle=DEFAULT_THEME,
        padding=PADDING
    )
    hdr_tittle.grid(row=0, column=1, sticky=NSEW)

    hdr_logo_rigth = ttk.Label(
            master=hdr_frame,
            image='logo',
            bootstyle=(INVERSE,PRIMARY),
            border=FRAME_BORDER_WIDTH,
            relief=RAISED
        )
    hdr_logo_rigth.grid(row=0, column=2, sticky=NSEW)      

    # Configure the grid for widgets expand
    hdr_frame.grid_columnconfigure(0, weight=0)
    hdr_frame.grid_columnconfigure(1, weight=1)
    hdr_frame.grid_columnconfigure(2, weight=0)
    
    hdr_tittle.grid_columnconfigure(0,weight=1)

    tittle_text_one = ttk.Label(
        master=hdr_tittle,
        text='Digital Lock-In-Amplifier for Thermography Images Processing',
        font=('TkDefaultFixed', 15),
        bootstyle=(INVERSE, SECONDARY),
        justify=CENTER
    )
    tittle_text_one.grid(row=0,column=0,sticky=EW)
    tittle_text_one.grid_rowconfigure(0,weight=1)
    
    tittle_text_two = ttk.Label(
        master=hdr_tittle,
        text='Developed by PhD. Eduardo Vargas Bernardino',
        font=('TkDefaultFixed', 12),
        bootstyle=(INVERSE, SECONDARY),
        justify=CENTER
    )
    tittle_text_two.grid(row=1,column=0,sticky=EW)
    tittle_text_two.grid_rowconfigure(1,weight=1)
    
    tittle_text_three = ttk.Label(
        master=hdr_tittle,
        text='copyrigth',
        font=('TkDefaultFixed', 12),
        bootstyle=(INVERSE, SECONDARY),
        justify=CENTER
    )
    tittle_text_three.grid(row=2,column=0,sticky=EW)
    tittle_text_three.grid_rowconfigure(2,weight=1)
