# Animation with Sprites!
# ================================
# A simple example of movement animation
# ================================
# Additional Work:
# - while jumping is incorporated, and sprites are included in this file's folder
#   they have not been implemented, discuss what would need to be done to do so,
#   if you have time, it is good practice to attempt to do so yourself 
# ================================

# importing the pygame module 
import pygame as py
from jump_supp import JUMP  
            
# a list of colors for easy access
BLACK = (0,0, 0)
WHITE = (255,255,255)

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
pos = [int(xlen/2),int(ylen/2 - 80),50,50]

# load all images
sprites_R = [py.image.load('M(R0).png'),py.image.load('M(R1).png'),py.image.load('M(R2).png')]
sprites_L = [py.image.load('M(L0).png'),py.image.load('M(L1).png'),py.image.load('M(L2).png')]

# transform sprites to apropriate size
for i in range(len(sprites_R)):
    sprites_R[i] = py.transform.scale(sprites_R[i],(55,100))
    sprites_L[i] = py.transform.scale(sprites_L[i],(55,100))

# makes a single tuple of all relavent sprites
sprites = (sprites_L,sprites_R)

# for determining what sprite to draw
current = 0
direction = 0

# main game loop
while run:

      # check for key inputs 
      keys = py.key.get_pressed()
      if keys[py.K_LEFT]:
            pos[0] += -5
            direction = 0 # 0 = left, 1 = right, -1 = no movement
            current += 1

      elif keys[py.K_RIGHT]:
            pos[0] += 5
            direction = 1
            current += 1

      else:
            current = 0 # resets sprite to standing still if l/r not pressed

      # These lines are for the jumping function
      if keys[py.K_UP] and jump[0] == False:
            jump = [True,0]

      if jump[0] == True:
            pos,jump = JUMP(pos,jump[1],5,True)


      # checks if user clicks x to quit
      for e in py.event.get():
          
            if e.type == py.QUIT:
                  py.quit()
                  run = False

      # draws all objects and updates display
      win.fill(WHITE)
      py.draw.rect(win,BLACK,(0,320,xlen,25))
      win.blit(sprites[direction][current % 3], pos)
      
      # update window
      py.time.wait(11)
      py.display.update()

py.quit()
