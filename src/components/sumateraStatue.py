import pygame
import random

from src.components.gameEntity import GameEntity


class SumaterStatue(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraStatue.png", x, y, 240, 300)
        self.rect.center = (x, y)