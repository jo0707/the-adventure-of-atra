import pygame
import random

from src.components.interactableItem import InteractableItem

class JamGadang(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraBarat/jamGadang.png", x, y, scale=1, title="Jam Gadang", description="Jam Gadang adalah menara jam yang menjadi penanda atau ikon Kota Bukittinggi, Sumatera Barat, Indonesia. Menara jam ini menjulang setinggi 27 meter dan diresmikan pembangunannya pada 25 Juli 1927. Terdapat jam berukuran besar berdiameter 80 cm di empat sisi menara sehingga dinamakan Jam Gadang, sebutan bahasa Minangkabau yang berarti \"jam besar\".", realImageName="sumateraBarat/jamGadang.png")