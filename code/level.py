#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter.font import Font

import pygame
from pygame import Surface, Rect

from code.Const import COLOR_SUBMENU, WIN_HEIGHT, COLOR_MENU
from code.entityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = EntityFactory.get_entity('Level1Bg')
        self.timeout = 20000

    def run(self):
        clock = pygame.time.Clock()
        running = True
        pygame.mixer_music.load(f'./asset/815460__josefpres__piano-loops-135-efect-4-octave-long-loop-120-bpm.wav')
        pygame.mixer_music.play(-1)

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            self.window.fill((0, 0, 0))

            for ent in self.entity_list:
                ent.move()
                self.window.blit(ent.surf, ent.rect)

            self.level_text(50, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_MENU, (10, 5))
            self.level_text(50, f'fps: {clock.get_fps() :.0f}', COLOR_MENU, (10, WIN_HEIGHT - 75))
            self.level_text(50, f'entidades: {len(self.entity_list)}', COLOR_MENU, (10, WIN_HEIGHT - 45))
            pygame.display.flip()
            clock.tick(60)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
