#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter.font import Font
import pygame
from pygame import Surface, Rect
import random
from code.player import Player

from code.Const import C_SUBMENU, WIN_HEIGHT, C_MENU, EVENT_ENEMY, SPAWN_TIME, WIN_WIDTH, C_GREEN
from code.entityFactory import EntityFactory
from code.entityMediator import entityMediator
from code.playerSword import PlayerShot
from code.Score import Score


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list = EntityFactory.get_entity('Level1Bg')

        player_start_y = 300 - 200  # player height and resizing
        self.entity_list.extend(EntityFactory.get_entity('Player1', (100, player_start_y)))

        self.timeout = 20000
        # Progressive difficulty control
        self.difficulty_timer = 0
        self.spawn_interval = 2000  # initial spawn interval
        self.last_spawn_time = 0
        self.base_enemy_speed = 5  # enemy initial speed
        self.score = 0
        self.score_timer = 0

    def run(self):
        clock = pygame.time.Clock()
        running = True
        pygame.mixer_music.load(f'./asset/613965__bloodpixelhero__retro-arcade-music-5.wav')
        pygame.mixer_music.set_volume(0.3)
        pygame.mixer_music.play(-1)

        while running:
            now = pygame.time.get_ticks()
            self.difficulty_timer += 1

            self.score_timer += 1
            if self.score_timer >= 60:
                self.score += 1
                self.score_timer = 0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        player = next((e for e in self.entity_list if isinstance(e, Player)), None)
                        if player:
                            if player.facing_right:
                                sword_x = player.rect.right - 20
                            else:
                                sword_x = player.rect.left - 40
                            sword_y = player.rect.top + 70
                            sword = EntityFactory.get_entity('Player1Sword', (sword_x, sword_y))
                            self.entity_list.append(sword)

            # Enemy spawn with dynamic range
            if now - self.last_spawn_time > self.spawn_interval:
                self.last_spawn_time = now
                choice = random.choice(('Enemy1', 'Enemy2'))
                enemy = EntityFactory.get_entity(choice)
                enemy.speed = self.base_enemy_speed
                self.entity_list.append(enemy)

            # Increase difficulty every 10 seconds
            if self.difficulty_timer % (60 * 10) == 0:
                self.base_enemy_speed += 0.5
                self.spawn_interval = max(500, self.spawn_interval - 100)

            self.window.fill((0, 0, 0))

            for ent in self.entity_list:
                ent.move()
                if isinstance(ent, Player):
                    self.entity_list.extend(ent.spawned_entities)
                    ent.spawned_entities.clear()
                self.window.blit(ent.surf, ent.rect)

            player = next((e for e in self.entity_list if isinstance(e, Player)), None)
            health = player.health if player else 0

            self.level_text(50, f'Player1 - Health {health}', C_GREEN, (10, 5))
            self.level_text(50, f'Score: {self.score}', C_SUBMENU, (10, 35))
            self.level_text(50, f'fps: {clock.get_fps() :.0f}', C_MENU, (10, WIN_HEIGHT - 75))

            pygame.display.flip()
            clock.tick(60)

            entityMediator.verify_collision(entity_list=self.entity_list)
            entityMediator.verify_health(entity_list=self.entity_list)

            if player is None or player.health <= 0:
                pygame.time.delay(1000)
                # Ask the player's name
                name = self.ask_player_name()
                # Save the score with the name
                Score(self.window).save_score(self.score, name)
                return

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def ask_player_name(self):
        name = ""
        font = pygame.font.SysFont("Lucida Sans Typewriter", 50)
        game_over_font = pygame.font.SysFont("Lucida Sans Typewriter", 80, bold=True)
        input_active = True

        # Load the background image for the Game Over screen
        background_img = pygame.image.load('./asset/Battleground2.png').convert_alpha()
        bg_rect = background_img.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))

        pygame.mixer_music.load(f'./asset/382310__mountain_man__game-over-arcade.wav')
        pygame.mixer_music.play()

        while input_active:
            self.window.fill((0, 0, 0))

            self.window.blit(background_img, bg_rect)

            game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
            game_over_rect = game_over_text.get_rect(center=(WIN_WIDTH // 2, 50))
            self.window.blit(game_over_text, game_over_rect)

            prompt = font.render("Digite seu nome:", True, (255, 255, 255))
            prompt_rect = prompt.get_rect(center=(WIN_WIDTH // 2, 250))
            self.window.blit(prompt, prompt_rect)

            name_surf = font.render(name, True, (0, 255, 0))
            name_rect = name_surf.get_rect(center=(WIN_WIDTH // 2, 320))
            self.window.blit(name_surf, name_rect)

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and name:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    elif len(name) < 12 and event.unicode.isprintable():
                        name += event.unicode

        return name