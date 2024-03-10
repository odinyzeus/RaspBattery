import ttkbootstrap as ttk
from Constants import *

# Footer
def footer_create(self:ttk.Frame):
    ftr_frame = ttk.Frame(self, height=15, border=2,relief='raised',padding=PADDING, bootstyle=DEFAULT_THEME)
    ftr_frame.pack(fill=X)
    
    # Create a status bar
    self._status_bar = ttk.Label(
        master=ftr_frame,
        text="Listo",
        font=(DEFAULT_THEME,12),
        bootstyle=LIGHT
    )
    self._status_bar.pack(fill=BOTH,expand=TRUE)