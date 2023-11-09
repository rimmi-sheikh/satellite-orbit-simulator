import sys
import os
import math

# Determine the Pygame path relative to this script
pygame_path = os.path.join(os.path.dirname(__file__), 'pygame')
sys.path.insert(0, pygame_path)

import pygame

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 150  # Radius of the orbit
SPEED = 1  # Angular speed (radians per frame)

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Satellite Orbit Simulator")

# Main loop
running = True
angle = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(BLACK)

    # Calculate the position of the satellite
    x = CENTER[0] + RADIUS * math.cos(angle)
    y = CENTER[1] + RADIUS * math.sin(angle)

    # Draw the Earth
    pygame.draw.circle(screen, WHITE, CENTER, RADIUS, 2)

    # Draw the satellite
    pygame.draw.circle(screen, WHITE, (int(x), int(y)), 10)

    # Update the display
    pygame.display.update()

    # Increase the angle
    angle += SPEED

    # Control the frame rate
    pygame.time.delay(10)

# Quit Pygame
pygame.quit()
