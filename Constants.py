"""
In this file its define the constants and parameters of Digital Lock-In-Amplifier Application
"""
from pathlib import Path
from ttkbootstrap.constants import *

PATH                = Path(__file__).parent / 'assets'
 
PRG_NAME            = 'Digital Graphic Lock-In Amplifier'
PRG_THEME           = 'superhero'
PRG_HDR_TEXT        = 'Developed by PhD. Eduardo Vargas Bernardino.....\nsistema de prueba...............\n es una prueba'
FRM_BORDER          = SOLID
PRG_FONT            = 'Helvetica'
PRG_FONT_SIZE       = 10
PRG_FONT_PROP       = 'italic'
txt_Status_Default  = 'Initializing system please wait............'
txtTabProcess       = 'Method'
txtTabFourier       = 'Fourier'
txtFourPoints       = 'Four Points'
txtGeometrical      = 'Geometrical'
frm_txt_Process     = 'Process related'
txtTabPlayer        = 'Play Source'
optionsMethod        = ['Geometrical', 'Fourier', 'Four Points','Another']
PADX                = 3
PADY                = 3
PADGRAL             = 3                 # Represents the general padding value 
FRAME_BORDER_WIDTH  = 1                 # Represents the width of frame's border