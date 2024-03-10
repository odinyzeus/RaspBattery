from guiApp import *

if __name__ == "__main__":
    # Creates and configure the principal windows for the Digital Lock-In-Amplifier application
    app = ttk.Window(PRG_NAME, PRG_THEME)
    
    app.resizable(True,True)                                            # Indicates that application can be resizable
    app.minsize(width=800, height=600)                                  # Sets the minimum size of GUI
    app.maxsize(width=1200, height=600)                                 # Sets the maximum size of main window
    set_win2center(app)                                                 # Centers the main window into pc's screen
    set_menu(app)
    set_gui(app)
    
    # gui.Application(app)
    app.mainloop()