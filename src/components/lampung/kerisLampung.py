import pygame
import random

from src.components.interactableItem import InteractableItem

class KerisLampung(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/lampung/keris.png", x, y, scale=1,
                         title= 'Keris Lampung',
                         description= 'Keris Lampung, atau Terapang, terkenal dengan bilahnya yang bengkok dan ukirannya yang rumit. Keris ini bukan hanya senjata, tapi juga memiliki nilai spiritual dan budaya tinggi, dan sering diwariskan turun-temurun. Jenis keris Lampung yang terkenal adalah Keris Kijang milik Raden Intan II. Keris Lampung dapat ditemukan di berbagai museum di Lampung, seperti Museum Negeri Lampung dan Museum Raden Intan II.',
                         realImageName='assets/images/real/lampung/kerisLampung.png'
                         )