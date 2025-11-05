import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y): #I wrongly put in radius here, didn't know it doesn't need radius here! Just like Jet in aircraft doesn't need height only need speed
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)    

    def update(self, dt):
        # sub-classes must override
        self.position += (self.velocity * dt)