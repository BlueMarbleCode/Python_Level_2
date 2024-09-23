# mini golf game
# ==============

import math, random, pygame
from pygame.locals import *
from collision_supp import collision

def draw_terrain(terrain):
      for cmd in terrain:
            if cmd[0] == 'circ':
                  pygame.draw.circle(*cmd[1::])

def place_hole(terrain_chosen,xpos,ypos):
      for cmd in terrain_chosen:
            if cmd[0] == 'circ':
                  pygame.draw.circle(cmd[1],BLACK,(xpos,ypos),25)

def arrow(win,arc,pos,rho):
      pygame.draw.line(win, RED, pos,(pos[0]+rho*math.sin(arc),pos[1]+rho*math.cos(arc)))
      #pygame.draw.polygon(win, (0, 0, 0), ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))


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

##terrain = []
### open a given textfile, read it in
##with open('terrain.txt','r') as f:
##    for l in f:
##        terrain.append(l.strip('\n'))

terrain = [('circ',win,GREEN,(500,300),250),('circ',win,GREEN,(200,400),150),('circ',win,GREEN,(700,100),170)]
cmd = random.randint(0,len(terrain)-1)
cmd = terrain[cmd]
xpos = random.randint(cmd[3][0]-cmd[4]//2,cmd[3][0]+cmd[4]//2)
ypos = random.randint(cmd[3][1]-cmd[4]//2,cmd[3][1]+cmd[4]//2)
pos = xlen/2,ylen
pos_move = xlen/2,ylen
arc, rho, count, pwr, active = math.pi, 70, 0, 0, 20
direct = 1

# text module initialization
pygame.font.init() 
my_font = pygame.font.SysFont('Comic Sans MS', 30)
well = my_font.render('WELL DONE!!!', False, BLACK)

# main game loop    
while True:
      power_text = my_font.render('Power: '+str(pwr),False,BLACK)
      
      win.fill(LIGHT_BLUE)
      draw_terrain(terrain)
      place_hole(terrain,xpos,ypos)
      arrow(win,arc,pos,rho)                
                  
      keys = pygame.key.get_pressed()
      if keys[pygame.K_LEFT]:
            arc += 0.005
      if keys[pygame.K_RIGHT]:
            arc -= 0.005
      if keys[pygame.K_SPACE]:
            if pwr > 30:
                  direct = -1

            if pwr < 0.05:
                  direct = 1
                  
            pwr += direct * 0.05
            pwr = round(pwr,2)
            
      for event in pygame.event.get():
            if event.type == pygame.QUIT:
                  pygame.quit()
            if event.type == pygame.KEYUP:
                  if event.key == pygame.K_SPACE:
                        active = 0
      if active < 25:
            active += 1
            pos_move = [pos_move[0]+pwr*math.sin(arc),pos_move[1]+pwr*math.cos(arc)]
            pygame.draw.circle(win, RED,(int(pos_move[0]),int(pos_move[1])),10)
            pygame.time.wait(20)

            if active == 25:
                  pwr = 0
                  if collision((xpos-20,ypos-20,40,40),(pos_move[0]-5,pos_move[1]-5,10,10)):
                        win.blit(well,(100,100))
                        pygame.display.update()
                        pygame.time.wait(300)

                        # re pick random location of hole
                        cmd = random.randint(0,len(terrain)-1)
                        cmd = terrain[cmd]
                        xpos = random.randint(cmd[3][0]-cmd[4]//2,cmd[3][0]+cmd[4]//2)
                        ypos = random.randint(cmd[3][1]-cmd[4]//2,cmd[3][1]+cmd[4]//2)
                        
                  pos_move = xlen/2,ylen
                  pygame.time.wait(250)
                  
      win.blit(power_text,(20,20))
      pygame.display.update()
