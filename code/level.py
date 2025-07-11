#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code import entityFactory
from code.entityFactory import EntityFactory
from code.entity import Entity


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))

    def run(self):
        clock = pygame.time.Clock()

        while True:
            # ⚠️ TRATAR EVENTOS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            # 🔄 Atualizar entidades
            for ent in self.entity_list:
                ent.move()
                self.window.blit(ent.surf, ent.rect)

            # 🔁 Atualizar tela
            pygame.display.flip()

            # ⏱️ Controlar FPS
            clock.tick(60)
