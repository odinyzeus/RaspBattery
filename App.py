import guiApp as gui

from Constants import *

import ttkbootstrap as ttk

__app = ttk.Window(PRG_NAME, PRG_THEME) # Creates the principal window for application

frmPrincipal = gui.main_frame(master  = __app)          # Creates the main frame contains all widgets of application
frmHeader    = gui.main_header(master = frmPrincipal)   # Creates the main header's frame that contains all header's widgets
frmFooter    = gui.main_footer(master = frmPrincipal)   # Creates the main footer's frame that contains the status and progress bar

"""
Contains all sections and widgets that compose the body's program
the principal process is showned and processed into this section
this frame is composed by:

info: this section show all information of experiment and device about, the info section configuration is inside frmbody class 
"""
# frmBody         = mb(master = frmPrincipal,footer = frmFooter)

def onStatusChanged(status):
    frmFooter.update_status(status)
    
if __name__ == "__main__":
    __app.config(menu=gui.main_menu(master = __app))       # Defines that principal menu in principal application
    __app.minsize(width=800, height=600)        # Sets the minimum size of GUI    
    __app.maxsize(width=1200, height=1024)      # Sets the maximum size of main window

    frmPrincipal._status_event.register(onStatusChanged)

    __app.mainloop()                            # event's loop