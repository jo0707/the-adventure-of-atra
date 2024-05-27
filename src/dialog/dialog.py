# from typing import Any, List, Tuple
# import pygame


# import pygame.docs
# from src.components.closeButton import CloseButton
# from src.components.textbox import Textbox
# from src.components.gameEntity import GameEntity

# class Dialog(pygame.sprite.Group):
#     def __init__(self, position: Tuple[int, int], width = 1024, height = 575, pad = 48):
#         super().__init__()
#         self.height = height
#         self.width = width
#         self.pad = pad
#         self.textboxes: dict[str, List[pygame.Surface, ]] = {}
        
#         self.grayBackground = pygame.surface.Surface((pygame.display.get_window_size()), pygame.SRCALPHA, 32)
#         self.grayBackground.fill((0, 0, 0, 128))
#         self.background = GameEntity('assets/images/components/dialogBackground.png', position[0], position[1], width=self.width, height=self.height)
        
#         self.closeButton = CloseButton(position[0] + self.pad, position[1] + self.pad, 1.7)
#         self.add(self.background, self.image, self.closeButton)
        
#     def draw(self, surface: pygame.Surface, bgsurf: pygame.Surface | None = None, special_flags: int = 0) -> List[pygame.Rect]:
#         surface.blit(self.grayBackground, (0, 0))
#         super().draw(surface, bgsurf, special_flags)

#     def onClick(self, position: tuple[int, int]):
#         for item in self:
#             if item.rect.collidePoint(position):
#                 if isinstance(item, CloseButton): item.onClick()
                
#     def insertText(self, key: str, text: str, textSize: int, position: Tuple[int, int], rectSize: Tuple[int, int], color: pygame.Color = pygame.Color("black")):
#         surface = pygame.surface.Surface(rectSize, pygame.SRCALPHA, 32)
#         textbox = Textbox(text, size=textSize, color=color, wrap=True)
#         self.textboxes.append([surface, surface.get_rect(topleft=(position)), textbox])
        
#     def setOnClose(self, func):
#         self.closeButton.setOnClick(func)