# from typing import Any, List
# import pygame


# from src.components.closeButton import CloseButton
# from src.components.textbox import Textbox
# from src.components.interactableItem import InteractableItem
# from src.components.gameEntity import GameEntity

# class Dialog(pygame.sprite.Group):
#     def __init__(self, x: int, y: int, interactableItem: InteractableItem, onClose = lambda: print("Close item detail clicked")):
#         super().__init__()
#         self.width = 1024
#         self.height = 575
#         self.pad = 48
        
#         self.interactableItem = interactableItem
#         self.grayBackground = pygame.surface.Surface((pygame.display.get_window_size()), pygame.SRCALPHA, 32)
#         self.grayBackground.fill((0, 0, 0, 128))
#         self.background = GameEntity('assets/images/components/dialogBackground.png', x, y, width=self.width, height=self.height)
        
#         self.closeButton = CloseButton(x + self.pad, y + self.pad, 1.5, action=onClose)
#         self.add(self.background, self.image, self.closeButton)
        
#     def draw(self, surface: pygame.Surface, bgsurf: pygame.Surface | None = None, special_flags: int = 0) -> List[pygame.Rect]:
#         surface.blit(self.grayBackground, (0, 0))
#         super().draw(surface, bgsurf, special_flags)