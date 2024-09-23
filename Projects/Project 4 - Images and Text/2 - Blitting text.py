# ======================================
# Here we discuss blitting text, this file may be
# useful as a template for putting a timer into a game,
# for instance
# ======================================
# Additional Work:
# - try blitting new text lines
# - (difficult) try blitting text imported from a text file (see hangman game from beginner program for additional aid)
# ======================================


# as usual, we have to import the module
import pygame as py

# initialize pygame
py.init()

# create and name window
win = py.display.set_mode((1000,800))
py.display.set_caption('Text and Timer Setup')

# initialize text module
py.font.init() 
my_font = py.font.SysFont('Comic Sans MS', 30)

# main loop for image
run, t = True, 0
while run:

    # fills window with black background
    win.fill((255,255,255))

    # draws a timer in the corner
    timer = my_font.render('Time elapsed: '+str(t), False, (0, 0, 0))
    win.blit(timer, (0,0))
    t = round(t + 0.01, 2)
    
    # checks if you clicked X, quits animation
    for e in py.event.get():
        if e.type == py.QUIT:
              py.quit()
              run = False

    # update visual
    py.time.wait(10)
    py.display.update()

# this is redundant here, but is good practice to quit when finished
py.quit()
