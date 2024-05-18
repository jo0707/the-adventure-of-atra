import pygame
import random

from src.components.interactableItem import InteractableItem

class SigerLampung(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/lampung/siger.png", x, y, scale=1,
                         title= 'Siger Lampung',
                         description= 'Siger Lampung, mahkota pengantin wanita yang terbuat dari kuningan berlapis emas, melambangkan keanggunan, kesuburan, kewibawaan, dan kemuliaan. Bentuk segitiga menjulang dengan banyak cabang, dihiasi bunga, burung, dan tanduk kerbau, dibuat dengan teknik tempa dan ukir rumit. Ada tiga jenis Siger Lampung: Patah (delapan cabang), Seman (sembilan cabang), dan Bejul (banyak ornamen). Siger Lampung bukan hanya perhiasan, tetapi warisan budaya yang dilestarikan..',
                         realImageName='assets/images/real/lampung/siger.png')
