import pygame
import random

from src.components.interactableItem import InteractableItem

class Karih(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraBarat/karih.png", x, y, scale=1, title="Karih", description="Karih adalah simbol keberanian dan kejantanan dalam budaya Minangkabau, dan sering kali digunakan dalam tarian perang tradisional yang disebut \"randai\". Selain digunakan untuk keperluan militer, karih juga sering digunakan dalam upacara adat, seperti pernikahan atau pertunjukan seni tradisional.", realImageName="sumateraBarat/karih.png")