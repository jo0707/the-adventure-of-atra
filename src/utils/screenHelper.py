import pygame

class ScreenHelper:
    @staticmethod
    def getWindowX():
        return pygame.display.get_surface().get_size()[0]
    
    @staticmethod
    def getWindowY():
        return pygame.display.get_surface().get_size()[1]
    