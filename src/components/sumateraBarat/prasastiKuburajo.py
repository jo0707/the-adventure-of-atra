import pygame
import random

from src.components.interactableItem import InteractableItem

class PrasastiKuburajo(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraBarat/prasastiKuburajo.png", x, y, scale=1, title="Prasasti Kuburajo II", description="Prasasti Kuburajo II adalah salah satu prasasti peninggalan dari masa Raja Adityawarman. Di komplek prasasti ini, ada tiga buah batu berjajar yang ukurannya besar, disusun seperti sandaran tempat duduk untuk rapat para penghulu/kepala adat di masa lalu.", realImageName="sumateraBarat/prasastiKuburajo.png")