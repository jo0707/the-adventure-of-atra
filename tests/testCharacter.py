import unittest
import pygame
from unittest.mock import MagicMock

from src.components.character import Character

class TestCharacter(unittest.TestCase):

    def setUp(self):
        # Mocking pygame functions and classes
        pygame.init = MagicMock()
        pygame.transform.scale = MagicMock(return_value=pygame.Surface((68, 136)))

    def testInitialization(self):
        character = Character("Atra")
        self.assertEqual(character.width, 68)
        self.assertEqual(character.height, 136)
        self.assertEqual(character.currentDirection, "down")
        self.assertEqual(character.currentFrame, 0)
        self.assertEqual(character.animationTick, 0)
        # Ensure images are loaded correctly
        self.assertEqual(len(character.images), 4)  # DIRECTIONS = ("down", "left", "up", "right")

    def testUpdate(self):
        character = Character("Atra")
        character.isKeyDown = True
        character.nextFrame = MagicMock()  # Mocking nextFrame method for testing

        # Test when isKeyDown is True
        character.update()
        self.assertFalse(character.nextFrame.called)

        # Test when isKeyDown is False
        character.isKeyDown = False
        character.update()
        self.assertEqual(character.currentFrame, 0)  # currentFrame should be reset
        self.assertEqual(character.image, character.images[character.currentDirection][0])

    def testNextFrame(self):
        character = Character("Atra")
        character.currentFrame = 2
        character.currentDirection = "down"
        character.animationTick = 0

        # Test next frame calculation
        character.nextFrame()
        self.assertEqual(character.currentFrame, 3)  # Next frame
        self.assertEqual(character.image, character.images["down"][3])  # Image updated

        # Test frame reset
        character.currentFrame = 3
        character.nextFrame()
        self.assertEqual(character.currentFrame, 0)  # Back to the first frame