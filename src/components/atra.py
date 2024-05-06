import pygame

from src.components.character import Character

DIRECTIONS = ("down", "left", "up", "right")

class Atra(Character):
    def __init__(self):
        super().__init__("atra")
        
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