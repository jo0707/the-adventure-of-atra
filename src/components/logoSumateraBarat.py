
from src.components.interactableItem import InteractableItem

class LogoSumateraBarat(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/logoSumbar.png", x, y, 0, 0, 1)