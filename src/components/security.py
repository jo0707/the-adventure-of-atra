
from src.components.gameEntity import GameEntity


class Security(GameEntity):
    def __init__(self, x, y, direction = "down"):
        super().__init__(f"assets/images/char/security/{direction}/0.png", x, y, 0, 0, 0.2)