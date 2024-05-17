
from src.components.interactableItem import InteractableItem

class LogoLampung(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/logoLampung.png", x, y, 0, 0, 1)