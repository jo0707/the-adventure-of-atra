import pygame
import random


class GameEntity(pygame.sprite.Sprite):
    def __init__(self, imagePath: str = "/assets/images/components/pillar.png", x: int = 0, y: int = 0, width: int = 0, height: int = 0, scale: float = 0):
        super().__init__()
        self.image = pygame.image.load(imagePath)
        if scale:
            self.image = pygame.transform.scale_by(self.image, scale)
        else:
            self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        
    def update(self):
        pass
