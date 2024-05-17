from src.components.interactableItem import InteractableItem

class GajahStatue(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/gajahStatue.png", x, y, 240, 300,
            title="Patung Gajah", 
            description="Patung Gajah",
        )                 
        self.rect.center = (x, y)