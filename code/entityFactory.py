#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background
from code.enemy import Enemy
from code.playerSword import PlayerShot


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        if entity_name == 'Level1Bg':
            list_bg = []
            for i in range(7):
                name = f'Level1Bg{i}'
                bg1 = Background(name, (0, 0))
                bg2 = Background(name, (bg1.rect.width, 0))
                list_bg.append(bg1)
                list_bg.append(bg2)
            return list_bg

        elif entity_name == 'Player1':
            from code.player import Player
            return [Player('MoveSkeleton/0', position)]

        elif entity_name == 'Enemy1':  # Golem
            paths = [f'./asset/Golem/Golem{i:02d}.png' for i in range(18)]
            return Enemy('Enemy1', paths, (WIN_WIDTH + 10, 530 - 200))

        elif entity_name == 'Enemy2':  # Wraith
            paths = [f'./asset/Wraith/Wraith{i:02d}.png' for i in range(12)]
            return Enemy('Enemy2', paths, (WIN_WIDTH + 10, 550 - 200))

        elif entity_name == 'Player1Sword':
            return PlayerShot('MoveSkeleton/Slashing_000', position)
