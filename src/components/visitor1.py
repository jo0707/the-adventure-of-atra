
from src.components.gameEntity import GameEntity


class Visitor1(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/char/visitor1/up/0.png", x, y, 0, 0, 8)