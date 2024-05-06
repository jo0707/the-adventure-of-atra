
from src.components.gameEntity import GameEntity


class Visitor2(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/char/visitor2/up/0.png", x, y, 0, 0, 1)