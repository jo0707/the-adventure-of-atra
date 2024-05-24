

from src.components.interactableItem import InteractableItem

class SumaterStatue(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraStatue.png", x, y, 240, 300,
            title="Pulau Sumatera", 
            description="""Pulau Sumatra adalah pulau keenam terbesar di dunia yang terletak di Indonesia, dengan luas 473.481 km^2. Penduduk yang tinggal di pulau ini sekitar 57 juta jiwa. Pulau ini dikenal pula dengan nama lain yaitu Pulau Percha, Andalas, atau Suwarnadwipa (bahasa Sanskerta, berarti "pulau emas").""",
            realImageName="sumateraStatue.png"
        )                 
        self.rect.center = (x, y)