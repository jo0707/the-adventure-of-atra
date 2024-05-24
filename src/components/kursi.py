
from src.components.gameEntity import GameEntity


class Kursi(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/components/kursi.png", x, y, 0, 0, 1)