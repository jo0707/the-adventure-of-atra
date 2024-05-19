

from src.components.interactableItem import InteractableItem

class SumaterStatue(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraStatue.png", x, y, 240, 300,
            title="Patung Sumatera", 
            description="""Sumatra (bentuk tidak baku: Sumatera) adalah pulau keenam terbesar di dunia yang terletak di Indonesia, dengan luas 473.481 km². Penduduk yang tinggal di pulau ini sekitar 57.940.351 jiwa (sensus 2018)[2]. Pulau ini dikenal pula dengan nama lain yaitu Pulau Percha, Andalas, atau Suwarnadwipa (bahasa Sanskerta, berarti "pulau emas").""",
        )                 
        self.rect.center = (x, y)