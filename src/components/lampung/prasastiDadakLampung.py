import pygame
import random

from src.components.gameEntity import GameEntity

class PrasastiDadakLampung(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/components/lampung/prasastiDadak.png", x, y, scale=1)