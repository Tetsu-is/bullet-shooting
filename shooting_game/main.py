import pyxel

from enum import Enum


class GameMode(Enum):
    MENU = 0
    PLAYING = 1
    GAME_OVER = 2


class GameManager:
    def __init__(self):
        self.game_mode = GameMode.MENU
        pass


class Player:
    def __init__(self):
        pass


class Enemy:
    def __init__(self):
        pass


class Bullet:
    def __init__(self):
        pass


class Aim:
    def __init__(self):
        pass


class App:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


App()
