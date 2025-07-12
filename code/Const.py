# C
import pygame

COLOR_MENU = (173, 218, 255)
COLOR_SUBMENU = (255, 255, 255)

# E
EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 3,
    'Level1Bg4': 4,
    'Level1Bg5': 5,
    'Level1Bg6': 6,
    'Player1': 3,
    'Enemy1': 7,
    'Enemy2': 6,
}

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Player1': 300,
    'Player1Sword': 1,
    'Enemy1': 1,
    'Enemy2': 1,
    }

# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

# S
SPAWN_TIME = 3000

# W
WIN_WIDTH = 1920
WIN_HEIGHT = 1080

# Y
COLOR_SELECTION = (234, 168, 77)
