#######################################
# The Blue Marble Academy 
# Pygame – Basics and Event Handling 

# NOTE: In a separate Python file, complete the exercises after reviewing each section. 
# Mario.png must be stored in the same folder as this file to run it
#######################################
# Import and intialze pygame
# pygame.init() is necessary to use the pygame commands
import pygame
pygame.init()

# Exercise 1: Import and Initialize pygame in your new file

#######################################
# Create the screen 
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

# Exercise 2: Create the screen with a different width and height

#######################################
# Creating a rectangle 
# The first two arguments are the placement of the rectangle on the screen, x & y
# The top left corner of the screen is represented by x=0, y=0
# The bottom right corner of the screen is the x=width and the y=height of the screen
# To move down, add to x, to move up, add to y
# The second two arguments are the width and the height of the the rectangle
# NOTE: The rectangle will not appear on the screen yet, it needs to be drawn in the game loop

x = 60
y = 400
rectangle = pygame.Rect(x,y,30,30)

# Exercise 3: Create another rectangle: 
# Add a second rectangle to the screen at a different position, say (200, 300)
# Try out different values for the width and height

# Exercise 4: Add another shape like a circle or another rectangle to the screen.
#    - Use `pygame.draw.circle()` for drawing the circle.

#######################################
# Loading an image
# Make sure the image is stored in the same folder as this python file
# NOTE: The image will not appear on the screen yet, it must be blitted in the game loop
image = pygame.image.load("Mario.png") 

# Resize the image
new_width, new_height = 250, 300  # Update these values to your desired size
resized_image = pygame.transform.scale(image, (new_width, new_height))


# Exercise 5: Add another image (different from "Mario.png") to the screen in your file.   

#######################################
# Game loop 
# The most important part of the game development code is the game loop. All games will have a game loop.
# This loop continuously runs in the background until the user ends the game or the game is over. 
running = True

while running: 
    # Loops through the events in pygame
    # All games must have this code
    for event in pygame.event.get():
        # The event to quit the pygame screen  
        # checks if user clicks x 
        if event.type == pygame.QUIT:
            # Stop the game loop
            running = False

    # Change the screen colour 
    # White = (255, 255, 255)
    # Black = (0, 0, 0)
    # Exercise: Set the screen colour in your Python file
    screen.fill((255, 255, 255))

    # Draw the rectangle
    # The first argument is always the screen
    # The second argument is the colour of the rectangle
    # Exercise 6: Draw your circle and rectangle in your python file
    pygame.draw.rect(screen, (0, 0, 0), rectangle) 

    # Draw the image 
    # Blit keyword is used to draw a surface on another surface. 
    # When we draw an image we just blit it onto some other surface (the screen).
    # The second argument, (x, y), is the placement of the image on the screen 
    # Exercise 7: Blit your image
    screen.blit(resized_image, (0, 0))

    # Flip is used to update the entire screen after everything is drawn. 
    # All games must have this code
    # Remember that the flip only works after drawing all the necessary surfaces otherwise, 
    # it will update nothing. Flip is usually found at the bottom of the game loop. 
    # NOTE: Only flip the screen once all the game features are drawn (at the bottom of the while loop)
    pygame.display.flip()

