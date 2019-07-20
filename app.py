import time, sys, keyboard, cv2

from screen import grab_screen
from metin2.mt2 import check_open_game
from metin2.IA import A_I_predict, A_I_health, A_I_dead
import metin2.GLOBAL as m2


def main():
  last_time    = time.time()-10
  last_time_two= time.time()-10
  last_time3   = time.time()-10
  win_position = check_open_game()
  print('position current -',win_position)

  print ('---',m2.skill.getname(), '---')

  #remove borda superior "nao pegar nome dos bichos selecionados"
  win_position = list(win_position)
  win_position[1] = win_position[1]+80
  win_position[3] = win_position[3]-150

  while win_position: 
   
    m2.loop_full()

    if time.time()-last_time >= 0.5 :   #controla o game loop 0.5/s
      #screen
      screen = grab_screen(region=win_position)
      #print('Frame took {} seconds'.format(time.time()-last_time))

      img_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

      #---- hidden own name
      #cv2.rectangle(img_gray, (300,190), (380,200), color=(0, 255, 0), thickness=3) #camera perto
      cv2.rectangle(img_gray, (300,210), (380,215), color=(0, 255, 0), thickness=3)  #camera longe

      #---- match
      img_gray, list_mob = A_I_predict(cv2, img_gray)
      health = A_I_health(cv2, img_gray)
      dead   = A_I_dead(cv2, img_gray)
      #print('health',health)
      m2.action.allow_atk(list_mob, win_position, health, dead)     

      #cv2.imshow('window',img_gray)
      #cv2.resizeWindow('window', win_position[2],win_position[3])      

      #loop game      
      last_time = time.time()

      if cv2.waitKey(25) & 0xFF == ord('q'):
          print('close2')
          cv2.destroyAllWindows()
          break

    if keyboard.is_pressed('q'):
        print('close')
        cv2.destroyAllWindows()
        sys.exit() 
   
    if time.time()-last_time_two >= 30 :   #controla o game loop 5/s 
      last_time_two = time.time()
      m2.action.allow_blue_pot()       

    if time.time()-last_time3 >= 1 :   #controla o game loop 1/s
      print('time3 {} seconds'.format(time.time()-last_time3))
      last_time3 = time.time()
      m2.loop()      


if __name__ == "__main__":
  main()   
    
