import pygame
import random

from src.components.interactableItem import InteractableItem

class PisoGajaSumateraUtara(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraUtara/pisoGaja.png", x, y, scale=1,
                         title= 'Piso Gaja Dompak',
                         description= 'Senjata ini digunakan oleh pahlawan nasional Indonesia Sisingamangaradja XII. Senjata ini dipergunakan ketika melakukan perlawanan terhadap penjajah Belanda di tanah Batak.',
                         realImageName='assets/images/real/sumateraUtara/pisoGaja.png')