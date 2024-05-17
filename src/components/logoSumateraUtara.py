
from src.components.interactableItem import InteractableItem

class LogoSumateraUtara(InteractableItem):
    def __init__(self, x, y):
        super().__init__("assets/images/components/logoSumut.png", x, y, 0, 0, 1)