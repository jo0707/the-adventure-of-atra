
from src.components.gameEntity import GameEntity


class WallMap(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/components/wallMap.png", x, y, 0, 0, 1)