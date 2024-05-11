import ttkbootstrap as ttk
from pathlib import Path
from .__init__ import PRGMAIN , PRGTHEME , Fourier_Frame

class Fourier:
    __container         : Fourier_Frame
       
    __currentFrame      = int                   # Represents the current frame in the range of frames to be process
    __porcentage        = int                   # Represents the progress's porcentage of the process compute   
    __Reset             = bool                  # Indicates that the process should be reset on the next video file read operation  
    __imgPath           : Path

    @property
    def imgPath(self)->Path:
        return self.__imgPath
    
    @imgPath.setter
    def imgPath(self, value:Path):
        self.__imgPath = value
        self.__container.imgPath = value

    #Defines the properties to set and recover the ttk.Frame container for Fourier Method
    @property
    def Container(self)->Fourier_Frame:
        return self.__container
    
    @Container.setter
    def Container(self, value: Fourier_Frame):
        self.__container = value

    # Creates the Fourier's class constructor
    def __init__(self, **kwargs) -> None:
        self.__container = Fourier_Frame(**kwargs)
    


if __name__ == "__main__":
    __app = ttk.Window(PRGMAIN, PRGTHEME)         # Creates the principal window for application
    fourier = Fourier(master = __app)
    # frm = main_frame(master = __app)
    # __app.config(menu=main_menu(master=__app))      # Defines that principal menu in principal application
    __app.minsize(width=800, height=600)            # Sets the minimum size of GUI   
    __app.mainloop()                                # event's loop
