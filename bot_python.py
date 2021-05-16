# from core import * 

# frostArmor = 168
# fireBall = 133
# autoAttack = 6603

# class CombatRoutline:

#      def __init__(self):
#           pass

#      def needRest(self):
#           player = LocalPlayer()
#           desc = player.descriptor

#           healthPerecent = (desc.health / desc.maxhealth) = 100
#           powerPerecent = (desc.power / desc. maxPower) * 100

#           if healthPerecent < 50:
#                return True
#           if powerPerecent < 30:
#                return True

#           return False

#      def rest(self):
#           pass

#      def buffs(self):
#           if not LocalPlayer().hasAura(frostArmor):
#                CastSpell(frostArmor, LocalPlayer().guid)

#      def prepare(self, target):
#           if target.distance() > 20:
#                WalkTo(target.position)
#                return False
          
#           if LocalPlayer().isMoving():
#                StopMoving()   
#                return False

#           if not IsFacing(target.position):
#                LookTo(target.position)
#                return False
          
#           return True

#      def process(self, target):
#           if CanCast(fireBall) and LocalPlayer().descriptor.power > 30:
#                CastSpell(fireBall, target.guid)
#           elif not IsAutoAttacking():
#                Cast spell(autoAttack, target.guid)

# class GrindTask:

# hotspot = CreateVector(-699.25, -4325.50, 43.95)
# targets = ['Mottled Boar']

# state= 'default'
# curentTask = GrindTask(targets, hotspot)





























# import numpy as np 
# from PIL import ImageGrab
# import cv2
# import numpy as np


# while(True):
# printscreen_PIL = ImageGrab.grab(bbox=(0, 40, 800, 640))
# printscreen_numpy= np.array(printscreen_PIL.getdata(), dtype='uint8')\
# .reshape ((printscreen_PIL.size[1],printscreen_PIL.size[0],3))
# cv2.imshow('window',printscreen_numpy)
# if cv2.waitKey(25) & 0xFF == ord('q'):
#      break
# cv2.destroyAllWindows()
   





# *******************************************************************************

# from PIL import ImageGrab
# img = ImageGrab.grab()
# img.show()


# *******************************************************************************

# from PIL import Image

# image = Image.open('image.jpg')
# image.show()
# # img = Image.open('test_scr.jpg')
# display(img)

# import time
# def queue_alert(alertat=2, interval=6, occurences=3, alarm=True, emailalert = False, playsong = False):
#     counter = 0
#     while True:
#         # capture screenshot of the current queue
#         time.sleep(interval)
#         img = ImageGrab.grab()
#         img.show()
#         # extract the queue time
#         minutes = get_time_in_queue(img)
#         # alert when queue reaches threshold
#         if not minutes:
#             print('Could not extract queue')
#         else:
#             print(f'Current queue: {minutes}')
#             if minutes <= alertat:
#                 counter += 1
#                 if counter >= occurences:
#                     print('Your queue is about to pop!')
#                     send_alert(alarm=alarm, email=emailalert, playsong=playsong)
#                     emailalert = False
#         # stop after 15 alarms
#         if counter > 15:
#             break
          