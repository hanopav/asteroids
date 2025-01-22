import pygame
from constants import *
from player import Player, Shot
from AsteroidField import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    shots = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables,)
    Shot.containers = (updatables, drawables, shots)
    
    player = Player(x, y)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0), None, 0)
        for updatable in updatables:
            updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collision_check(player):
                print("Game over!")
                exit()
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collision_check(shot):
                    asteroid.split()
                    shot.kill()
        for drawable in drawables:
            drawable.draw(screen)
       
        dt = clock.tick(60) / 1000
        pygame.display.flip()

if __name__ == "__main__":
    main()