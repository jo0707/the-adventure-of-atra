

from src.components.gameEntity import GameEntity


class FrontRightTable(GameEntity):
    def __init__(self, x, y):
        super().__init__("assets/images/components/lobbyFrontRightTable.png", x, y, 0, 0, 1)
        self.rect.bottomright = (x, y)