import pygame
import random

from src.components.gameEntity import GameEntity

class TapisLampung(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/components/lampung/tapis.png", x, y, scale=1)