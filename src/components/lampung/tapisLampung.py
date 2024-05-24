import pygame
import random

from src.components.interactableItem import InteractableItem

class TapisLampung(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/lampung/tapis.png", x, y, scale=1,
                         title= 'Kain Tapis',
                         description= 'Kain Tapis adalah pakaian wanita suku Lampung yang berbentuk sarung. Kain ini terbuat dari tenun benang kapas yang bermotif atau hiasan sugi, benang perak atau emas yang dibuat dengan sistem sulam. Kain Tapis biasa dikenakan saat upacara-upacara adat.',
                         realImageName='lampung/tapis.png')