import pygame
import random

from src.components.gameEntity import GameEntity

class BajuBatak(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraUtara/bajuBatak.png", x, y, scale=1)