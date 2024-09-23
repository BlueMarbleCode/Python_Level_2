# The Blue Marble Academy
# Snake Game 
# Made by Darian and Arifa

import pygame
import random
import end  # Assuming end.py handles the game over screen

# Initialize Pygame and set up the screen
def initialize_game():
    pygame.init()
    dis = pygame.display.set_mode((800, 600))
    return dis

# Load the apple image and transform it to the correct size
def load_apple_image():
    apple = pygame.image.load("apple.png").convert()
    return pygame.transform.scale(apple, (30, 30))

# Handle key events and update snake's direction
def handle_key_events(x_change, y_change):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y_change = 10
                x_change = 0
            if event.key == pygame.K_UP:
                y_change = -10
                x_change = 0
            if event.key == pygame.K_LEFT:
                x_change = -10
                y_change = 0
            if event.key == pygame.K_RIGHT:
                x_change = 10
                y_change = 0

    return x_change, y_change

# Check if the snake collides with the apple
def check_apple_collision(x, y, apple_x, apple_y):
    if x < apple_x + 30 and x + 30 > apple_x and y < apple_y + 30 and y + 30 > apple_y:
        return True
    return False

# Update snake's position and body
def update_snake(snake_segments, x, y, score):
    snake_segments.append([x, y])
    if len(snake_segments) > score:
        del snake_segments[0]
    return snake_segments

# Check for collisions with the screen border or the snake's own body
def check_collision(x, y, snake_segments, score):
    # Check if snake collides with the wall
    if x <= 0 or x >= 770 or y >= 570 or y <= 0:
        end.main(score)
        return True

    # Check if snake collides with itself (only if snake has more than 1 segment)
    for segment in snake_segments[:-1]:  # Exclude the current head (last segment)
        if segment == [x, y]:
            end.main(score)
            return True

    return False

# Draw the game elements on the screen (snake, apple, score, border)
def draw_elements(dis, snake_segments, snake_apple, apple_x, apple_y, x, y, score):
    # Clear screen
    dis.fill((255, 255, 255))

    # Draw the apple
    dis.blit(snake_apple, (apple_x, apple_y))

    # Draw the snake
    pygame.draw.rect(dis, (0, 0, 255), (x, y, 30, 30))  # Snake head
    for segment in snake_segments:
        pygame.draw.rect(dis, (0, 0, 255), (segment[0], segment[1], 30, 30))  # Snake body

    # Draw the score
    font = pygame.font.Font(None, 45)
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    dis.blit(score_text, (50, 25))

    # Draw the border
    pygame.draw.rect(dis, (0, 0, 0), (0, 0, 10, 600))   # Left
    pygame.draw.rect(dis, (0, 0, 0), (0, 0, 850, 10))   # Top
    pygame.draw.rect(dis, (0, 0, 0), (0, 590, 850, 10)) # Bottom
    pygame.draw.rect(dis, (0, 0, 0), (790, 0, 10, 600)) # Right

    # Update the display
    pygame.display.update()

# Main game loop
def main():
    # Initial settings
    dis = initialize_game()
    clock = pygame.time.Clock()

    apple_x = random.randint(0, 760)
    apple_y = random.randint(0, 560)
    snake_apple = load_apple_image()

    x = 300
    y = 300
    x_change = 0
    y_change = 0
    score = 1  # Starting score, snake is 1 segment long initially
    snake_segments = []

    game_over = False

    # Main game loop
    while not game_over:
        # Handle key events
        x_change, y_change = handle_key_events(x_change, y_change)

        # Update snake position
        x += x_change
        y += y_change

        # Check if the snake collides with the apple
        if check_apple_collision(x, y, apple_x, apple_y):
            score += 1
            apple_x = random.randint(0, 760)
            apple_y = random.randint(0, 560)

        # Update the snake's body
        snake_segments = update_snake(snake_segments, x, y, score)

        # Check for game over conditions
        if check_collision(x, y, snake_segments, score):
            game_over = True

        # Draw everything on the screen
        draw_elements(dis, snake_segments, snake_apple, apple_x, apple_y, x, y, score)

        # Control the frame rate
        clock.tick(25)

if __name__ == "__main__":
    main()
