# =================================
# Sample project: Juggling Game
# By: Nicholas Miceli
# ---------------------------------
# This basic game utilises functions previously discussed in the course
# you may use this as a base for your own game, adding on additional
# quirks, or simply use it as inspiration for creative methods of implementing
# the collision function
# ---------------------------------
# Suggested Changes:
#   - randomizing the ball's speed
#   - adding a second player
#   - adding progressively more balls
#   - use as base for a brick breaker type game (tough)
# ---------------------------------
# Addendum: this code uses sine and cosine to help in drawing the ball's flight,
# this is very useful for our work, as such, an additional review of these concepts
# is included entitled: "sine_and_cosine_basics"
# =================================

# importing the pygame module and other useful modules
import pygame as py
from collision_supp import *
import random, math

# draws ball trajectory
def ball_flight(xlen,ylen,ball_pos,arc,speed = 10):
      py.draw.circle(win,BLACK,ball_pos[:2],ball_pos[2])
      return [int(ball_pos[0] + speed * math.cos(arc)), int(ball_pos[1] - speed * math.sin(arc)), ball_pos[2]]
                  
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
xlen = 800
ylen = 800
win = py.display.set_mode((xlen, ylen))
t = 0

# dimensions and starting positions
width = 150
height = 20
rad = 10
pos = [int(xlen/2)-width//2,int(ylen*9/10),width,height]
ball_pos = [int(xlen/2),0,rad]
arc = math.pi*random.randint(240,300)/180

# dimensions of end zone and walls
end = (0,ylen*39/40,xlen,10)
walls = ((-20,0,20,ylen),(0,-20,xlen,20),(xlen,0,20,ylen))

# initialize text module
py.font.init() 
my_font = py.font.SysFont('Comic Sans MS', 30)

# main game loop
while run:

      # check for key inputs 
      keys = py.key.get_pressed()
      if keys[py.K_LEFT] and pos[0] > 0:
            pos[0] += -10
 
      if keys[py.K_RIGHT] and pos[0] < xlen - width:
            pos[0] += 10

      # this key is just to reset the ball for testing purposes
      if keys[py.K_SPACE]:
            arc = math.pi*random.randint(240,300)/180
            ball_pos = [int(xlen/2),0,rad]

      # checks if user clicks x to quit
      for e in py.event.get():
            if e.type == py.QUIT:
                  py.quit()
                  run = False

      # draws all objects and updates display
      win.fill((200,0,200))
      py.draw.rect(win,BLACK,pos)
      py.draw.rect(win,BLUE, end)

      # translates ball
      ball_pos = ball_flight(xlen,ylen,ball_pos,arc)
      ball_rect = (*ball_pos, rad, rad)

      # check if ball hit your paddle
      if collision(pos,ball_rect):
            arc = -arc

      # checks if a wall was hit, technically, we could incorporate
      # the line above, but its far messier and is an example of an
      # occasion where clarity wins over speed
      for wall in enumerate(walls):
            if collision(wall[1], ball_rect):
                  arc = (wall[0] + 1)* math.pi - arc

      # checks if the ball was dropped
      if collision(end,ball_rect):
            print('ended')

      # draws a timer in the corner, to display how long the ball has been kept up
      timer = my_font.render('Time elapsed: '+str(t), False, (0, 0, 0))
      win.blit(timer, (0,0))
      t = round(t + 0.01, 2)
      
      # update window
      py.time.wait(10)
      py.display.update()

py.quit()
