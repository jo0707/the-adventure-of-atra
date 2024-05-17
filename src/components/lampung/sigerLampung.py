import pygame
import random

from src.components.interactableItem import InteractableItem

class SigerLampung(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/lampung/siger.png", x, y, scale=1)