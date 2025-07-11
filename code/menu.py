#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, COLOR_MENU, MENU_OPTION, COLOR_SUBMENU


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/Battleground3.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/815081__josefpres__piano-loops-133-efect-4-octave-long-loop-120-bpm.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(200, "Skeleton", COLOR_MENU, ((WIN_WIDTH / 2), 70))
            self.menu_text(200, "Run", COLOR_MENU, ((WIN_WIDTH / 2), 200))

            for i in range(len(MENU_OPTION)):
                self.menu_text(100, MENU_OPTION[i], COLOR_SUBMENU, ((WIN_WIDTH / 2), 720 + 100 * i))

            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # End Pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="8-Bit-Madness", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)