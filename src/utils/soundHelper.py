import os
import pygame

class SoundHelper:
    sounds: dict[str, pygame.mixer.Sound] = {}
        
    @staticmethod
    def initSounds():
        for filePath in os.listdir("assets/sounds"):
            name = os.path.splitext(filePath)[0]
            SoundHelper.sounds[name] = pygame.mixer.Sound(f"assets/sounds/{filePath}")