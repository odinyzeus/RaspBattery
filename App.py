from guiApp import main_frame as mf
from guiApp import main_menu as mm
from guiApp import main_header as mh
from guiApp import main_footer as ff
from guiApp import main_body as mb
from Constants import *

import ttkbootstrap as ttk

__app = ttk.Window(PRG_NAME, PRG_THEME) # Creates the principal window for application

frmPrincipal    = mf(master = __app)            # Creates the main frame contains all widgets of application
frmHeader       = mh(master = frmPrincipal)
frmFooter       = ff(master = frmPrincipal)
frmBody         = mb(master = frmPrincipal,footer = frmFooter)

if __name__ == "__main__":
    __app.config(menu=mm(master = __app))       # Defines that principal menu in principal application
    __app.minsize(width=800, height=600)        # Sets the minimum size of GUI    
    __app.maxsize(width=1200, height=1024)      # Sets the maximum size of main window
             
    __app.mainloop()                            # event's loop