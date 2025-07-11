#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.background import Background
from code.player import Player


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
            return [Player('MoveSkeleton/0', position)]
