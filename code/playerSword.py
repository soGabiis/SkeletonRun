import pygame

from code.entity import Entity
from code.Const import ENTITY_SPEED

class PlayerShot(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.Surface((40, 25), pygame.SRCALPHA)
        self.rect = self.surf.get_rect(topleft=position)


    def move(self):
        pass