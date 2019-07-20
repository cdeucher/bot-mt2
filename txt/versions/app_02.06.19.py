from ahk import AHK
from ahk.window import Window
import time


ahk = AHK(executable_path='C:\Program Files\AutoHotkey\AutoHotkey.exe')

def moveMetin2():
    win = ahk.find_window(title=b'METIN2')
    win.activate()

    print('running start skill')
    ahk.key_press('1')
    time.sleep(2)
    ahk.key_press('4')
    time.sleep(2)

    print('running ahead')
    ahk.key_down('w')
    time.sleep(1)
    ahk.key_up('w')

    print('running left') 
    ahk.key_down('a')
    time.sleep(1)
    ahk.key_up('a')

    print('running start pot')
    ahk.key_press('3')
    print('running start atk')
    ahk.key_down('Space')
    ahk.key_press('f3') 
    time.sleep(5)
    ahk.key_up('Space')
    ahk.key_press('f3') 

def moveESO():
    win = ahk.find_window(title=b'Elder Scrolls Online')
    win.activate()
    ahk.click(600, 400) 

    print('running start skill')
    ahk.key_press('1')
    time.sleep(2)

    print('running ahead')
    ahk.key_down('w')
    time.sleep(1)
    ahk.key_up('w')

    print('running left') 
    ahk.key_down('a')
    time.sleep(1)
    ahk.key_up('a')

    print('running start atk')
    ahk.key_press('2')
    time.sleep(2)
    ahk.click(250, 450) 
    time.sleep(1)
    ahk.click(250, 450) 
    time.sleep(1)
    ahk.click(250, 450) 

while True:    
  moveMetin2()
  time.sleep(5)
