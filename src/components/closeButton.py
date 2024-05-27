import pygame
import random

from src.components.textbox import Textbox
from src.components.gameEntity import GameEntity
from src.components.clickable import Clickable
from src.utils.fontHelper import FontHelper

class CloseButton(GameEntity, Clickable):
    def __init__(self, x: int, y: int, scale: int = 1, action=lambda: None) -> None:
        GameEntity.__init__(self, "assets/images/components/close.png", x, y, scale=scale)
        self.action = action
        self.isHovered = False
        
    def update(self):
        if self.getHoverState() != self.isHovered:
            self.isHovered = not self.isHovered
            self.hoverChange()

    def onClick(self):
        self.action()
        
    def setOnClick(self, action: callable):
        self.action = action
        
    def setText(self, text: str):
        self.__text = text
        self.update()

    def getHoverState(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    def hoverChange(self):
        if self.isHovered:
            self.image.fill((32, 32, 32), special_flags=pygame.BLEND_RGB_SUB)
        else:
            self.image.fill((32, 32, 32), special_flags=pygame.BLEND_RGB_ADD)
            