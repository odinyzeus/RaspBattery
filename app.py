#import Thermography as tg
import guiApp as gui
from pathlib import Path

#Defines the private properties for program exclusive use 
_Program_Name = "Digital Lock-In Amplifier for Thermography Analisis"
_Program_Theme = "superhero"

if __name__ == "__main__":
    app = gui.ttk.Window(_Program_Name, _Program_Theme)
    gui.Application(app)
    app.mainloop()