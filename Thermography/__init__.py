# Modulo principal del software de lockin amplifier para el laboratorio de Tecnocas fototermicas
import cv2
import os



_max_devices    = 10            # Maximum devices to scan by the app
Video_Device:any
Video:str
Directory:str
VideoFile:str

def _get_device_number():
    for i in range(_max_devices):  
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            cap.release()
            return i
    return None

def Split_Path_and_File(ruta):
    # get the path an file's name of video
    Directory = os.path.dirname(ruta)
    VideoFile = os.path.basename(ruta)

# Set a global variable for the device pointer
_device_id = _get_device_number()
if _device_id is not None:
    Video_Device = cv2.VideoCapture(_device_id)
else:
    Video_Device = None
