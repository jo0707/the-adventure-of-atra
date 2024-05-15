import pygame
import random

class GameEntity(pygame.sprite.Sprite):
    # imagePath: image will be loaded from this path and used as sprite
    # x: x coordinate of the sprite
    # y: y coordinate of the sprite
    # width: width of the sprite
    # height: height of the sprite
    # scale: size of the sprite
    def __init__(self, imagePath: str = "/assets/images/components/pillar.png", x: int = 0, y: int = 0, width: int = 0, height: int = 0, scale: float = 0):
        super().__init__()
        self.image = pygame.image.load(imagePath).convert_alpha()
        if scale:
            self.image = pygame.transform.scale_by(self.image, scale)
        else:
            self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft=(x, y))
        
    def update(self):
        pass
    
    # mainly used for creating obstacle rect while collision detection
    # this will limit player movement
    def copyRect(self, heightFactor: float, bottomOffset: int = 0):
        rectCopy = self.rect.copy()
        rectCopy.top = rectCopy.bottom - bottomOffset
        rectCopy.height = rectCopy.height * heightFactor
        rectCopy.top = rectCopy.top - rectCopy.height
        return rectCopy