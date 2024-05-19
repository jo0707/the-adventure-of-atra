import pygame
import random

from src.components.interactableItem import InteractableItem

class SisingamangaradjaSumateraUtara(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraUtara/sisingamangaradja.png", x, y, scale=1,
                         title= 'Lukisan Pahlawan Sisingamangaradja XII',
                         description= 'Sisingamanaradja atau nama asli nya  diangkat sebagai Pahlawan Nasional Indonesia pada tanggal 9 November 1961. Perjuangannya melawan Belanda adalah perjuangan menentang pemaksaan penyebaran ajaran agama Kristen kepada rakyat Batak. Hal ini disebabkan karena Sisingamangaradja khawatir tindakan ini akan mengikis tradisi dan kepercayaan animisme rakyat Batak.',
                         realImageName='sumateraUtara/sisingamangaradja.png')