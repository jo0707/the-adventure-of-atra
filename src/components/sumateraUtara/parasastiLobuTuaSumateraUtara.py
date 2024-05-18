import pygame
import random

from src.components.interactableItem import InteractableItem

class PrasastiLobuTuaSumateraUtara(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraUtara/prasastiLobuTua.png", x, y, scale=1,
                         title= 'Prasasti Lobu Tua',
                         description= 'Prasasti Lobu Tua adalah sebuah prasasti dalam bahasa Tamil, yang ditemukan pada tahun 1873 di Desa Lobu Tua, Kecmatan Andam Dewi, Kabupaten Tapanuli Tengah, Sumatera Utara. Prasati ini berangka tahun Saka 1010 atau 1088 Masehi.',
                         realImageName='assets/images/real/sumateraUtara/prasastiLobuTua.png')