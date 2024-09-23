from collision_supp import *
import random
import pygame as py

def create_bullets(n,color, dom, rang, updown = False, max_speed = 10, speed_var = False):
      bullets = []
      
      for i in range(n):

            if speed_var == True:
                  speed = random.randint(2,max_speed)

            else:
                  speed = max_speed
            
            a = random.randint(0,1)
            if a == 0:
                  d = 1
            else:
                  d = -1
            
            if updown == False:
                  ypos = random.randint(rang[0],rang[1])
                  xpos = dom[a]
            else:
                  xpos = random.randint(dom[0],dom[1])
                  ypos = rang[-1::-1][a]
            
            bullets.append([xpos,ypos,color,speed,d,(dom,rang)])

      if n == 1:
            return bullets[0]
            
      return bullets

def bullet_died(bullet):
      if bullet[-1][0][0] >= bullet[0] or bullet[-1][0][1] <= bullet[0]:
            return create_bullets(1,bullet[2],bullet[-1][0],bullet[-1][1])

      else:
            return bullet

def move_x(bullets):
      for i in enumerate(bullets):
            bullets[i[0]][0] += i[1][3] * i[1][4]

      return bullets

def bullet_draw(win, bullets):
      for bullet in bullets:
            py.draw.rect(win,bullet[2],(bullet[0],bullet[1],50,20))
