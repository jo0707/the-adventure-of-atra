
from src.components.gameEntity import GameEntity


class Staff(GameEntity):
    def __init__(self, x, y, direction = "down"):
        super().__init__(f"assets/images/char/staff/{direction}/0.png", x, y, 0, 0, 1)