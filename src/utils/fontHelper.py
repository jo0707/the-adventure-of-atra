
import os
import pygame

class FontHelper:
    fonts: dict[str, pygame.font.Font] = {}

    @staticmethod
    def initFonts():
        FontHelper.fonts["default"] = pygame.font.Font(None, 32)
        for fontPath in os.listdir("assets/fonts"):
            if fontPath.endswith(".ttf") or fontPath.endswith(".otf"):
                name = os.path.splitext(fontPath)[0]
                FontHelper.fonts[name] = pygame.font.Font(f"assets/fonts/{fontPath}", 32)