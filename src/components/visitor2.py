
from src.components.gameEntity import GameEntity


class Visitor2(GameEntity):
    def __init__(self, x, y, direction = "down"):
        super().__init__(f"assets/images/char/visitor2/{direction}/0.png", x, y, 0, 0, 0.9)