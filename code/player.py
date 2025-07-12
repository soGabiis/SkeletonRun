#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.entity import Entity
from code.Const import WIN_WIDTH, E_SPEED
from code.playerSword import PlayerShot


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        self.facing_right = True

        self.invulnerable = False
        self.invulnerable_timer = 0

        # Animations move, run and jump
        self.jump_sound = pygame.mixer.Sound('./asset/380471__acebrian__jump.wav')
        self.jump_sound.set_volume(0.4)

        self.idle_frames = [
            pygame.transform.scale(
                pygame.image.load(f'./asset/MoveSkeleton/{i}.png').convert_alpha(),
                (200, 200)
            ) for i in range(24)
        ]

        self.run_frames = [
            pygame.transform.scale(
                pygame.image.load(f'./asset/MoveSkeleton/Running_0{i}.png').convert_alpha(),
                (200, 200)
            ) for i in range(6)
        ]

        self.jump_frames = [
            pygame.transform.scale(
                pygame.image.load(f'./asset/MoveSkeleton/Jump Start_0{i}.png').convert_alpha(),
                (200, 200)
            ) for i in range(6)
        ]

        self.attack_frames = [
            pygame.transform.scale(
                pygame.image.load(f'./asset/MoveSkeleton/Slashing_{i:03}.png').convert_alpha(),
                (200, 200)
            ) for i in range(12)
        ]

        self.attack_pressed = False

        self.spawned_entities = []
        self.surf = self.idle_frames[0]
        self.rect = self.surf.get_rect(topleft=position)
        self.mask = pygame.mask.from_surface(self.surf)

        # Physical
        self.speed = E_SPEED['Player1']
        self.vel_y = 0
        self.gravity = 1
        self.jump_strength = -20
        self.on_ground = True
        self.ground_y = 550

        self.is_running = False
        self.is_jumping = False
        self.is_attacking = False
        self.attack_frame = 0

        # animation
        self.current_frame = 0
        self.frame_timer = 0
        self.frame_delay = 5

        # life
        self.health = 2  # Number of player lives

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and not self.is_attacking:
            self.is_attacking = True
            self.attack_frame = 0
            from code.entityFactory import EntityFactory
            sword_x = self.rect.right - 20
            sword_y = self.rect.top + 70
            sword = EntityFactory.get_entity('Player1Sword', (sword_x, sword_y))
            self.spawned_entities.append(sword)

        elif not keys[pygame.K_SPACE]:
            self.attack_pressed = False

        # Movement and Physics
        if keys[pygame.K_UP] and self.on_ground:
            self.vel_y = self.jump_strength
            self.on_ground = False
            self.is_jumping = True
            self.jump_sound.play()

        self.is_running = False
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
            self.is_running = True
        if keys[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.rect.x += self.speed
            self.is_running = True

        self.vel_y += self.gravity
        self.rect.y += self.vel_y
        if self.rect.bottom >= self.ground_y:
            self.rect.bottom = self.ground_y
            self.vel_y = 0
            self.on_ground = True
            self.is_jumping = False

        # Animations
        self.frame_timer += 1
        if self.frame_timer >= self.frame_delay:
            self.frame_timer = 0
            self.current_frame += 1

            if self.is_attacking:
                if self.attack_frame < len(self.attack_frames):
                    self.surf = self.attack_frames[self.attack_frame]
                    self.update_mask()
                    self.attack_frame += 1
                else:
                    self.is_attacking = False
                    self.attack_frame = 0

            elif self.is_jumping:
                self.current_frame %= len(self.jump_frames)
                self.surf = self.jump_frames[self.current_frame]
                self.update_mask()

            elif self.is_running:
                self.current_frame %= len(self.run_frames)
                self.surf = self.run_frames[self.current_frame]
                self.update_mask()

            else:
                self.current_frame %= len(self.idle_frames)
                self.surf = self.idle_frames[self.current_frame]
                self.update_mask()

            # Temporary invulnerability
            if self.invulnerable:
                self.invulnerable_timer -= 1
                if self.invulnerable_timer <= 0:
                    self.invulnerable = False