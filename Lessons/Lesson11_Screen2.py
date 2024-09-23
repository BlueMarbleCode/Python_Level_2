#######################################
# The Blue Marble Academy 
# Boundary Checking and Multiple Screens
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
RED = (139, 0, 0)

#######################################
# Main function to display Game Over screen
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

        # Clear the screen
        screen.fill(WHITE)

        # Set up font and text
        font = pygame.font.Font(None, 74)
        text = font.render("Game Over", True, RED)
        
        # Draw the text
        screen.blit(text, (250, 280))

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()