import unittest
import pygame
from unittest.mock import MagicMock
from src.components.closeButton import CloseButton

class TestCloseButton(unittest.TestCase):
    def setUp(self):
        pygame.init()
        
    def testInitialization(self):
        close_button = CloseButton(100, 100)
        
        # Test if the image loaded successfully
        self.assertIsNotNone(close_button.image)
        
        # Test if hover state initialized correctly
        self.assertFalse(close_button.isHovered)
        
        # Test if the image fill color is set correctly
        self.assertEqual(close_button.image.get_at((0, 0)), (0, 0, 0, 0))

    def testOnClick(self):
        # Mocking the action
        mock_action = MagicMock()
        
        # Creating CloseButton instance with mocked action
        close_button = CloseButton(100, 100, action=mock_action)
        
        # Simulating a click event
        close_button.onClick()
        
        # Asserting if the action was called
        mock_action.assert_called_once()

    def testHoverChange(self):
        close_button = CloseButton(100, 100)
        
        # Before hover
        self.assertEqual(close_button.image.get_at((0, 0)), (0, 0, 0, 0))
        
        # Simulating hover
        close_button.isHovered = True
        close_button.hoverChange()
        
        # After hover
        self.assertEqual(close_button.image.get_at((0, 0)), (0, 0, 0, 0))
        
        # Simulating unhover
        close_button.isHovered = False
        close_button.hoverChange()
        
        # After unhover
        self.assertEqual(close_button.image.get_at((0, 0)), (32, 32, 32, 0))