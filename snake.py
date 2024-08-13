import pygame
import random

# Initialize Pygame library, which is necessary for using its functions and modules
pygame.init()

# Constants
SCREEN_WIDTH = 1280   # Set the width of the game window
SCREEN_HEIGHT = 720   # Set the height of the game window
SNAKE_BLOCK = 20      # Size of each block of the snake, also determines movement steps
SNAKE_SPEED = 15      # Speed of the snake (how fast the game updates)

# Colors defined in RGB format
WHITE = (255, 255, 255)  # Color for score text
BLACK = (0, 0, 0)        # Color for snake
RED = (213, 50, 80)      # Color for losing message
GREEN = (0, 255, 0)      # Color for welcome message and food
BLUE = (50, 153, 213)    # Background color of the game

# Initialize the game window with a fixed size of 1280x720 pixels
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Snake Game')  # Set the title of the game window

# Clock object to control the frame rate of the game
clock = pygame.time.Clock()

# Font styles for displaying text on the screen
font_style = pygame.font.SysFont(None, 50)  # Large font for messages
score_font = pygame.font.SysFont(None, 35)  # Smaller font for score

def our_snake(snake_block, snake_list):
    
    """
    Draws the snake on the screen by rendering each block of the snake's body.
    - snake_block: Size of each block of the snake
    - snake_list: List of coordinates for each segment of the snake's body
    """
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_block, snake_block])

def message(msg, color, font, y_displace=0):
    """
    Renders and displays a text message on the screen at a centered position.
    - msg: The message to display
    - color: The color of the text
    - font: The font object to use for rendering the text
    - y_displace: Vertical displacement to adjust text position
    """
    mesg = font.render(msg, True, color)  # Render the text message
    text_rect = mesg.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + y_displace))  # Center the text
    screen.blit(mesg, text_rect)  # Draw the text on the screen

def display_score(score):
    """
    Displays the current score at the top-left corner of the screen.
    - score: The current score to display
    """
    value = score_font.render("Score: " + str(score), True, WHITE)
    screen.blit(value, [0, 0])  # Position the score at the top-left

def pause_menu():
    """
    Displays the pause menu with options to resume, restart, or quit the game.
    """
    paused = True
    while paused:
        screen.fill(BLUE)
        message("Game Paused", GREEN, font_style, -100)
        message("Press R to Restart, Q to Quit, or ESC to Resume", WHITE, score_font, 50)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart the game
                    game_loop()
                if event.key == pygame.K_q:  # Quit the game
                    pygame.quit()
                    quit()
                if event.key == pygame.K_ESCAPE:  # Resume the game
                    paused = False

def game_loop():
    """
    Main game loop where the snake moves, checks for collisions, and updates the screen.
    Handles user input, snake movement, food consumption, and game over conditions.
    """
    global SCREEN_WIDTH, SCREEN_HEIGHT, screen

    # Initial game state
    game_over = False   # Flag to indicate if the game is over
    game_close = False  # Flag to indicate if the player has lost but hasn't quit or restarted

    # Initial position of the snake's head (center of the screen)
    x1 = SCREEN_WIDTH / 2
    y1 = SCREEN_HEIGHT / 2

    # Initial change in position (snake starts stationary)
    x1_change = 0
    y1_change = 0

    # List to hold the positions of all segments of the snake
    snake_list = []
    snake_length = 1  # Initial length of the snake

    # Initial random position for the food
    foodx = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
    foody = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK

    while not game_over:

        # Game over loop to handle replay or quit options
        while game_close:
            screen.fill(BLUE)
            message("You Lost! Press C-Play Again or Q-Quit", RED, font_style)
            pygame.display.update()

            # Check for player input to restart or quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:  # Quit the game
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:  # Restart the game
                        game_loop()

        # Handle events like quitting, moving the snake, and pausing the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit the game
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_ESCAPE:  # Pause the game
                    pause_menu()

        # Update the position of the snake's head
        x1 += x1_change
        y1 += y1_change

        # Implement screen wrapping: if the snake goes off one edge, it appears on the opposite side
        if x1 >= SCREEN_WIDTH:
            x1 = 0
        elif x1 < 0:
            x1 = SCREEN_WIDTH - SNAKE_BLOCK

        if y1 >= SCREEN_HEIGHT:
            y1 = 0
        elif y1 < 0:
            y1 = SCREEN_HEIGHT - SNAKE_BLOCK

        # Refresh the screen with the background color
        screen.fill(BLUE)
        
        # Draw the food on the screen
        pygame.draw.rect(screen, GREEN, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])

        # Update the snake's body
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        # Check for collisions with the snake itself (game over condition)
        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_close = True

        # Draw the snake on the screen
        our_snake(SNAKE_BLOCK, snake_list)
        
        # Display the current score
        display_score(snake_length - 1)

        # Update the full display surface to the screen
        pygame.display.update()

        # Check if the snake has eaten the food
        if x1 == foodx and y1 == foody:
            # Generate new food position
            foodx = round(random.randrange(0, SCREEN_WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            foody = round(random.randrange(0, SCREEN_HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK) * SNAKE_BLOCK
            snake_length += 1  # Increase the length of the snake

        # Control the speed of the snake
        clock.tick(SNAKE_SPEED)

    pygame.quit()  # Quit the game
    quit()

def start_menu():
    """
    Displays the start menu where the player can start the game or quit.
    """
    while True:
        screen.fill(BLUE)
        message("Welcome to Snake Game!", GREEN, font_style, -50)  # Display welcome message
        message("Press S to Start or Q to Quit", WHITE, score_font, 50)  # Display start/quit instructions
        pygame.display.update()

        # Check for player input to start or quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit the game
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Start the game
                     game_loop()
                if event.key == pygame.K_q:  # Quit the game
                    pygame.quit()
                    quit()
# Start the game by displaying the start menu
start_menu()
