import pygame
import pygame.freetype

from src.utils.fontHelper import FontHelper

class Textbox():
    def __init__(self, text = "Text", x = 0, y = 0, size = 24, color = pygame.colordict.THECOLORS["white"], font: pygame.freetype.Font = None, bgColor = None):
        self.font = font if font else FontHelper.fonts["reguler"]
        self.__text = text
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        
        [self.surf, self.rect] = self.font.render(self.__text, color, bgColor, size=size)
        self.rect.topleft = (x, y)
        
    def display(self, screen):
        screen.blit(self.surf, self.rect)
        
    def setText(self, text):
        self.__text = text
        [self.surf, self.rect] = self.font.render(self.__text, True, self.color)
        self.rect.topleft = (self.x, self.y)
        
    def wrapText(self, width):
        self.__text = self.font.render_textrect(self.__text, (self.x, self.y, width, 0), self.color)
        [self.surf, self.rect] = self.font.render(self.__text, True, self.color)
        self.rect.topleft = (self.x, self.y)