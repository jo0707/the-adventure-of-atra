import pygame
import random

from src.components.interactableItem import InteractableItem

class KainUlosSumateraUtara(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraUtara/kainUlos.png", x, y, scale=1,
                         title= 'Kain Tenun Ulos',
                         description= 'Kain tenun Ulos adalah kain tenun khas suku Batak. ulos mempunyai fungsi dan arti yang sangat penting. Kain Tenun Ulos digunakan di berbagai upacara adat seperti kelahiran, pernikahan, kematian dan ritual lainnya.',
                         realImageName='sumateraUtara/kainUlos.png')