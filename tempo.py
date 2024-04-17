import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from Constants import *

class Event:
    def __init__(self):
        self._observers = []

    def register(self, observer):
        self._observers.append(observer)

    def unregister(self, observer):
        self._observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer(*args, **kwargs)

if __name__ == "__main__":
    __app = ttk.Window(PRG_NAME, PRG_THEME)         # Creates the principal window for application


    frm = main_frame(master=__app)
    __app.config(menu=main_menu(master=__app))      # Defines that principal menu in principal application
    __app.minsize(width=800, height=600)            # Sets the minimum size of GUI   
    __app.mainloop()    