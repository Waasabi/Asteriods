# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *

def main():
  
  pygame.init()
  x = SCREEN_WIDTH / 2
  y = SCREEN_HEIGHT / 2
  clock = pygame.time.Clock()
  dt=0 
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  player1 = player(x,y)
  while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        player1.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000
        
if __name__ == "__main__":
    main()