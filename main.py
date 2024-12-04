import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    print("Starting asteroids!")
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        loop(screen, dt, player, updatable, drawable, asteroids)
        dt = clock.tick(60) / 1000

def loop(screen: pygame.Surface, dt: float, player: Player,
         updatable: pygame.sprite.Group, 
         drawable: pygame.sprite.Group,
         asteroids: pygame.sprite.Group):

    screen.fill("black")

    for sprite in updatable:
        sprite: pygame.sprite.Sprite
        sprite.update(dt)

    for asteroid in asteroids:
        asteroid: Asteroid
        if asteroid.check_collision(player):
            print("Game over!")
            sys.exit()
    
    for sprite in drawable:
        sprite: pygame.sprite.Sprite
        sprite.draw(screen)

    pygame.display.flip()

if __name__ == "__main__":
    main()