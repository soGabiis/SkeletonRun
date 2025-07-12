#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.rect = pygame.Rect(position[0], position[1], 0, 0)
        self.surf = None
        self.health = 1

    @abstractmethod
    def move(self):
        pass
