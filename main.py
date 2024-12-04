import pygame
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    pygame.init()
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        loop(screen, player)
        dt = clock.tick(60) / 1000

def loop(screen: pygame.Surface, player: Player):
    screen.fill("black")
    player.draw(screen)

    pygame.display.flip()

if __name__ == "__main__":
    main()