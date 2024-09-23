# Bullet Dodger Game
# ================================
# a simple game made for dodging
# moving bullets
# ================================

# importing the pygame module 
import pygame as py
from jump_supp import JUMP
from collision_supp import *
from bullets_supp import *
import tkinter
import lost_supp as LOST
            
# a list of colors for easy access
BLACK = (0,0, 0)
WHITE = (255,255,255)
RED   = (255,0, 0)
GREEN = (0,255,0)
BLUE  = (0,0,255)
LIGHT_BLUE = (102,255,255)
BROWN = (100,100,0)
YELLOW = (255,255,0)

# initialize pygame
py.init()
py.font.init()
run = True
jump = [False,0]
jump2 = [False,0]

# creates window
xlen = 1000
ylen = 600
win = py.display.set_mode((xlen, ylen))

# your starting position
pos = [int(xlen/2),int(ylen/2 - 25),50,50]
pos2 = [int(xlen/2),int(ylen/2 - 25),50,50]

# create bullets
enemies = create_bullets(2,YELLOW, (-50,xlen),(100,300),False,7,True)

# main game loop
while run:

      # check for key inputs 
      keys = py.key.get_pressed()
      if keys[py.K_LEFT]:
            pos[0] += -10

      if keys[py.K_RIGHT]:
            pos[0] += 10

      if keys[py.K_a]:
            pos2[0] += -10

      if keys[py.K_d]:
            pos2[0] += 10

      # These lines are for the jumping function
      if keys[py.K_UP] and jump[0] == False:
            jump = [True,0]

      if jump[0] == True:
            pos,jump = JUMP(pos,jump[1],7,True)

      if keys[py.K_w] and jump2[0] == False:
            jump2 = [True,0]

      if jump2[0] == True:
            pos2,jump2 = JUMP(pos2,jump2[1],7,True)

      # checks if user clicks x to quit
      for e in py.event.get():
            if e.type == py.QUIT:
                  py.quit()
                  run = False

      # draws all objects and updates display
      win.fill((125,125,125))
      py.draw.rect(win,BLACK,(0,320,xlen,25))
      py.draw.rect(win,WHITE,pos)
      py.draw.rect(win,BROWN,pos2)

      # add bullets
      enemies = move_x(enemies)
      bullet_draw(win,enemies)
      
      # update window
      py.time.wait(12)
      py.display.update()

      # check if there was a collision
      for enemy in enumerate(enemies):

            # once the enemy has reached the end of the screen, a new one is created
            enemies[enemy[0]] = bullet_died(enemy[1])

            # resets your position if you collide
            collide = collision(pos,(enemy[1][0],enemy[1][1],50,20))
            collide2 = collision(pos2,(enemy[1][0],enemy[1][1],50,20))

            # resets your position if you step into the box
            if collide == True or collide2 == True:

                  # check if you want to replay the game or quit
                  # LOST.game_lost()
                  enemies = create_bullets(2,YELLOW, (-50,xlen),(100,300),False,7,True)
                  pos = [int(xlen/2),int(ylen/2 - 25),50,50]
                  pos2 = [int(xlen/2),int(ylen/2 - 25),50,50]
                  jump = [False,0]
                  jump2 = [False,0]
                  break

py.quit()

# TECHNICALLY, what we're doing is repeatedly redrawing a ball, which we move along the surface
# the surface is being repeatedly refilled
