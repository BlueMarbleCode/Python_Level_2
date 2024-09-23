#######################################
# The Blue Marble Academy 
# Lesson 18: Understanding Sprites in Pygame

#######################################
# 1. What are Sprites and How to Use Them 
# Sprites are 2D images or animations that are integrated into a larger scene.
# In Pygame, sprites are used to represent characters, obstacles, and other objects in a game.

# Purpose:
# - **Organize Code**: Sprites help keep related data and functions together for game objects.
# - **Reuse Code**: Once you define a sprite, you can create many instances of it.
# - **Simplify Programs**: Sprites make it easier to manage and update game objects.

#######################################
# 2. Creating Character Sprites 
# Basic Syntax:
# Here is the basic syntax for creating a sprite in Pygame:

import pygame
pygame.init()

# Define a sprite class
class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 255, 0))

        # All sprites have rectangles, this can be useful to check for collision using colliderect
        self.rect = self.image.get_rect()

        # Set the initial x and y for the player
        self.rect.center = (0, 0)

    def update(self):
        # To access the x or y, use rect.x/rect.y
        self.rect.x += 1 # Move the sprite to the right
        self.rect.y += 1 # Move the sprite to the right


# Initialize Pygame
screen = pygame.display.set_mode((800, 600))

# Create the character sprite 
character = Character()

# All sprites must be placed in a group
# Create a sprite group for characters 
all_sprites = pygame.sprite.Group()
all_sprites.add(character)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites.update()

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw all sprites
    all_sprites.draw(screen)

    # Update the display
    pygame.display.flip()

pygame.quit()
