import pygame
import time
import random

pygame.init()

# Set up the game window
window_width, window_height = 640, 480
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Snake Game")

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Snake properties
snake_block = 20
snake_speed = 15

# Initialize snake position
snake_x, snake_y = window_width // 2, window_height // 2
snake_x_change, snake_y_change = 0, 0
snake_list = []
snake_length = 1

# Initialize food position
food_x, food_y = random.randrange(0, window_width - snake_block, snake_block), random.randrange(0, window_height - snake_block, snake_block)

# Game loop
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_block
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_block
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_block
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_block
                snake_x_change = 0

    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        food_x, food_y = random.randrange(0, window_width - snake_block, snake_block), random.randrange(0, window_height - snake_block, snake_block)
        snake_length += 1

    # Update snake list
    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for self-collision
    for segment in snake_list[:-1]:
        if segment == snake_head:
            game_over = True

    # Draw snake and food
    window.fill(black)
    for segment in snake_list:
        pygame.draw.rect(window, green, [segment[0], segment[1], snake_block, snake_block])
    pygame.draw.rect(window, red, [food_x, food_y, snake_block, snake_block])

    pygame.display.update()
    time.sleep(0.1)

pygame.quit()

