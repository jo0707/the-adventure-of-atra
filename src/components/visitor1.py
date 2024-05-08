
from src.components.gameEntity import GameEntity


class Visitor1(GameEntity):
    def __init__(self, x, y, direction = "down"):
        super().__init__(f"assets/images/char/visitor1/{direction}/0.png", x, y, 0, 0, 8)