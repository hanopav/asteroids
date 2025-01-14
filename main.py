import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while 0 != 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(0, None, 0)
        """
        print("Starting asteroids!")
        print(f"Screen width: {SCREEN_WIDTH}")
        print(f"Screen height: {SCREEN_HEIGHT}")
        """
    pygame.display.flip()
if __name__ == "__main__":
    main()