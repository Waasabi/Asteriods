# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import *
def main():
  
  pygame.init()
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  clock = pygame.time.Clock()
  dt=0 
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  
  asteroids = pygame.sprite.Group()
  updatable= pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  Player.containers = (updatable,drawable)
  Asteroid.containers = (asteroids,updatable,drawable)
  AsteroidField.containers = (updatable)
  Player(x,y)
  AsteroidField()
  
  while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60)/1000

        for MP in updatable:
            MP.update(dt)
        screen.fill("black")
        
        for MP in drawable:
            MP.draw(screen)
        pygame.display.flip()
        
        
if __name__ == "__main__":
    main()