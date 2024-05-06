
from src.components.gameEntity import GameEntity


class RadenIntan2(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/components/radenintan2.png", x, y, 0, 0, 0.16)