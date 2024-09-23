# ======================================
# Here we discuss creating textboxes, this may is useful
# for all kinds of practical purposes, for instance, making a
# GUI (graphics user interface) for your games, this can then be
# used in place of the shell (IDLE) that we used to make inputs
# previously.
# ======================================
# Additional Work:
# - consider how a rock paper scissors game (like the one made in the beginnner program) 
#   would be able to be enhanced using these text and image blitting tools 
# ======================================



# as usual, we have to import the module
import pygame as py
import sys

# initialize pygame
py.init()

# create a clock, used to guage fps
clock = py.time.Clock()

# create and name window
win = py.display.set_mode((1000,800))
py.display.set_caption('Text and Timer Setup')

# initialize text module
py.font.init() 
my_font = py.font.SysFont('Comic Sans MS', 30)

# default of what the user input
user_said, user_show = '' , ''

# main loop for image
run = True
while run:

    # fills window with black background
    win.fill((255,255,255))

    # checks for events
    for event in py.event.get():

        # if user clicks x, the screen will close
        if event.type == py.QUIT:
            py.quit()

        # if user begins typing
        if event.type == py.KEYDOWN:

            if event.key == py.K_RETURN:

                # wipes input, displays below
                user_show = 'You input "' + user_said + '"'
                user_said = ''

            # Check for backspace
            elif event.key == py.K_BACKSPACE:

                # removes last character
                user_said = user_said[:-1]

            # Unicode standard for string formation
            else:
                user_said += event.unicode
                
    # draw rectangle our textbox
    py.draw.rect(win, (0,0,0), (100,100,120,50))

    # renders current text being written 
    current_text = my_font.render(user_said, True, (100, 100, 100))

    # renders submitted text below box
    display_text = my_font.render(user_show, True, (100, 200, 100))

    # blit both bits of text
    win.blit(current_text, (105, 105))
    win.blit(display_text, (105, 205))

    # display.flip() will update only a portion of the screen 
    py.display.flip()

    # Clock.tick(60) = 60 fps
    clock.tick(60)
