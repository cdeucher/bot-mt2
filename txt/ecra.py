
#pip install pywin32

import win32gui
import win32api

dc = win32gui.GetDC(0)
red = win32api.RGB(255, 0, 0)


#win32gui.SetPixel(dc, 100, 100, red)  # draw red at 0,0

while( True ):
    win32gui.Rectangle(dc, 100,100, 300,300)
    win32gui.ReleaseDC(dc,0)

