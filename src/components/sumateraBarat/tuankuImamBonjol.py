import pygame
import random

from src.components.interactableItem import InteractableItem

class TuankuImamBonjol(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraBarat/tuankuImamBonjol.png", x, y, scale=1, 
                         title="Tuanku Imam Bonjol", description="Tempat Lahir : Bonjol, Luhak Agam, Pagaruyung. Tahun Lahir: 1772. Tempat Wafat : Lotta, Pineleng, Minahasa. Tanggal Wafat	: 6 November 1864. Imam Bonjol, atau Muhammad Syahab, adalah seorang pemimpin perlawanan terhadap penjajahan Belanda di Minangkabau, Sumatera Barat, pada abad ke-19. Dilahirkan pada tahun 1772 di Tanjung Gadang, Sumatera Barat, Bonjol tumbuh menjadi seorang ulama yang dihormati dan memimpin perang gerilya melawan Belanda, memproklamasikan perlawanan pada tahun 1824. Meskipun tertangkap dan diasingkan ke Pulau Ambon pada tahun 1837, perjuangannya tetap dihormati sebagai salah satu pahlawan nasional Indonesia.", realImageName="sumateraBarat/tuankuImamBonjol.png")