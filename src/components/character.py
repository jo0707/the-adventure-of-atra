import pygame

from constants import DURATION_CHAR_CHANGE
from src.components.gameEntity import GameEntity
from src.components.movable import Movable

DIRECTIONS = ("down", "left", "up", "right")

class Character(GameEntity, Movable):
    def __init__(self, name: str):
        self.width = 68
        self.height = 136
        GameEntity.__init__(self, f'assets/images/char/{name}/down/0.png', width=self.width, height=self.height)
        Movable.__init__(self, 8, self.rect)
        
        self.currentDirection = DIRECTIONS[0]
        self.currentFrame = 0
        self.animationTick = 0
        
        # walking animation for character
        self.images: dict[str, list[pygame.Surface]] = {}
        for direction in DIRECTIONS:
            self.images[direction] = []
            for j in range (0, 4):
                self.images[direction].append(
                    pygame.transform.scale(pygame.image.load(f'assets/images/char/{name}/{direction}/{j}.png').convert_alpha(), (self.width, self.height))
                )
                
    def update(self):
        self.animationTick += 1
        if not self.isKeyDown:
            self.currentFrame = 0
            self.image = self.images[self.currentDirection][self.currentFrame]
        if self.animationTick >= DURATION_CHAR_CHANGE and self.isKeyDown:
            self.nextFrame()
        
    def nextFrame(self):
        self.animationTick = 0
        self.currentFrame = (self.currentFrame + 1) % 4
        self.image = self.images[self.currentDirection][self.currentFrame]