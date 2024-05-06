
from src.components.gameEntity import GameEntity


class Staff(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/char/staff/down/0.png", x, y, 0, 0, 1)