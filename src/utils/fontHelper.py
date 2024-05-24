
import os
import pygame
import pygame.freetype

class FontHelper:
    fonts: dict[str, pygame.freetype.Font] = {}

    @staticmethod
    def initFonts():
        FontHelper.fonts["default"] = pygame.freetype.Font(None, 32)
        for fontPath in os.listdir("assets/fonts"):
            if fontPath.endswith(".ttf") or fontPath.endswith(".otf"):
                name = os.path.splitext(fontPath)[0]
                FontHelper.fonts[name] = pygame.freetype.Font(f"assets/fonts/{fontPath}", 32)
    
    # @staticmethod
    # def getFont(name: str = "reguler") -> pygame.freetype.Font:
    #     FontHelper.fonts.get(name, FontHelper.fonts["default"]).size = 32