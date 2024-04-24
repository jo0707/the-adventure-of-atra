import pygame

from src.utils.fontHelper import FontHelper

class Textbox():
    def __init__(self, text = "Text", x = 0, y = 0, size = 24, color = pygame.colordict.THECOLORS["white"], font: pygame.font = None, bgColor = None):
        self.font = font if font else FontHelper.fonts["reguler"]
        self.__text = text
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        
        self.surf = self.font.render(self.__text, True, color, bgColor)
        self.rect = self.surf.get_rect()
        self.rect.topleft = (x, y)
        
    def display(self, screen):
        screen.blit(self.surf, self.rect)
        
    def setText(self, text):
        self.__text = text
        self.surf = self.font.render(self.__text, True, self.color)
        self.rect = self.surf.get_rect()
        self.rect.topleft = (self.x, self.y)