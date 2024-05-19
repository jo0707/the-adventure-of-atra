from typing import List
import pygame


from src.components.textbox import Textbox
from src.components.interactableItem import InteractableItem
from src.components.gameEntity import GameEntity

class ItemDetail(pygame.sprite.Group):
    def __init__(self, x: int, y: int, interactableItem: InteractableItem):
        super().__init__()
        self.width = 1024
        self.height = 575
        self.pad = 48
        
        self.interactableItem = interactableItem
        self.background = GameEntity('assets/images/components/itemDetailBackground.png', x, y, width=self.width, height=self.height)
        
        # TODO: Change image path after image path refactored
        self.image = GameEntity(f"assets/images/real/{interactableItem.realImageName}", width=self.width // 3)
        self.image.rect.midleft = (x + self.pad, y + self.height/2)
        
        self.titleTextbox = Textbox(interactableItem.title, x + self.pad, y + self.pad, 24, pygame.colordict.THECOLORS['black'])
        self.titleTextbox.rect.topright = (x + self.width - self.pad, y + self.pad)
        
        self.descriptionTextbox = Textbox(interactableItem.description, size=18, color=pygame.colordict.THECOLORS['black'])
        self.descriptionTextbox.rect.bottomright = (x + self.width - self.pad, y + self.height - self.pad)
        
        self.add(self.background, self.image)
        
    def draw(self, surface: pygame.Surface, bgsurf: pygame.Surface | None = None, special_flags: int = 0) -> List[pygame.Rect]:
        super().draw(surface, bgsurf, special_flags)
        self.titleTextbox.display(surface)
        self.descriptionTextbox.display(surface)