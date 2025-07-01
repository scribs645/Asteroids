from circleshape import CircleShape
from constants import *

import pygame
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)


    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        asteroid_angle1 = self.velocity.rotate(random_angle)
        asteroid_angle2 = self.velocity.rotate(-random_angle)
        new_asteroid_rad = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_asteroid_rad)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_asteroid_rad)
        asteroid1.velocity = asteroid_angle1 * 1.2
        asteroid2.velocity = asteroid_angle2 * 1.2