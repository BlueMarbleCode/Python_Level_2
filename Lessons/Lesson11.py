#######################################
# The Blue Marble Academy 
# Boundary Checking and Multiple Screens 
#######################################
# Import and initialize pygame
import pygame
pygame.init()

# Import the second screen
import Lesson10_Screen2

#######################################
# Create the screen 
width = 800
height = 600
screen = pygame.display.set_mode((width, height))

#######################################
# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#######################################
# Create a player rectangle
player_width = 50
player_height = 50
player_x = 0 # Initial position of the player
player_y = 0 # Initial position of the player
player_speed = 0.5

# Create a button to go to the next screen
next_screen = pygame.Rect(650, 500, 100, 70)

#######################################
# Boundary Check
# This functions always keeps the player in bounds of the screen
def boundary():
    # To use the player_x and player_y variables in a function, add the key word global
    global player_x, player_y
    if player_x >= width - 50:
        player_x = width - 50
    if player_x <= 0: 
        player_x = 0
    if player_y >= height - 50:
        player_y = height - 50
    if player_y < 0:
        player_y = 0


#######################################
# Game loop 
running = True

while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()


    # Get the state of all keyboard keys
    keys = pygame.key.get_pressed()
    
    # Move player based on key presses
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Clear the screen
    screen.fill(WHITE)

    # Draw the player
    player = pygame.Rect(player_x, player_y, player_width, player_height)
    pygame.draw.rect(screen, BLUE, player)

    # Call on boundary()
    boundary()

    # Create the next screen button
    pygame.draw.rect(screen, GREEN, next_screen)

    # Go to the next screen if the player collides with the next screen rectangle 
    if player.colliderect(next_screen):
        Lesson10_Screen2.main()
        
    # Update the display
    pygame.display.flip()
