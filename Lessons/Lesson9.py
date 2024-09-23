#######################################
# The Blue Marble Academy 
# Movement Using Keys, Creating Buttons, Collision Detection, and Adding Sound 
#######################################
# Import and initialize pygame
import pygame

pygame.init()

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
# Load sound
# Make sure the sound file is in the same folder as this Python file
sound = pygame.mixer.Sound("button_click.mp3")

#######################################
# Create a player rectangle
player_width = 50
player_height = 50
player_x = width // 2
player_y = height // 2
player_speed = 1

# Create a button
button_color = BLUE
button_width = 150
button_height = 50
button_x = (width - button_width) // 2
button_y = (height - button_height) // 2
button = pygame.Rect(button_x, button_y, button_width, button_height)

# Create a target rectangle for collision detection
target_color = RED
target_width = 100
target_height = 100
target_x = width // 4
target_y = height // 4
target = pygame.Rect(target_x, target_y, target_width, target_height)

#######################################
# Check collision with the target
def check_collision():
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    target_rect = pygame.Rect(target_x, target_y, target_width, target_height)
    return player_rect.colliderect(target_rect)

#######################################
# Game loop 
running = True

while running:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

        # Handle button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            if button.collidepoint(mouse_x, mouse_y):
                sound.play()

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

    # Draw the target
    pygame.draw.rect(screen, target_color, target)

    # Draw the player
    # Check for collisions
    if check_collision():
        pygame.draw.rect(screen, BLACK, (player_x, player_y, player_width, player_height))  # Draw player in black on collision
    else: 
        pygame.draw.rect(screen, GREEN, (player_x, player_y, player_width, player_height))

    # Draw the button
    pygame.draw.rect(screen, button_color, button)

    # Update the display
    pygame.display.flip()
