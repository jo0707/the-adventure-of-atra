import pygame
import random

from src.components.interactableItem import InteractableItem

class PrasastiDadakLampung(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/lampung/prasastiDadak.png", x, y, scale=1,
                         title= 'Prasasti Dadak',
                         description= 'Prasasti Dadak ditemukan di Dusun Dadak Desa Tebing, Kecamatan Perwakilan Melintang, Lampung Timur, pada tahun 1994. Terdiri dari 14 baris tulisan huruf Jawa Kuno dengan Bahasa Melayu. Isinya menjelaskan mengenai peminjaman tanah selama 100 tahun untuk pendirian bangunan suci.',
                         realImageName='lampung/prasastiDadak.png')