
from src.components.gameEntity import GameEntity


class WallText(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/components/wallText.png", x, y, 0, 0, 1)