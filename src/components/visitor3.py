
from src.components.gameEntity import GameEntity


class Visitor3(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/char/visitor3/down/0.png", x, y, 0, 0, 1)