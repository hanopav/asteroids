import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SPEED
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

        self.image = pygame.Surface((PLAYER_RADIUS * 2, PLAYER_RADIUS * 2), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        self.timer -= dt
        self.timer = max(0, self.timer)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()
        
        self.rect.center = self.position

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * (PLAYER_SPEED * dt)

    def shoot(self):
        if self.timer > 0:
            return    
        direction = pygame.Vector2(0, 1)
        direction = direction.rotate(self.rotation)
        self.velocity = direction * PLAYER_SHOOT_SPEED 
        shot = Shot(self.position.x, self.position.y, self.velocity)
        self.timer = PLAYER_SHOOT_COOLDOWN