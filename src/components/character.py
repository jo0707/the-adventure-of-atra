import pygame

from src.components.gameEntity import GameEntity
from src.player import Player
from src.components.movable import Movable

class Character(GameEntity, Movable):
    def __init__(self):
        GameEntity.__init__(self, 'assets/images/char/atra/00.png', 0, 0, 104, 168)
        self.images = []
        for i in range(0, 1):
            for j in range (0, 4):
                self.images.append(
                    pygame.transform.scale(pygame.image.load(f'assets/images/char/atra/{i}{j}.png'), (104, 168))
                )
        self.player = Player.getPlayer()
        Movable.__init__(self, 2, self.rect)
        
    def update(self):
        pass
        
    def moveDown(self, amount: int = 0):
        self.image = self.images[0]
        return super().moveDown(amount)
    
    def moveUp(self, amount: int = 0):
        self.image = self.images[1]
        return super().moveUp(amount)