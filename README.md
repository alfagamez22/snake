# Snake Game

A classic Snake game implemented in Python using the Pygame library.

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Requirements](#requirements)
4. [Installation](#installation)
5. [How to Play](#how-to-play)
6. [Game Controls](#game-controls)
7. [Code Structure](#code-structure)
8. [Customization](#customization)
9. [Future Improvements](#future-improvements)

## Introduction

This is a Python implementation of the classic Snake game using the Pygame library. The player controls a snake that moves around the screen, eating food to grow longer. The game ends if the snake collides with itself.

## Features

- Start menu
- Pause functionality
- Score display
- Game over screen with replay option
- Screen wrapping (snake appears on opposite side when it reaches the edge)
- Increasing difficulty as the snake grows longer

## Requirements

- Python 3.x
- Pygame library

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install Pygame by running:
    pip install pygame
3. Download the game script (`snake_game.py`).

## How to Play

1. Run the script:
    python snake.py
2. In the start menu, press 'S' to start the game or 'Q' to quit.
3. Control the snake using arrow keys to eat the food (green squares).
4. Avoid colliding with the snake's own body.
5. The game ends when the snake collides with itself.
6. At game over, press 'C' to play again or 'Q' to quit.

## Game Controls

- Arrow keys: Move the snake
- ESC: Pause the game
- In menus:
- S: Start game
- C: Play again (after game over)
- Q: Quit game
- R: Restart (in pause menu)

## Code Structure

- `start_menu()`: Displays the start menu
- `game_loop()`: Main game logic
- `pause_menu()`: Handles game pausing
- `our_snake()`: Draws the snake on the screen
- `message()`: Displays messages on the screen
- `display_score()`: Shows the current score

## Customization

You can easily customize the game by modifying the constants at the beginning of the script:

- `SCREEN_WIDTH` and `SCREEN_HEIGHT`: Change the game window size
- `SNAKE_BLOCK`: Adjust the size of the snake and food
- `SNAKE_SPEED`: Modify the game speed
- Color constants: Change the game's color scheme

## Future Improvements

- Add sound effects
- Implement a high score system with sound fx
- Implement sound fx whenever user reaches 10th point score
- Create levels with obstacles
- Improve graphics
