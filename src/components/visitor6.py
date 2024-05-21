
from src.components.gameEntity import GameEntity


class Visitor6(GameEntity):
    def __init__(self, x, y, direction = "down"):
        super().__init__(f"assets/images/char/visitor6/{direction}/0.png", x, y, 0, 0, 0.2)