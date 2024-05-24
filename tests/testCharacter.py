import unittest

from src.components.gameEntity import GameEntity
from src.components.movable import Movable
from src.components.character import Character


class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.name = "atra"
        self.character = Character(self.name)

    def test_initialization(self):
        self.assertTrue(hasattr(self.character, "width"))
        self.assertTrue(hasattr(self.character, "height"))
        self.assertTrue(isinstance(self.character, Character))
        self.assertTrue(isinstance(self.character, Movable))
        self.assertTrue(isinstance(self.character, GameEntity))
        self.assertEqual(self.character.name, self.name)

    def test_methods(self):
        self.assertTrue(hasattr(self.character, "update"))
        self.assertTrue(hasattr(self.character, "nextFrame"))