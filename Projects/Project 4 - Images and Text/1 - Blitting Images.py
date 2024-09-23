# ======================================
# Here we discuss blitting images, this file may be
# useful as a template for putting a png's into a game,
# for instance. This is the basis of spritework, games
# will loop between a set of sprites (or images) to
# give the illusion of motion, for instance.
# ======================================
# Additional work:
# - Find another image online, try to blit it instead
# - try implementing a basic movement system, like we did with the animated ball previously
# ======================================




# as usual, we have to import the module
import pygame as py

# initialize pygame
py.init()

# create and name window
win = py.display.set_mode((1000,800))
py.display.set_caption('Moving Rock Animation')

# load image
# NOTE: images must be in the same folder as this script
rock = py.image.load('rock.png')

# position of image
x = 0
y = 0
run = True

# main loop for image
while run:

    # fills window with black background
    win.fill((0,0,0))
    
    # moves image
    x += 1
    y += 1

    # displays image
    win.blit(rock,(x,y))
    py.display.update()
    py.time.wait(30)

    # checks if you clicked X, quits animation
    for e in py.event.get():
        if e.type == py.QUIT:
              py.quit()
              run = False

# this is redundant here, but is good practice to quit when finished
py.quit()
