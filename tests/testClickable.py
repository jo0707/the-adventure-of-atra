import unittest
from src.components.clickable import Clickable

class MockClickable(Clickable):
    def onClick(self):
        pass

class TestClickable(unittest.TestCase):
    def setUp(self):
        self.clickable = MockClickable((0, 0), (100, 100))
        
    def test_initialization(self):
        self.assertEqual(self.clickable.position, (0, 0))
        self.assertEqual(self.clickable.size, (100, 100))
        self.assertTrue(hasattr(self.clickable, "rect"))
        
    def test_methods(self):
        self.assertTrue(hasattr(self.clickable, "isClicked"))
        self.assertTrue(hasattr(self.clickable, "onClick")) 