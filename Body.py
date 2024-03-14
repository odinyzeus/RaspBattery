import ttkbootstrap as ttk
from Constants import *


# header
def body_create(self:ttk.Frame):
    bdy_frame = ttk.Frame(self, border=2,relief='raised', bootstyle=DEFAULT_THEME)
    bdy_frame.pack(fill=BOTH, expand=True)
    
    # Contains all icons for configuration options
    body_upper_frame = ttk.Frame(
        master=bdy_frame, 
        bootstyle = DEFAULT_THEME,
        borderwidth=FRAME_BORDER_WIDTH,
        relief=RAISED,
        height=50
    )
    body_upper_frame.grid(row=0, column=0, columnspan=3, sticky=EW)

    #Contains all widgets related with the process    
    body_process_frame = ttk.Frame(
        master=bdy_frame,
        bootstyle = DEFAULT_THEME,
        borderwidth=FRAME_BORDER_WIDTH,
        relief=RAISED
    )
    body_process_frame.grid(row=1,column=0,columnspan=3,sticky=NSEW)    
    
    # Contains the progress bar that indicate the progress of every actions executed by th programm
    body_down_frame = ttk.Frame(
        master=bdy_frame, 
        bootstyle = DEFAULT_THEME,
        borderwidth=FRAME_BORDER_WIDTH,
        relief=RAISED,
        height=20
        )
    body_down_frame.grid(row=2, column=0, columnspan=3, sticky=EW)
    
    # Represents the progress bar for status processing
    progress_bar = ttk.Progressbar(
        master=body_down_frame, 
        orient=HORIZONTAL,
        mode=DETERMINATE, 
        style='primary.Horizontal.TProgressbar')
    progress_bar.pack(expand=TRUE, fill=BOTH, pady=2)

    
    # Configures the frames's bodíes grid for widgets expand
    bdy_frame.rowconfigure(0, weight=0)
    bdy_frame.rowconfigure(1, weight=1)
    bdy_frame.rowconfigure(2, weight=0)
    
    bdy_frame.columnconfigure(0,weight=1)
        
    # This section is designed for all process widgets
    
    # Contains the process's data that is in progress
    body_left_frame = ttk.Frame(
        master=body_process_frame, 
        bootstyle = DEFAULT_THEME,
        borderwidth=FRAME_BORDER_WIDTH,
        relief=RAISED,
        width=150
    )
    body_left_frame.grid(row=0, column=0, sticky=NS)
    

    # Contains the real time process is in progress.
    body_center_frame = ttk.Frame(
        master=body_process_frame, 
        bootstyle = DEFAULT_THEME,
        borderwidth=FRAME_BORDER_WIDTH,
        relief=RAISED
    )
    body_center_frame.grid(row=0, column=1, sticky=NSEW)    
    
    # contains the experimental data and options of the current process
    body_right_frame = ttk.Frame(
        master=body_process_frame,  
        bootstyle = DEFAULT_THEME,
        borderwidth=FRAME_BORDER_WIDTH,
        relief=RAISED,
        width=150
    )
    body_right_frame.grid(row=0,column=2,sticky=NS)
        
    # Configures the frames's bodíes grid for widgets expand
    body_process_frame.rowconfigure(0, weight=1)
    body_process_frame.columnconfigure(1, weight=1)