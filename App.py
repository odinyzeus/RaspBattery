import Basics
import ttkbootstrap as ttk

__app = ttk.Window(Basics.PRG_NAME, Basics.PRG_THEME)       # Creates the principal window for application
mnu   = Basics.main_menu(master = __app)                        # Creates the principal menu for application

frmPrincipal = Basics.main_frame(                           # Creates the main frame contains all widgets of application
    master = __app,
    relief=ttk.SOLID,
    padding= 5,
    bootstyle = ttk.DEFAULT_THEME
    )

if __name__ == "__main__":                                   
    __app.config(menu=mnu)                                  # Defines that principal menu in principal application
    __app.minsize(width=800, height=600)                    # Sets the minimum size of GUI    
    __app.maxsize(width=1200, height=800)                   # Sets the maximum size of main window
    
    #frmPrincipal.header.txtHeader['text'] = 'Solo formato's                                      
    __app.mainloop()                                        # event's loop