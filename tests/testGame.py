import unittest

from src.game import Game

class TestGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()
    
    def test_initialization(self):
        self.assertTrue(hasattr(self.game, "screen"))
        self.assertTrue(hasattr(self.game, "clock"))
        self.assertTrue(hasattr(self.game, "sceneManager"))
        
    def test_methods(self):
        self.assertTrue(hasattr(self.game, "onEvent"))
        self.assertTrue(hasattr(self.game, "gameLoop"))
        self.assertTrue(hasattr(self.game, "quitGame"))