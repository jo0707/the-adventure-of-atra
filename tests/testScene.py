
import unittest

from src.scene.scene import Scene
from tests.tools import getScreen

class MockScene(Scene):
    def onEvent(self, event):
        pass

    def onKeyDown(self, keys):
        pass

    def onClick(self, position):
        pass

    def display(self):
        pass

    def update(self):
        pass

class TestScene(unittest.TestCase):
    def setUp(self):
        self.scene = MockScene(getScreen())
    
    def test_initialization(self):
        self.assertTrue(hasattr(self.scene, "screen"))
        self.assertTrue(hasattr(self.scene, "sprites"))
        self.assertTrue(hasattr(self.scene, "textboxes"))
    
    def test_methods(self):
        self.assertTrue(hasattr(self.scene, "onEvent"))
        self.assertTrue(hasattr(self.scene, "onKeyDown"))
        self.assertTrue(hasattr(self.scene, "onClick"))
        self.assertTrue(hasattr(self.scene, "display"))
        self.assertTrue(hasattr(self.scene, "update"))
        self.assertTrue(hasattr(self.scene, "switchSceneEvent"))
        self.assertTrue(hasattr(self.scene, "changeMusic"))
        