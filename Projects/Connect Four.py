# ============================
# base version of python connect 4 game
# ============================
# This version is purposefully unfinished students can use it as a base for their final project and add: 
# - piece drops to bottom, don't need to check where we clicked in y axis (since it drops), consider using true/false of pos_list
# - win/loss condition, use pos_list T/F, check if ever a 4 in a row, display that yellow / red won
# ============================


import math, random, pygame
from pygame.locals import *

# draw the lines, its modular so that the window
# size is irrelevant
def draw_grid(win, xlen,ylen, color = (0,0,0)):
      xpos, ypos = 0, 0
      xstep, ystep = xlen/7 , ylen/6

      # draw the rows
      for i in range(8):
            pygame.draw.rect(win,color,(xpos,0, 5,ylen))
            xpos += xstep

      # draw the columns
      for i in range(7):
            pygame.draw.rect(win,color,(0,ypos, xlen,5))
            ypos += ystep

# draws disc where clicked
def draw_circle(win, pos_list, mousepos = (0,0), color = (0,0,0)):

      # checks the line in which the button has been clicked
      for i in range(len(pos_list)):
            if pos_list[i][0] < mousepos[0] and mousepos[0] < pos_list[i+1][0] and pos_list[i][2] == True:
                  xpos = int((pos_list[i][0] + pos_list[i+1][0])/2)
                  xsave = pos_list[i][0]
            if pos_list[i][1] < mousepos[1] and mousepos[1] < pos_list[i+1][1] and pos_list[i][2] == True:
                  ypos = int((pos_list[i][1] + pos_list[i+1][1])/2)
                  ysave = pos_list[i][1]

      # tries to find the place the user clicked, then turns true to false (if possible), then draws the circle
      try:
            place = [i for i in pos_list if i == [xsave,ysave,True]]
            pos_list[pos_list.index(place[0])][2] = False
            pygame.draw.circle(win,color,(xpos,ypos), int(xlen/25))
            turn = 1 # turn is only increased if the player is able to place a piece

      except:
            turn = 0

      return pos_list, turn 
      

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
pygame.init()
pygame.font.init()

# creates window
xlen = 1000
ylen = 600
win = pygame.display.set_mode((xlen, ylen))

# color the window
win.fill(LIGHT_BLUE)

# call the draw grid function
draw_grid(win,xlen,ylen)
turn = 0
player_color = (RED,YELLOW)
pos_list = []
ypos = 0
xstep, ystep = xlen/7 , ylen/6

# list of all combinations of positions
for i in range(7):
      xpos = 0
      for j in range(8):
            pos_list.append([xpos,ypos,True])
            xpos += xstep
      ypos += ystep

# main game loop    
while True:
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                  create = draw_circle(win, pos_list, pygame.mouse.get_pos(),player_color[turn%2])
                  turn += create[1]
                  pos_list = create[0]
      pygame.display.update()
