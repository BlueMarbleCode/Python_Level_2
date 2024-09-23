# Collision Pygame Basics
# ================================
# - this code demonstrates some pygame fundamentals
# - initialization, windows, drawing, events, and keypresses
# - students can use the collision and JUMP modules in their
#   work, it is important to understand their implementation
# ================================

# importing the pygame module 
import pygame as py
from jump_supp import JUMP
from collision_supp import *

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

# creates window
xlen = 1000
ylen = 600
win = py.display.set_mode((xlen, ylen))

# your starting position
pos = [int(xlen/2),int(ylen/2 - 25),50,50]

# this is the red box that resets position, try changing some parameters!
deathbox = (100,100,100,100)

# main game loop
while run:

      
      
      # check for key inputs 
      keys = py.key.get_pressed()
      if keys[py.K_LEFT]:
            pos[0] += -5

      if keys[py.K_RIGHT]:
            pos[0] += 5

      # These lines are for the jumping function
      if keys[py.K_UP] and jump[0] == False:
            jump = [True,0]

      if jump[0] == True:
            pos,jump = JUMP(pos,jump[1],14)

      # checks if user clicks x to quit
      for e in py.event.get():
            if e.type == py.QUIT:
                  py.quit()
                  run = False

      # draws all objects and updates display
      win.fill(LIGHT_BLUE)
      py.draw.rect(win,RED,deathbox)
      py.draw.rect(win,BLACK,(0,320,xlen,25))
      py.draw.rect(win,WHITE,pos)
      
      # update window
      py.time.wait(10)
      py.display.update()

      # check if there was a collision
      reset = collision(deathbox,pos)

      # resets your position if you step into the box
      if reset == True:
            pos = [int(xlen/2),int(ylen/2 - 25),50,50]
            jump = [True,0]

# TECHNICALLY, what we're doing is repeatedly redrawing a ball, which we move along the surface
# the surface is being repeatedly refilled
