import pyautogui as pg
import os
from PIL import Image
from real_time import real_time
import sys
import time

UnMuted = Image.open('/home/kirill/zoom_solution/icon_photos/UnMuted.png')

login_bar = Image.open('/home/kirill/zoom_solution/icon_photos/login_bar.png')

Zoom_enetrence = Image.open('/home/kirill/zoom_solution/icon_photos/zoom_enterence.png')

Muted = Image.open('/home/kirill/zoom_solution/icon_photos/Muted.png')

Enterence_with_sound = Image.open('/home/kirill/zoom_solution/icon_photos/Enterence_with_sound.png')

Turn_on_Sound = Image.open('/home/kirill/zoom_solution/icon_photos/Turn_On_Sound.png')

Kate = Image.open('/home/kirill/zoom_solution/icon_photos/Kate.png')

Enter_password= Image.open('/home/kirill/zoom_solution/icon_photos/enter_the_password.png')

Password_enternce = Image.open('/home/kirill/zoom_solution/icon_photos/acession_enterence.png')

Zoom = Image.open('/home/kirill/zoom_solution/icon_photos/Zoom.png')

Zoom_aloted = Image.open('/home/kirill/zoom_solution/icon_photos/Zoom_alloted.png')

screen_zoom = Image.open('/home/kirill/zoom_solution/icon_photos/screen_zoom.png')

window = Image.open('/home/kirill/zoom_solution/icon_photos/pop-up-window.png')

Zoom_OK = Image.open('/home/kirill/zoom_solution/icon_photos/Zoom_OK.png')

Enter_password_2= Image.open('/home/kirill/zoom_solution/icon_photos/enter_password_2.png')

check_time = "9:30"





t = pg.locateOnScreen(Zoom, grayscale=True)
t1 = pg.locateOnScreen(Zoom_aloted, grayscale=True)
while( (t is None) and (t1 is None)):
    if real_time() > "13:00":
        sys.exit()
    t = pg.locateOnScreen(Zoom, grayscale=True)
    t1 = pg.locateOnScreen(Zoom_aloted, grayscale=True)
    pg.hotkey('winleft', 'd')
if t is None:
    template = t1
else:
    template = t
pg.click(template[0], template[1])
pg.click(template[0], template[1])


count = 0

while real_time() < "12:50":
    if pg.locateOnScreen(screen_zoom, grayscale=True) is None:
        if count != 0:
            t = pg.locateOnScreen(Zoom_OK, grayscale=True)
            while(t is None):
                t = pg.locateOnScreen(Zoom_OK, grayscale=True)
            pg.click(t[0], t[1])


        t = pg.locateOnScreen(Zoom_enetrence, grayscale=True)
        while(t is None):
            t = pg.locateOnScreen(Zoom_enetrence, grayscale=True)
        pg.click(t[0], t[1])


        t = pg.locateOnScreen(login_bar, grayscale=True, confidence=.5)
        while (t is None):
            t = pg.locateOnScreen(login_bar, grayscale=True, confidence=.5)
        pg.click(t[0], t[1])
        pg.typewrite("826 7964 4481")

        t = pg.locateOnScreen(Enter_password, grayscale=True)
        while(t is None):
            t = pg.locateOnScreen(Enter_password, grayscale=True)
        pg.click(t[0], t[1])

        t = pg.locateOnScreen(Password_enternce, grayscale=True)
        while (t is None):
            t = pg.locateOnScreen(Password_enternce, grayscale=True)
        pg.click(t[0], t[1])
        pg.typewrite("062409")


        t = pg.locateOnScreen(Enter_password)
        while (t is None):
            t = pg.locateOnScreen(Enter_password, grayscale=True)
        pg.click(t[0], t[1])


        t = pg.locateOnScreen(Enterence_with_sound, grayscale=True)
        while(t is None):
            t = pg.locateOnScreen(Enterence_with_sound, grayscale=True)
        pg.click(t[0], t[1])


        t = pg.locateOnScreen(Turn_on_Sound, grayscale=True, confidence = .5)
        while (t is None):
            t = pg.locateOnScreen(Turn_on_Sound, grayscale=True, confidence = .5)
        pg.click(t[0], t[1])
        count += 1

    else:
        time.sleep(120)
















