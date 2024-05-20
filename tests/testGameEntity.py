import random
import unittest

from src.components.gameEntity import GameEntity

class TestGameEntity(unittest.TestCase):
    imagePath = "assets/images/components/pillar.png"

    # created GameEntity object must have rect with desired width and height
    def testWidthHeightInitialization(self):
        width = random.randint(0, 1280)
        height = random.randint(0, 720)
        gameEntity = GameEntity(TestGameEntity.imagePath, width=width, height=height)
        self.assertEqual(gameEntity.rect.width, width)
        self.assertEqual(gameEntity.rect.height, height)
        
    # create GameEntity object with only width parameter, height should be scaled accordingly
    def testWidthInitialization(self):
        width = random.randint(0, 1280)
        gameEntity = GameEntity(TestGameEntity.imagePath, width=width)
        self.assertEqual(gameEntity.rect.width, width)
        
    # create GameEntity object with only height parameter, width should be scaled accordingly
    def testHeightInitialization(self):
        height = random.randint(0, 720)
        gameEntity = GameEntity(TestGameEntity.imagePath, height=height)
        self.assertEqual(gameEntity.rect.height, height)