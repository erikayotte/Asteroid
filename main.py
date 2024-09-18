# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()
# Set the width and height of the screen

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Loop repeater
done = False

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

#	def main():
#		print("Starting asteroids!")
#		print(f"Screen width:", SCREEN_WIDTH)
#		print(f"Screen height:", SCREEN_HEIGHT)

    screen.fill(BLACK)
# --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()

if __name__ == "__main__":
    main()
