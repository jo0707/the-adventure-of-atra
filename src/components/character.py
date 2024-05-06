import pygame

from constants import DURATION_CHAR_CHANGE
from src.components.gameEntity import GameEntity
from src.player import Player
from src.components.movable import Movable

DIRECTIONS = ("down", "left", "up", "right")

class Character(GameEntity, Movable):
    def __init__(self, name: str):
        GameEntity.__init__(self, f'assets/images/char/{name}/down/0.png', 104, 192, 0)
        Movable.__init__(self, 2, self.rect)
        
        self.currentDirection = DIRECTIONS[0]
        self.currentFrame = 0
        self.animationTick = 0
        self.keyDown = False
        self.images: dict[str, list[pygame.Surface]] = {}
        for direction in DIRECTIONS:
            self.images[direction] = []
            for j in range (0, 4):
                self.images[direction].append(
                    pygame.transform.scale(pygame.image.load(f'assets/images/char/{name}/{direction}/{j}.png'), (104, 192))
                )
    def update(self):
        self.animationTick += 1
        if self.animationTick >= DURATION_CHAR_CHANGE and self.keyDown:
            self.nextFrame()
        
    def onKeyDown(self, keys):
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.moveDown()
            if self.currentDirection != DIRECTIONS[0]:
                self.currentDirection = DIRECTIONS[0]
                self.nextFrame()
            self.keyDown = True
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.moveLeft()
            if self.currentDirection != DIRECTIONS[1]:
                self.currentDirection = DIRECTIONS[1]
                self.nextFrame()
            self.keyDown = True
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.moveUp()
            if self.currentDirection != DIRECTIONS[2]:
                self.currentDirection = DIRECTIONS[2]
                self.nextFrame()
            self.keyDown = True
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.moveRight()
            if self.currentDirection != DIRECTIONS[3]:
                self.currentDirection = DIRECTIONS[3]
                self.nextFrame()
            self.keyDown = True
        else:
            self.keyDown = False 
        
    def moveDown(self, amount: int = 0):
        return super().moveDown(amount)
    
    def moveLeft(self, amount: int = 0):
        return super().moveLeft(amount)
    
    def moveUp(self, amount: int = 0):
        return super().moveUp(amount)
    
    def moveRight(self, amount: int = 0):
        return super().moveRight(amount)
    
    def nextFrame(self):
        self.currentFrame += 1
        self.animationTick = 0
        if self.currentFrame >= 4:
            self.currentFrame = 0
        self.image = self.images[self.currentDirection][self.currentFrame]