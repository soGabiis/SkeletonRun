#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.menu import Menu
from code.level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption("Parallax Game")

    def run(self):
        while True:
            menu = Menu(self.window)
            choice = menu.run()

            if choice == MENU_OPTION[0]:
                level = Level(self.window, 'Level1', choice)
                level.run()
            elif choice == MENU_OPTION[2]:
                pygame.quit()
                quit()

