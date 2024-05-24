from typing import List
import pygame


from src.components.textbox import Textbox
from src.components.interactableItem import InteractableItem
from src.components.gameEntity import GameEntity

class ItemPreview(pygame.sprite.Group):
    def __init__(self, x: int, y: int, interactableItem: InteractableItem):
        super().__init__()
        self.width = 600
        self.height = 180
        self.pad = 24
        
        self.interactableItem = interactableItem
        self.background = GameEntity('assets/images/components/itemPreviewBackground.png', x, y, width=self.width, height=self.height)
        
        # TODO: Change image path after image path refactored
        self.image = GameEntity(interactableItem.imagePath, height=95)
        self.image.rect.bottomleft = (x + self.pad, y + self.height - self.pad)
        
        self.titleTextbox = Textbox(interactableItem.title, x + self.pad, y + self.pad, 20, pygame.colordict.THECOLORS['black'])
        
        self.enterToOpenTextbox = Textbox('⏎ Tekan E untuk melihat detail', size=16, color=pygame.colordict.THECOLORS['black'])
        self.enterToOpenTextbox.rect.bottomright = (x + self.width - self.pad, y + self.height - self.pad)
        
        self.add(self.background, self.image)
        
    def draw(self, surface: pygame.Surface, bgsurf: pygame.Surface | None = None, special_flags: int = 0) -> List[pygame.Rect]:
        super().draw(surface, bgsurf, special_flags)
        self.titleTextbox.display(surface)
        self.enterToOpenTextbox.display(surface)