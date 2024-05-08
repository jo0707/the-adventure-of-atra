import pygame

from constants import DURATION_CHAR_CHANGE
from src.components.gameEntity import GameEntity
from src.components.movable import Movable

DIRECTIONS = ("down", "left", "up", "right")

class Character(GameEntity, Movable):
    def __init__(self, name: str):
        GameEntity.__init__(self, f'assets/images/char/{name}/down/0.png', width=78, height=144)
        Movable.__init__(self, 4, self.rect)
        
        self.currentDirection = DIRECTIONS[0]
        self.currentFrame = 0
        self.animationTick = 0
        self.isKeyDown = False
        self.images: dict[str, list[pygame.Surface]] = {}
        for direction in DIRECTIONS:
            self.images[direction] = []
            for j in range (0, 4):
                self.images[direction].append(
                    pygame.transform.scale(pygame.image.load(f'assets/images/char/{name}/{direction}/{j}.png').convert_alpha(), (78, 144))
                )
                
    def update(self):
        self.animationTick += 1
        if not self.isKeyDown:
            self.currentFrame = 0
            self.image = self.images[self.currentDirection][self.currentFrame]
        if self.animationTick >= DURATION_CHAR_CHANGE and self.isKeyDown:
            self.nextFrame()
        
    def onKeyDown(self, keys):
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.isKeyDown = True
            self.moveDown()
            if self.currentDirection != DIRECTIONS[0]:
                self.currentDirection = DIRECTIONS[0]
                self.nextFrame()
        elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.isKeyDown = True
            self.moveLeft()
            if self.currentDirection != DIRECTIONS[1]:
                self.currentDirection = DIRECTIONS[1]
                self.nextFrame()
        elif keys[pygame.K_UP] or keys[pygame.K_w]:
            self.isKeyDown = True
            self.moveUp()
            if self.currentDirection != DIRECTIONS[2]:
                self.currentDirection = DIRECTIONS[2]
                self.nextFrame()
        elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.isKeyDown = True
            self.moveRight()
            if self.currentDirection != DIRECTIONS[3]:
                self.currentDirection = DIRECTIONS[3]
                self.nextFrame()
        else:
            self.isKeyDown = False 
        
    def nextFrame(self):
        self.animationTick = 0
        self.currentFrame = (self.currentFrame + 1) % 4
        self.image = self.images[self.currentDirection][self.currentFrame]