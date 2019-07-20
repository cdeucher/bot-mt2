import time, os
from ahk import AHK

##AutoHotkey.exe
dirpath = os.getcwd()+'\\bin'
ahk = AHK(executable_path=dirpath+'\\bin.exe')
ahk.key_press('`')
##
##  CLASS
##
class gameSkills:
   def __init__(self): 
       self.skill = 0
       self.fisical_atk = False
       self.key = ['a','d']
       self.indexkey = 0

   def move(self):
       ahk.key_press('e')  
       ahk.key_press('e') 
       ahk.key_press('e') 
       ahk.key_press('e')  
       ahk.key_press('e') 
       #ahk.key_press('e')     
          
   def press(self, key):
       ahk.key_down(key)
       #print("key_down("+key+")")

   def up(self, key):
       ahk.key_up(key)
       #print("key_up("+key+")")

   def start_skill_1(self):
       ahk.key_press('1')
       print("key_press('1')")

   def start_skill_2(self):
       ahk.key_press('2')
       print("key_press('2')")

   def start_skill_3(self):
       ahk.key_press('3')
       print("key_press('3')")

   def start_skill_4(self):
       ahk.key_press('4') 
       print("key_press('4')")                     

   def active_fisical(self):
       if not self.fisical_atk :
          ahk.key_down('Space') 
          self.fisical_atk = True
       else :
          ahk.key_press(self.key[self.indexkey]) 
          #print('indexkey',self.key[self.indexkey])  
          if self.indexkey == 0 :
             self.indexkey = 1
          else :
             self.indexkey = 0   

   def disable_fisical(self):
       if self.fisical_atk : 
          ahk.key_up('Space')
          self.fisical_atk = False                   

   def start_pot(self):
       ahk.key_press('f2')  

   def start_pot_cash(self):
       ahk.key_press('f3') 
       ahk.key_press('f1') 

   def start_blue_pot(self):
       ahk.key_press('f4')  
    

   def start_drop(self):
       ahk.key_press("'")  

   def start_click(self, first_mob, win_position):
       click_position = (first_mob[0]+win_position[0] , first_mob[1]+win_position[1]) #+65

       #print('click_position',click_position)
       ahk.mouse_position = click_position
       ahk.click()    


game = gameSkills()   

##
##  FUNCTIONS
##
def check_open_game():
  try:

    win = ahk.find_window(title=b'METIN2')
    win.activate()

    for window in ahk.windows():
        if window.title == b'METIN2':
          return window.rect
    return (0,0,0,0)

  except AttributeError: 
    print('no game open')
    return False

def game_atk(position, win_position, ahk):
  try:
    click_position = (position[0]+win_position[0]+35 , position[1]+win_position[1]+ 25)

    print(click_position)
    ahk.mouse_position = click_position
    ahk.click()

    time.sleep(3)
    moveMetin2x(ahk)

  except Exception as e:
    print('fail click')

    ahk.key_down('a')
    time.sleep(2)
    ahk.key_up('a') 
