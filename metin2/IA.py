
import numpy as np
from metin2.mt2 import game_atk

def A_I_predict(cv2, img_gray):
    lvl = ['match/22.png','match/33.png'] 
    first_mob = [] 
    for img in lvl:
        template = cv2.imread(img,0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

        threshold = 0.8
        loc = np.where( res >= threshold)
        
        for pt in zip(*loc[::-1]):
            first_mob.append(pt)                       
            #font = cv2.FONT_HERSHEY_SIMPLEX
            #cv2.putText(img_gray, str(pt[0])+'x'+str(pt[1]) ,(pt[0],pt[1]), font, 0.5,(255,255,255),2,cv2.LINE_AA)
            #cv2.rectangle(img_gray, ( pt[0]+70,pt[1]+50 ), (pt[0] + w, pt[1] + h), (0,255,255), 2)

    return img_gray,first_mob        

def A_I_health(cv2, img_gray):
    lvl = ['match/bar1.png']

    for img in lvl:
        template = cv2.imread(img,0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

        threshold = 0.8
        loc = np.where( res >= threshold)
        
        first_mob = []
        for pt in zip(*loc[::-1]):
            first_mob = pt                     
            #font = cv2.FONT_HERSHEY_SIMPLEX
            #cv2.putText(img_gray, str(res) ,(pt[0],pt[1]), font, 0.5,(255,255,255),2,cv2.LINE_AA)
            #cv2.rectangle(img_gray, ( pt[0],pt[1] ), (pt[0] + w, pt[1] + h), (0,255,255), 2)

    return first_mob  

def A_I_dead(cv2, img_gray):
    lvl = ['match/dead.png']

    for img in lvl:
        template = cv2.imread(img,0)
        w, h = template.shape[::-1]
        res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

        threshold = 0.8
        loc = np.where( res >= threshold)
        
        first_mob = []
        for pt in zip(*loc[::-1]):
            first_mob = pt                     
            #font = cv2.FONT_HERSHEY_SIMPLEX
            #cv2.putText(img_gray, str(res) ,(pt[0],pt[1]), font, 0.5,(255,255,255),2,cv2.LINE_AA)
            #cv2.rectangle(img_gray, ( pt[0],pt[1] ), (pt[0] + w, pt[1] + h), (0,255,255), 2)

    return first_mob          
