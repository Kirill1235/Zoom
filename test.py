import pyautogui as pg
from PIL import Image
import time

UnMuted = Image.open('/home/kirill/zoom_solution/icon_photos/UnMuted.png')


login_bar = Image.open('/home/kirill/zoom_solution/icon_photos/login_bar.png')


Zoom_enetrence = Image.open('/home/kirill/zoom_solution/icon_photos/zoom_enterence.png')

Muted = Image.open('/home/kirill/zoom_solution/icon_photos/Muted.png')

Enterence_with_sound = Image.open('/home/kirill/zoom_solution/icon_photos/Enterence_with_sound.png')

Turn_on_Sound = Image.open('/home/kirill/zoom_solution/icon_photos/Turn_On_Sound.png')

Kate = Image.open('/home/kirill/zoom_solution/icon_photos/Kate.png')

Ente_password= Image.open('/home/kirill/zoom_solution/icon_photos/enter_the_password.png')

Password_enternce = Image.open('/home/kirill/zoom_solution/icon_photos/acession_enterence.png')

Zoom = Image.open('/home/kirill/zoom_solution/icon_photos/Zoom.png')

Zoom = Image.open('/home/kirill/zoom_solution/icon_photos/Zoom.png')


window = Image.open('/home/kirill/zoom_solution/icon_photos/pop-up-window.png')


Zoom_aloted = Image.open('/home/kirill/zoom_solution/icon_photos/Zoom_alloted.png')




t = pg.locateOnScreen(Enterence_with_sound, grayscale=True)
while(t is None):
    t = pg.locateOnScreen(Enterence_with_sound, grayscale=True)
pg.click(t[0], t[1])
pg.click(t[0], t[1])


t = pg.locateOnScreen(Turn_on_Sound, grayscale=True, confidence = .5)
while (t is None):
    t = pg.locateOnScreen(Turn_on_Sound, grayscale=True, confidence = .5)
pg.click(t[0], t[1])




