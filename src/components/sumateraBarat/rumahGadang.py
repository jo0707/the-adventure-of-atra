import pygame
import random

from src.components.interactableItem import InteractableItem

class RumahGadang(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraBarat/rumahGadang.png", x, y, scale=1, title="Rumah Gadang", description="Rumah Gadang adalah rumah adat yang khas dari masyarakat Minangkabau di Sumatera Barat, Indonesia. Rumah ini memiliki ciri khas atapnya yang melengkung ke atas di kedua ujungnya, menyerupai tanduk kerbau. Rumah Gadang bukan hanya sekadar tempat tinggal, tetapi juga merupakan simbol identitas dan kebanggaan bagi masyarakat Minangkabau. Rumah gadang memiliki struktur yang kokoh dan seringkali dihiasi dengan ukiran yang indah.\nBahan Bangunan 	: Kayu dan Bambu\nFungsi 		: Kegiatan adat, pertemuan keluarga, upacara adat, pernikahan.", realImageName="sumateraBarat/rumahGadang.png")