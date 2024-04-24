import pygame
import random


class GameEntity(pygame.sprite.Sprite):
    def __init__(self, imagePath: str, x: int, y: int, width: int, height: int):
        super().__init__()
        self.image = pygame.image.load(imagePath)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        
    def update(self):
        pass
