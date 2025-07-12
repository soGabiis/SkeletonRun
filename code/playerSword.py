import pygame
from code.entity import Entity

class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.Surface((40, 25), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(topleft=position)

        self.lifetime = 0  # contador de frames que a espada existe

    def move(self):
        self.lifetime += 1
        if self.lifetime > 3:
            self.health = 0  # remove a espada após 3 frames