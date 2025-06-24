import pygame

from constants import *
from player import Player

def main ():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

#initiate classes and stuff
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

#game loop
    while(True):
        dt = game_clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        player.update(dt)    
        
    #rendering/drawing
        screen.fill(color="black")

        player.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()