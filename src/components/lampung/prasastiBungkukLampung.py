import pygame
import random

from src.components.gameEntity import GameEntity

class PrasastiBungkukLampung(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/components/lampung/prasastiBungkuk.png", x, y, scale=1)