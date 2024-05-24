import random
import unittest

import pygame

from src.components.movable import Movable

class TestMovable(unittest.TestCase):
    speed = 4
    rect = pygame.draw.rect(pygame.Surface((100, 100)), (255, 255, 255), (0, 0, 100, 100))
    
    def setUp(self):
        self.movable = Movable(TestMovable.speed, TestMovable.rect)
    
    # check if all the methods are exists    
    def testMovable(self): 
        self.assertTrue(hasattr(self.movable, "moveTo"))
        self.assertTrue(hasattr(self.movable, "moveUp"))
        self.assertTrue(hasattr(self.movable, "moveDown"))
        self.assertTrue(hasattr(self.movable, "moveLeft"))
        self.assertTrue(hasattr(self.movable, "moveRight"))
        
    def test_moveUp(self):
        originalY = self.movable.rect.y
        self.movable.moveUp()
        self.assertEqual(self.movable.rect.y, originalY - TestMovable.speed)
        
    def test_moveDown(self):
        originalY = self.movable.rect.y
        self.movable.moveDown()
        self.assertEqual(self.movable.rect.y, originalY + TestMovable.speed)
        
    def test_moveLeft(self):
        originalX = self.movable.rect.x
        self.movable.moveLeft()
        self.assertEqual(self.movable.rect.x, originalX - TestMovable.speed)
        
    def test_moveRight(self):
        originalX = self.movable.rect.x
        self.movable.moveRight()
        self.assertEqual(self.movable.rect.x, originalX + TestMovable.speed)
        
    def test_moveTo(self):
        self.movable.rect.x = 0
        self.movable.rect.y = 0
        targetX = random.randint(0, 100)
        targetY = random.randint(0, 100)
        
        self.movable.moveTo(targetX, targetY)
        
        self.assertEqual(self.movable.rect.x, targetX)
        self.assertEqual(self.movable.rect.y, targetY)