import pygame
import random

from src.components.interactableItem import InteractableItem

class KainSongket(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraBarat/kainSongket.png", x, y, scale=1, title="Kain Songket Minangkabau", description="Kain songket Minangkabau adalah salah satu jenis kain songket yang berasal dari daerah Minangkabau, Sumatera Barat, Indonesia. Ini adalah kain tenun tradisional yang dihiasi dengan benang emas atau perak yang diselipkan secara manual ke dalam pola kain.", realImageName="sumateraBarat/kainSongket.png")