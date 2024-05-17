from src.components.interactableItem import InteractableItem

class BadakStatue(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/badakStatue.png", x, y, 240, 300,
            title="Patung Badak", 
            description="Patung Badak",
        )                 
        self.rect.center = (x, y)