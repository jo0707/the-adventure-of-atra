import pygame
import random

from src.components.gameEntity import GameEntity

class RadenIntan2Lampung(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/components/lampung/radenIntan2.png", x, y, scale=1)