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

    # created GameEntity object must have rect with desired scale
    def testWidthHeightInitialization(self):
        scale = random.uniform(0, 1)
        gameEntity = GameEntity(TestGameEntity.imagePath, scale=scale)
        self.assertAlmostEqual(gameEntity.rect.width, gameEntity.image.get_width() * scale, delta=10)
        self.assertAlmostEqual(gameEntity.rect.height, gameEntity.image.get_height() * scale, delta=10)
        
    # create GameEntity object with only width parameter, height should be scaled accordingly
    def testWidthInitialization(self):
        width = random.randint(0, 1280)
        gameEntity = GameEntity(TestGameEntity.imagePath, width=width)
        self.assertEqual(gameEntity.rect.width, width)
        self.assertAlmostEqual(gameEntity.rect.height, gameEntity.image.get_height() * (width / gameEntity.image.get_width()), delta=10)
        
    # create GameEntity object with only height parameter, width should be scaled accordingly
    def testHeightInitialization(self):
        height = random.randint(0, 720)
        gameEntity = GameEntity(TestGameEntity.imagePath, height=height)
        self.assertEqual(gameEntity.rect.height, height)
        self.assertAlmostEqual(gameEntity.rect.width, gameEntity.image.get_width() * (height / gameEntity.image.get_height()), delta=10)