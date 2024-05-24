
from src.components.interactableItem import InteractableItem
from src.components.gameEntity import GameEntity


class StaffQuiz(InteractableItem):
    def __init__(self, x, y, direction = "down"):
        super().__init__(f"assets/images/char/staff/{direction}/0.png", x, y, 0, 0, 1,
                            "Edukator",
                            "Siapkah kamu untuk mengikuti kuis dari saya?",
                            "transparent.png",
                         )