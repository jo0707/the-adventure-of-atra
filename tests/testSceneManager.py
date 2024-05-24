
import unittest

from src.scene.sceneManager import SceneManager
from tests.tools import getScreen

class TestSceneManager(unittest.TestCase):
    def setUp(self):
        self.sceneManager = SceneManager(getScreen())
    
    def test_initialization(self):
        self.assertTrue(hasattr(self.sceneManager, "screen"))
        self.assertTrue(hasattr(self.sceneManager, "currentScene"))
        self.assertTrue(hasattr(self.sceneManager, "lastSceneEvent"))   
        
    def test_methods(self):
        self.assertTrue(hasattr(self.sceneManager, "onEvent"))
        self.assertTrue(hasattr(self.sceneManager, "onKeyDown"))
        self.assertTrue(hasattr(self.sceneManager, "onTick"))
        self.assertTrue(hasattr(self.sceneManager, "onClick"))