from guiApp import main_frame as mf
from guiApp import main_menu as mm
from Constants import *

import ttkbootstrap as ttk

__app = ttk.Window(PRG_NAME, PRG_THEME) # Creates the principal window for application
mnu   = mm(master = __app)              # Creates the principal menu for application

frmPrincipal = mf(                      # Creates the main frame contains all widgets of application
    master = __app,
    relief=ttk.SOLID,
    padding= 3,
    bootstyle = ttk.PRIMARY
    )

if __name__ == "__main__":                                   
    __app.config(menu=mnu)                                  # Defines that principal menu in principal application
    __app.minsize(width=800, height=600)                    # Sets the minimum size of GUI    
    __app.maxsize(width=1200, height=1024)                   # Sets the maximum size of main window
             
    __app.mainloop()                                        # event's loop