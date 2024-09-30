import pygame

# Initialize pygame
pygame.init()

# Set global variables
WIDTH = 300
HEIGHT = 350 

# Width of the lines
LINE_WIDTH = 15

# Set the rows and columns 
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = WIDTH // BOARD_COLS

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

import pygame

# Initialize pygame
pygame.init()

# Initialize the game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

# Set the font for rendering text
font = pygame.font.Font(None, 36)

# Function to draw the grid lines for the board
def draw_lines():
    # Draw horizontal lines
    pygame.draw.line(screen, BLACK, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)

    # Draw vertical lines
    pygame.draw.line(screen, BLACK, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT - 50), LINE_WIDTH)
    pygame.draw.line(screen, BLACK, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT - 50), LINE_WIDTH)

# Function to draw an X at a given row and column
# This function can be provided!  
def draw_x(row, col):
    start_desc = (col * SQUARE_SIZE + LINE_WIDTH, row * SQUARE_SIZE + LINE_WIDTH)
    end_desc = (col * SQUARE_SIZE + SQUARE_SIZE - LINE_WIDTH, row * SQUARE_SIZE + SQUARE_SIZE - LINE_WIDTH)
    pygame.draw.line(screen, RED, start_desc, end_desc, LINE_WIDTH)  # Descending line
    start_asc = (col * SQUARE_SIZE + LINE_WIDTH, row * SQUARE_SIZE + SQUARE_SIZE - LINE_WIDTH)
    end_asc = (col * SQUARE_SIZE + SQUARE_SIZE - LINE_WIDTH, row * SQUARE_SIZE + LINE_WIDTH)
    pygame.draw.line(screen, RED, start_asc, end_asc, LINE_WIDTH)  # Ascending line

# Function to draw an O at a given row and column
def draw_o(row, col):
    center = (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2)
    pygame.draw.circle(screen, BLACK, center, SQUARE_SIZE // 3, LINE_WIDTH)  # Draw the circle

# Function to display a message at the bottom of the screen
def display_message(text):
    screen.fill(WHITE, (0, HEIGHT - 50, WIDTH, 50))  # Clear the bottom area for new text
    message = font.render(text, True, BLUE)  # Render the text
    screen.blit(message, (WIDTH // 2 - message.get_width() // 2, HEIGHT - 40))  # Display the text

# Function to check if there is a winner
def check_winner():
    # Check for vertical, horizontal, and diagonal wins
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != 0:
            return board[0][col]  # Return the player number (1 or 2) if there's a win in a column
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != 0:
            return board[row][0]  # Return the player number if there's a win in a row
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != 0:
        return board[0][0]  # Return the player number if there's a win in a descending diagonal
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != 0:
        return board[0][2]  # Return the player number if there's a win in an ascending diagonal
    return 0  # Return 0 if no winner

# Draw the initial board and display the first player's turn
draw_lines()
display_message("X's Turn")

# Main game loop
player = 1  # 1 for X, 2 for O
board = [[0] * BOARD_COLS for _ in range(BOARD_ROWS)]  # Initialize the game board with 0s
game_over = False  # Flag to check if the game is over

while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If the user clicks the close button
            game_over = True
            pygame.quit()  # Quit the game

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]  # X coordinate of where the screen was clicked
            mouseY = event.pos[1]  # Y coordinate of where the screen was clicked

            clicked_row = mouseY // SQUARE_SIZE  # Determine the row where the click occurred
            clicked_col = mouseX // SQUARE_SIZE  # Determine the column where the click occurred

            # Place X or O if the clicked cell is empty
            if board[clicked_row][clicked_col] == 0:
                if player == 1:
                    draw_x(clicked_row, clicked_col)  # Draw X
                    board[clicked_row][clicked_col] = 1  # Mark the board
                    player = 2  # Switch to player 2
                elif player == 2:
                    draw_o(clicked_row, clicked_col)  # Draw O
                    board[clicked_row][clicked_col] = 2  # Mark the board
                    player = 1  # Switch to player 1

                # Check for a winner after each move
                winner = check_winner()
                if winner != 0:
                    game_over = True  # Set the game over flag
                    winner_text = "X Wins!" if winner == 1 else "O Wins!"
                    display_message(winner_text)  # Display the winning message
                else:
                    # Update the display to show the current player's turn if the game is not over
                    if not game_over:
                        display_message("X's Turn" if player == 1 else "O's Turn")

    pygame.display.update()  # Refresh the game screen
