import pygame
import random

from src.components.interactableItem import InteractableItem

class RadenIntan2Lampung(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/lampung/radenIntan2.png", x, y, scale=1,
                         title= 'Lukisan Raden Intan 2',
                         description= 'Raden Intan II, pahlawan nasional dari Lampung, dinobatkan sebagai Ratu pada usia 16 tahun dan langsung memimpin rakyat melawan Belanda. Beliau gigih memobilisasi rakyat, berperang, dan menjalin diplomasi. Meskipun muda, kepemimpinannya luar biasa dan semangatnya pantang menyerah. Kematiannya di tahun 1856 menjadi simbol perlawanan, dan warisannya menginspirasi rakyat Lampung dan Indonesia hingga saat ini.',
                         realImageName='assets/images/real/lampung/radenIntan2.png'
                         )