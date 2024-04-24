import pygame
from abc import ABC, abstractmethod

class Clickable(ABC):
    def __init__(self, position: tuple[int, int], size: tuple[int, int]):
        self.position = position
        self.size = size
        self.rect = pygame.Rect(position, size)
        
    def isClicked(self, position: tuple[int, int]):
        return self.rect.collidepoint(position)
    
    @abstractmethod
    def onClick(self):
        pass