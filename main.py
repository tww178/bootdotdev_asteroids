import sys
import pygame 
from circleshape import CircleShape #This was not needed in the suggested solution
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    # To add all instances of a Player to two groups, group_a (updatable) and group_b (drawable) in this example, we add a class variable (or static field) called containers to the class just like so (with literally this one line, you don't need to bother with adding this field to the class declaration):
    AsteroidField.containers = (updatable)
    Asteroid.containers = (asteroids, updatable, drawable) #I am starting to realise how these groupings works but maybe not completely
    Shot.containers = (shots, updatable, drawable) #Set up a new group in your initialization code and make it contain all of your shots.
    Player.containers = (updatable, drawable)
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        updatable.update(dt)
        for a in asteroids:
            if a.check_collision(player):
                print("Game over!")
                sys.exit()
            for b in shots:
                if b.check_collision(a):
                    a.split()
                    b.kill()

        for d in drawable:
            d.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
