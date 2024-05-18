import pygame
import random

from src.components.interactableItem import InteractableItem

class PrasastiBungkukLampung(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/lampung/prasastiBungkuk.png", x, y, scale=1,
                         title= 'Prasasti Bungkuk',
                         description= 'Prasasti ini berisi 13 baris Huruf Pallawa dengan Bahasa Melayu Kuno ini masih bercerita tentang kejayaan Kerajaan Sriwijaya yang akan mengutuk siapapun rakyatnya yang dianggap tidak tunduk kepada pemerintahan.',
                         realImageName='assets/images/real/lampung/prasastiBungkuk.png')