#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import ENTITY_SPEED
from code.entity import Entity


class Enemy(Entity):
    def __init__(self, enemy_type: str, frame_paths: list[str], position: tuple):
        super().__init__(enemy_type, position)

        self.enemy_type = enemy_type
        self.frames = []

        for path in frame_paths:
            img = pygame.image.load(path).convert_alpha()
            # Redimensiona mantendo proporção
            ratio = 200 / img.get_height()
            width = int(img.get_width() * ratio)
            img = pygame.transform.scale(img, (width, 200))
            img = pygame.transform.flip(img, True, False)  # Espelha para esquerda
            self.frames.append(img)

        self.current_frame = 0
        self.frame_timer = 0
        self.frame_delay = 5

        self.surf = self.frames[0]
        self.rect = self.surf.get_rect(topleft=position)

        self.mask = pygame.mask.from_surface(self.surf)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

        self.frame_timer += 1
        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.surf = self.frames[self.current_frame]
            self.update_mask()


    def speed(self):
        from code.Const import ENTITY_SPEED
        return ENTITY_SPEED[self.enemy_type]
