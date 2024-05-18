import pygame
import random

from src.components.interactableItem import InteractableItem

class BajuBatakSumateraUtara(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraUtara/bajuBatak.png", x, y, scale=1,
                         title= 'Pakaian Adat Batak Toba',
                         description= 'Pakaian Adat Batak Toba terbuat dari kain ulos atau kain tenun tradisional, mulai dari bagian atas sampai bawah. Pakaian adat pria bagian atas disebut ampe-ampe dan bagian bawah disebut singkot. sementara untuk perempuan, bagian atas berupa hoba-hoba dan bagian bawah adalah haen. Pakaian adat ini digunakan untuk upacara adat, pernikahan dan pesta  syukuran.',
                         realImageName='assets/images/real/sumateraUtara/pakaianAdat.png')