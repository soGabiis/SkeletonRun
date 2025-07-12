#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, E_SPEED
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.surf = pygame.image.load('./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(topleft=position)


    def move(self, ):
        self.rect.centerx -= E_SPEED[self.name]
        if self.rect.right <= 0:
            self.rect.left += self.rect.width * 2
