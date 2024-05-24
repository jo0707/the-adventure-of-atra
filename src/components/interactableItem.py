import pygame
import os
from src.components.gameEntity import GameEntity

class InteractableItem(GameEntity):
    def __init__(self, imagePath="assets/images/components/pillar.png", x=0, y=0, width=0, height=0, scale=1, title="Sebuah Item", description="Deskripsi item", realImageName="lampung/keris.png"):
        super().__init__(imagePath, x, y, width, height, scale)
        self.title = title
        self.description = description
        self.realImageName = realImageName
        self.isCollided = False
        
    def onPlayerCollision(self, isCollided: bool):
        if self.isCollided != isCollided:
            if isCollided:
                self.image.fill((32, 32, 32), special_flags=pygame.BLEND_RGB_SUB)
            else:
                self.image.fill((32, 32, 32), special_flags=pygame.BLEND_RGB_ADD)
            self.isCollided = isCollided