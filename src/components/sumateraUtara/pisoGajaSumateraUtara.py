import pygame
import random

from src.components.gameEntity import GameEntity

class PisoGajaSumateraUtara(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraUtara/pisoGaja.png", x, y, scale=1)