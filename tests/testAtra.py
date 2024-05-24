import unittest
from src.components.character import Character
from src.components.atra import Atra

class TestAtra(unittest.TestCase):
    def setUp(self):
        self.atra = Atra()

    def test_initialization(self):
        self.assertEqual(self.atra.isKeyDown, False)
        self.assertEqual(len(self.atra.obstacles), 0)
        self.assertEqual(len(self.atra.clamps), 0)
        self.assertEqual(self.atra.firstTickColliding, False)
        self.assertTrue(isinstance(self.atra, Atra))
        self.assertTrue(isinstance(self.atra, Character))

    def test_methods(self):
        self.assertTrue(hasattr(self.atra, "update"))
        self.assertTrue(hasattr(self.atra, "onKeyDown"))
        self.assertTrue(hasattr(self.atra, "placeBottom"))
        self.assertTrue(hasattr(self.atra, "placeRight"))
        self.assertTrue(hasattr(self.atra, "placeTop"))
        self.assertTrue(hasattr(self.atra, "placeLeft"))
        self.assertTrue(hasattr(self.atra, "placeCenter"))
        
    def test_moveUp(self):
        originalY = self.atra.rect.y
        self.atra.moveUp()
        self.assertEqual(self.atra.rect.y, originalY - self.atra.speed)
        
    def test_moveDown(self):
        originalY = self.atra.rect.y
        self.atra.moveDown()
        self.assertEqual(self.atra.rect.y, originalY + self.atra.speed)
        
    def test_moveLeft(self):
        originalX = self.atra.rect.x
        self.atra.moveLeft()
        self.assertEqual(self.atra.rect.x, originalX - self.atra.speed)
        
    def test_moveRight(self):
        originalX = self.atra.rect.x
        self.atra.moveRight()
        self.assertEqual(self.atra.rect.x, originalX + self.atra.speed)