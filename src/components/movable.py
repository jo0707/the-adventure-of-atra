import pygame

class Movable:
    def __init__(self, speed: int, rect: pygame.Rect):
        self.speed = speed
        self.rect = rect
        
    def moveTo(self, x: int, y: int):
        self.rect.move_ip(x, y)
        
    def moveUp(self, amount: int = 0):
        self.rect.move_ip(0, -(amount if amount > 0 else self.speed))
        
    def moveDown(self, amount: int = 0):
        self.rect.move_ip(0, amount if amount > 0 else self.speed)
        
    def moveLeft(self, amount: int = 0):
        self.rect.move_ip(-(amount if amount > 0 else self.speed), 0)
        
    def moveRight(self, amount: int = 0):
        self.rect.move_ip(amount if amount > 0 else self.speed, 0)