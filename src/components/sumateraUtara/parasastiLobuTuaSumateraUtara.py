import pygame
import random

from src.components.gameEntity import GameEntity

class PrasastiLobuTuaSumateraUtara(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraUtara/prasastiLobuTua.png", x, y, scale=1)