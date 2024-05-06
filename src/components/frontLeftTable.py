import pygame
import random

from src.components.gameEntity import GameEntity


class FrontLeftTable(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/components/lobbyFrontLeftTable.png", x, y, 0, 0, 1)
        self.rect.bottomleft = (x, y)