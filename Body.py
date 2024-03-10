import ttkbootstrap as ttk
from Constants import *

# header
def body_create(self:ttk.Frame):
    bdy_frame = ttk.Frame(self, border=2,relief='raised',padding=PADDING, bootstyle=DEFAULT_THEME)
    bdy_frame.pack(fill=BOTH, expand=True)
    
    body_left_frame = ttk.Frame(
        bdy_frame, 
        bootstyle = DEFAULT_THEME,
        borderwidth=FRAME_BORDER_WIDTH,
        relief=RAISED,
        width=250
    )
    body_left_frame.pack(fill=BOTH,side=LEFT,padx=PADDING)
        
    # self._body_right_frame = ttk.Frame(
    #     self._body_frame, 
    #     padding=self.Frame_Padding, 
    #     bootstyle = SECONDARY,
    #     borderwidth=1,
    #     relief=SOLID,
    #     width=250
    # )
    # self._body_right_frame.pack(fill=BOTH,side=RIGHT, padx=5)
        
    # self._body_center_frame = ttk.Frame(
    #     self._body_frame,
    #     padding=self.Frame_Padding,
    #     bootstyle = SECONDARY,
    #     borderwidth=1,
    #     relief=SOLID
    # )
    # self._body_center_frame.pack(fill=BOTH,side=LEFT,padx=5,expand=TRUE)
    # self._create_ribbon_left()  