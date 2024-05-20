import pygame
import random

from src.components.textbox import Textbox
from src.components.gameEntity import GameEntity
from src.components.clickable import Clickable

class QuizButton(GameEntity, Clickable):
    def __init__(self, x: int, y: int, width: int, height: int, text: str, font = None, textSize: int = 24, textColor = pygame.colordict.THECOLORS["black"], textHoverColor = pygame.colordict.THECOLORS["slategray"], action=lambda: None) -> None:
        GameEntity.__init__(self, "assets/images/components/quizButton.png", x, y, width, height)
        self.__text = text
        self.width = width
        self.height = height
        self.textColor = textColor
        self.textHoverColor = textHoverColor
        self.action = action
        self.isHovered = False
        self.originalSurface = self.image.copy()
        
        self.textbox = Textbox(text, 0, 0, textSize, textColor, font)
        self.setText(text)
        
    def update(self):
        if self.getHoverState() != self.isHovered:
            self.isHovered = not self.isHovered
            self.hoverChange()
            
    def clearSurface(self):
        self.image = self.originalSurface.copy()

    def onClick(self):
        self.action()
        
    def setText(self, text: str):
        self.__text = text
        self.clearSurface()
        self.textbox.setText(text)
        self.textbox.rect.center = (self.width // 2, self.height // 2)
        self.textbox.display(self.image)

    def getHoverState(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())
    
    def hoverChange(self):
        if self.isHovered:
            self.image.fill((32, 32, 32), special_flags=pygame.BLEND_RGB_SUB)
            self.textbox.surf.fill((32, 32, 32), special_flags=pygame.BLEND_RGB_SUB)
        else:
            self.image.fill((32, 32, 32), special_flags=pygame.BLEND_RGB_ADD)
            self.textbox.surf.fill((32, 32, 32), special_flags=pygame.BLEND_RGB_ADD)
            