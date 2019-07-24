import metin2.mt2 as mt2
import time

skill = []
actions = []

class skills:
   def __init__(self): 
        self.name = 'metin2'
        self.skill1 = 1
        self.skill2 = 2
        self.skill3 = 2
        self.skill4 = 1

   def getname(self):
        return self.name

   def reset_skill1(self):
        self.skill1 = 102
        mt2.game.start_skill_1()

   def reset_skill2(self):
        self.skill2 = 10
        mt2.game.start_skill_2()  

   def reset_skill3(self):
        self.skill3 = 15
        mt2.game.start_skill_3()

   def reset_skill4(self):
        self.skill4 = 63
        mt2.game.start_skill_4()

   def reset_fisical(self):
        mt2.game.start_fisical()

   def decrease(self): 
        self.skill1 -= 1
        self.skill2 -= 1
        self.skill3 -= 1
        self.skill4 -= 1

   def reset(self):
      print(self.skill1, self.skill2, self.skill3, self.skill4)
      if self.skill1 < 1 :
         self.reset_skill1() 
      elif self.skill2 < 1 :
         self.reset_skill2() 
      elif self.skill3 < 1 :
         self.reset_skill3() 
      elif self.skill4 < 1 :
         self.reset_skill4()    
      else:
         print('--')              

skill = skills()                  

class actions:
   def __init__(self): 
        self.name = 'metin2'
        self.time_move = 6
        self.time_atk  = 20
        self.atk = False
        self.first_mob = False
        self.win_position = False
        self.health = False
        self.dead = False
        self.dir  = 's'

   def search_boss(self) :
     atk = False 
     if self.first_mob and self.win_position : 
        for mob in self.first_mob:           
           if mob[0] > 150 and mob[0] < 550 and mob[1] > 150 and mob[1] < 550 :   # tela perto
           #if mob[0] > 200 and mob[0] < 550 and mob[1] > 200 and mob[1] < 550 :  # tela longe
              atk = True
           #  print('True',mob)              
           #else :
           #  print('False',mob)    
        
        if atk == True :
           #print('active_fisical', mt2.game.fisical_atk)           
           skill.reset() 
           old = self.dir
           mt2.game.active_fisical() 
           if self.dir == 'w':
              self.dir = 's'
           else :
              self.dir = 'w'   

           mt2.game.up(old)           
           mt2.game.press(self.dir)           
             

        elif atk == False :
           mt2.game.start_click((self.first_mob[0][0],self.first_mob[0][1]) , self.win_position )
           mt2.game.disable_fisical()  
           mt2.game.up('w')  
           mt2.game.up('s')                                          
     else :
        self.move()

     if atk == False :
        #print('disable_fisical', mt2.game.fisical_atk)
        mt2.game.disable_fisical()          
        mt2.game.up('w')  
        mt2.game.up('s')  
   ##search_boss         
                           
   def allow_pot(self) :
      mt2.game.start_pot()  

   def allow_cash_pot(self) :
      if self.health :
         mt2.game.start_pot_cash()  
         mt2.game.start_click( ( 715, 70 ) , self.win_position )     

   def allow_blue_pot(self) :
      mt2.game.start_blue_pot()       

   def allow_drop(self):       
      mt2.game.start_drop()  

   def move(self) :
      print('mt2.game.move')
      mt2.game.move()  
      mt2.game.start_click( ( 500, 40 ) , self.win_position )

   def revive(self) :
      print('revive',self.dead)
      mt2.game.start_click( (self.dead[0]+50, self.dead[1]-50) , self.win_position )
      mt2.game.start_pot()
      mt2.game.start_pot()
      mt2.game.start_pot()
      mt2.game.start_pot()
      mt2.game.start_pot()
      mt2.game.disable_fisical() 
      time.sleep(20)

   def allow_atk(self, list_mob, win_position, health, dead) :
      self.first_mob  = list_mob
      self.win_position  = win_position
      self.health = health
      self.dead   = dead
      
      if not self.dead :
         self.search_boss() 
      else :
         self.revive()   
   ##allow_atk       
      


action = actions()

def loop():
   skill.decrease() 

def loop_full():
   action.allow_pot()
   action.allow_cash_pot()
   action.allow_drop()
        

SETT = [15,15,15,15,15,15,15] 
def set(index, val):
   SETT[index] = val

def get(index):
   return SETT[index]    