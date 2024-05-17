
from src.components.interactableItem import InteractableItem

class WallMap(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/wallMap.png", x, y, 0, 0, 1)