

from src.components.interactableItem import InteractableItem

class SumaterStatue(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/sumateraStatue.png", x, y, 240, 300,
            title="Patung Sumatera", 
            description="Patung Sumatera",
        )                 
        self.rect.center = (x, y)