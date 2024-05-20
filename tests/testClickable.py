import unittest
import pygame
from src.components.clickable import Clickable

class TestClickable(unittest.TestCase):
    
    def setUp(self):
        self.position = (100, 100)
        self.size = (50, 50)
        # Create a subclass of Clickable for testing
        class TestClickableSubclass(Clickable):
            def onClick(self):
                pass
        
        self.clickable = TestClickableSubclass(self.position, self.size)

    def test_isClicked_inside(self):
        click_position = (110, 110)
        is_clicked = self.clickable.isClicked(click_position)
        self.assertTrue(is_clicked, "Click should be detected inside the clickable area")
        
    def test_isClicked_outside(self):
        click_position = (200, 200)
        is_clicked = self.clickable.isClicked(click_position)
        self.assertFalse(is_clicked, "Click should not be detected outside the clickable area")
        
    def test_isClicked_edge(self):
        click_position = (100, 100)
        is_clicked = self.clickable.isClicked(click_position)
        self.assertTrue(is_clicked, "Click should be detected on the edge of the clickable area")
        
    def test_onClick_abstract_method(self):
        with self.assertRaises(TypeError):
            class InvalidClickable(Clickable):
                pass
            InvalidClickable(self.position, self.size)
