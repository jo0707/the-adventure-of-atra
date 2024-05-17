import pygame
import random

from src.components.interactableItem import InteractableItem

class PrasastiBungkukLampung(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/lampung/prasastiBungkuk.png", x, y, scale=1)