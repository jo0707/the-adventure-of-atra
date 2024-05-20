import unittest

import pygame

from src.components.movable import Movable

class TestMovable(unittest.TestCase):
    speed = 4
    rect = pygame.draw.rect(pygame.Surface((100, 100)), (255, 255, 255), (0, 0, 100, 100))
    
    # check if all the methods are exists    
    def testMovable(self): 
        movable = Movable(TestMovable.speed, TestMovable.rect)
        self.assertTrue(hasattr(movable, "moveTo"))
        self.assertTrue(hasattr(movable, "moveUp"))
        self.assertTrue(hasattr(movable, "moveDown"))
        self.assertTrue(hasattr(movable, "moveLeft"))
        self.assertTrue(hasattr(movable, "moveRight"))