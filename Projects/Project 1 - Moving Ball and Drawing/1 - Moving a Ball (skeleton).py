# Moving A Ball, Pygame Basics
# ================================
# - this code demonstrates some pygmae fundamentals
# - initialization, windows, drawing, events, and keypresses
# - the skeleton version removes checks for all key inputs but K_LEFT
#   ask the student to fill in the rest
# ================================

# importing the pygame module 
import pygame as py

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

# creates window
xlen = 1000
ylen = 600
pos = [int(xlen/2),int(ylen/2)]
win = py.display.set_mode((xlen, ylen))

# main game loop
while run:

      # draws all objects and updates display
      py.time.wait(10)
      win.fill(LIGHT_BLUE)
      py.draw.circle(win,RED,pos,10)
      py.display.update()

      # check for key inputs
      keys = py.key.get_pressed()
      if keys[py.K_LEFT]:
            pos[0] += -5

      ### FILL IN HERE REMAINING KEY INPUTS

      # checks if user clicks x to quit
      for e in py.event.get():
            if e.type == py.QUIT:
                  py.quit()
                  run = False
