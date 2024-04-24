import pygame

from src.components.gameEntity import GameEntity
from src.player import Player
from src.components.movable import Movable

class Character(GameEntity, Movable):
    def __init__(self):
        GameEntity.__init__(self, 'assets/images/char/atra/0.png', 0, 0,52, 84)
        self.images = []
        for i in range(0, 2):
            self.images.append(
                pygame.transform.scale(pygame.image.load(f'assets/images/char/atra/{i}.png'), (52, 84))
            ) 
            
        self.player = Player.getPlayer()
        Movable.__init__(self, 4, self.rect)
        
    def update(self):
        pass
        
    def moveDown(self, amount: int = 0):
        self.image = self.images[0]
        return super().moveDown(amount)
    
    def moveUp(self, amount: int = 0):
        self.image = self.images[1]
        return super().moveUp(amount)