import pygame
import random

from src.components.interactableItem import InteractableItem

class PrasastiBatuganaSumateraUtara(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraUtara/prasastiBatugana.png", x, y, scale=1,
                         title= 'Prasasti Batugana I',
                         description= 'Prasasti Batugana I atau juga bisa disebut dengan Prasasti Panai, adalah sebuah prasasti yang bertuliskan aksara Kawi dan berbahaya Melayu Kuno, yang ditemukan di sekitar Candi Bahal I, di Desa Bahal, Kecamatan Portibi, Kabupaten Padang Lawas Utara, Provinsi Sumatera Utara.',
                         realImageName='sumateraUtara/prasastiBatugana.png')