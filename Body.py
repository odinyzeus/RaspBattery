import ttkbootstrap as ttk
from Constants import *

# header
def body_create(self:ttk.Frame):
    bdy_frame = ttk.Frame(self, border=2,relief='raised',padding=PADDING, bootstyle=DEFAULT_THEME)
    bdy_frame.pack(fill=BOTH, expand=True)