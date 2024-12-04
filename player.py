import pygame
from constants import PLAYER_RADIUS, SHOT_RADIUS, PLAYER_SHOOT_COOLDOWN
from constants import PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):

    def __init__(self, x: int, y: int):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.__cooldown = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen: pygame.Surface):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def update(self, dt):
        self.__cooldown -= dt

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)
        
        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt
    
    def move(self, dt: float):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if (self.__cooldown > 0):
            return 
        shot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.__cooldown = PLAYER_SHOOT_COOLDOWN