import pygame
import sys

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main ():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

#initiate classes and stuff
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()
    dt = 0

    #declare groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    AsteroidField.containers = (updateable)
    Asteroid.containers = (asteroids, updateable, drawable)
    Shot.containers = (shots, updateable, drawable)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroidfield = AsteroidField()

#game loop
    while(True):
    # clock and quit events
        dt = game_clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
    #updates    
        updateable.update(dt)

    #check for collsions
        #player collsions
        for asteroid in asteroids:
            if player.check_collision(asteroid):
                print("Game over!")
                sys.exit()

        #bullet collisions
        for shot in shots:
            for asteroid in asteroids:
                if shot.check_collision(asteroid):
                    asteroid.split()
                    shot.kill()
        
    #rendering/drawing
        screen.fill(color="black")

        for gameobject in drawable:
            gameobject.draw(screen)
        
        pygame.display.flip()


if __name__ == "__main__":
    main()