import numpy as np 
from PIL import ImageGrab
import cv2
import numpy as np


while(True):
printscreen_PIL = ImageGrab.grab(bbox=(0, 40, 800, 640))
printscreen_numpy= np.array(printscreen_pil.getdata(), dtype='uint8')\
.reshape ((printscreen.pil.size[1],printscreen_pil.size[0],3))
cv.imshow('window',printscreen_numpy)
if cv2.waitKey(25) & 0xFF == ord('q'):
     break
    cv2.destroyAllWindows()
   