import pygame

from src.components.character import Character
from src.utils.screenHelper import ScreenHelper

DIRECTIONS = ("down", "left", "up", "right")

class Atra(Character):
    def __init__(self):
        super().__init__("atra")
        self.isKeyDown = False  
        self.obstacles = []    
        self.clamps = []  
        
    def onKeyDown(self, keys):
        originalX = self.rect.x
        originalY = self.rect.y
        
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
            
        if self.rect.collidelist(self.obstacles) != -1:
            self.rect.x = originalX
            self.rect.y = originalY
            
    def addObstacles(self, obstacles: list[pygame.Rect]):
        self.obstacles.extend(obstacles)
        
    def addObstacle(self, obstacle: pygame.Rect):
        self.obstacles.append(obstacle)
        
    def addClampObstacle(self, obstacle: pygame.Rect):
        self.clamps.append(obstacle)

    def update(self):
        for obstacle in self.clamps:
            self.rect.clamp_ip(obstacle)
        return super().update()

    def placeBottom(self, x: int | None = None):
        self.rect.midbottom = (x if x != None else ScreenHelper.getWindowX() / 2, ScreenHelper.getWindowY() - 20)
        self.currentDirection = DIRECTIONS[2]
        self.image = self.images[self.currentDirection][0]
        
    def placeRight(self, y: int | None = None):
        self.rect.midright = (ScreenHelper.getWindowX() - 20, y if y != None else ScreenHelper.getWindowY() / 2)
        self.currentDirection = DIRECTIONS[1]
        self.image = self.images[self.currentDirection][0]
        
    def placeTop(self, x: int | None = None):
        self.rect.midtop = (x if x != None else ScreenHelper.getWindowX() / 2, 20)
        self.currentDirection = DIRECTIONS[0]
        self.image = self.images[self.currentDirection][0]
        
    def placeLeft(self, y: int | None = None):
        self.rect.midleft = (20, y if y != None else ScreenHelper.getWindowY() / 2)
        self.currentDirection = DIRECTIONS[3]
        self.image = self.images[self.currentDirection][0]
        
    def placeCenter(self):
        self.rect.center = (ScreenHelper.getWindowX() / 2, ScreenHelper.getWindowY() / 2)
        self.currentDirection = DIRECTIONS[0]
        self.image = self.images[self.currentDirection][0]
        