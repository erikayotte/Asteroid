import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)  
 
    # Override the draw method
    def draw(self, screen):
        print(f"Drawing asteroid with radius: {self.radius}")
        pygame.draw.circle(screen, (255, 255, 255), (self.position), self.radius, 2)

    # Override the update method
    def update(self, dt):
        self.position += self.velocity * dt

    #splitting the rocks
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            new_x, new_y = self.position.x, self.position.y
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_vector1 = self.velocity.rotate(random_angle) * 1.2
            new_vector2 = self.velocity.rotate(-random_angle) * 1.2
            new_asteroid1 = Asteroid(new_x, new_y, new_radius)
            new_asteroid2 = Asteroid(new_x, new_y, new_radius)
            new_asteroid1.velocity = new_vector1
            new_asteroid2.velocity = new_vector2
