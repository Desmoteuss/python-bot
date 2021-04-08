import numpy as np 
from PIL import ImageGrab
import cv2

while(True)
printscreen_pil = ImageGrab.grab (bbox=(0,40,800,640))
printscreen_numpy= np.array(printscreen_pil.getdata(), dtype='uint8')\
.reshape ((printscreen.pill))