import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def checkCollision(self,other):
        totalradius = self.radius + other.radius
        distance=pygame.Vector2(self.position).distance_to(pygame.Vector2(other.position))
        if ( distance <= totalradius):
            return True
        else:
            return False

        