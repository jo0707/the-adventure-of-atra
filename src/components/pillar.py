import pygame
import random

from src.components.gameEntity import GameEntity


class Pillar(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/components/pillar.png", x, y, 0, 0, 1)