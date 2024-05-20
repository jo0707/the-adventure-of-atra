import pygame
import pygame.freetype

from src.utils.fontHelper import FontHelper

class Textbox():
    def __init__(self, text = "Text", x = 0, y = 0, size = 24, color = pygame.colordict.THECOLORS["black"], font: pygame.freetype.Font = None, bgColor = None, wrap: bool = False):
        self.font = font if font else FontHelper.fonts["reguler"]
        self.__text = text
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.bgColor = bgColor
        self.wrap = wrap
        
        [self.surf, self.rect] = self.font.render(self.__text, color, bgColor, size=size)
        self.rect.topleft = (x, y)
        
    def display(self, surface):
        if not self.wrap:
            surface.blit(self.surf, self.rect)
        else:
            self.__renderWrappedText(surface)
        
    def setText(self, text):
        self.__text = text
        [self.surf, self.rect] = self.font.render(self.__text, self.color, self.bgColor, size=self.size)
        self.rect.topleft = (self.x, self.y)
        
    def __renderWrappedText(self, surface):
        self.font.size = self.size
        words = self.__text.split(' ')
        w, h = surface.get_size()
        line_spacing = self.font.get_sized_height() + 2
        x, y = 0, line_spacing
        space = self.font.get_rect(' ')

        for word in words:
            bounds = self.font.get_rect(word)
            if x + bounds.width + bounds.x >= w:
                x, y = 0, y + line_spacing
            self.font.render_to(surface, (x, y - bounds.y), None, self.color, size=self.size)
            x += bounds.width + space.width