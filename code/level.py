#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter.font import Font
import pygame
from pygame import Surface, Rect
import random
from code.player import Player

from code.Const import COLOR_SUBMENU, WIN_HEIGHT, COLOR_MENU, EVENT_ENEMY, SPAWN_TIME
from code.entityFactory import EntityFactory
from code.entityMediator import entityMediator
from code.playerSword import PlayerShot


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = EntityFactory.get_entity('Level1Bg')

        player_start_y = 300 - 200  # altura redimensionado do player
        self.entity_list.extend(EntityFactory.get_entity('Player1', (100, player_start_y)))

        self.timeout = 20000
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

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

                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        # Encontra o player na lista
                        player = next((e for e in self.entity_list if isinstance(e, Player)), None)
                        if player:
                            sword_x = player.rect.right - 20
                            sword_y = player.rect.top + 70
                            sword = EntityFactory.get_entity('Player1Sword', (sword_x, sword_y))
                            self.entity_list.append(sword)

            self.window.fill((0, 0, 0))

            for ent in self.entity_list:
                ent.move()

                if isinstance(ent, Player):
                    self.entity_list.extend(ent.spawned_entities)
                    ent.spawned_entities.clear()

                self.window.blit(ent.surf, ent.rect)

            self.entity_list = [ent for ent in self.entity_list if not isinstance(ent, PlayerShot)]

            self.level_text(50, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_MENU, (10, 5))
            self.level_text(50, f'fps: {clock.get_fps() :.0f}', COLOR_MENU, (10, WIN_HEIGHT - 75))
            self.level_text(50, f'entidades: {len(self.entity_list)}', COLOR_MENU, (10, WIN_HEIGHT - 45))

            pygame.display.flip()
            clock.tick(60)

            # Checa colisões e saúde das entidades
            entityMediator.verify_collision(entity_list=self.entity_list)
            entityMediator.verify_health(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
