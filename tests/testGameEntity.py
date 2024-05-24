import random
import unittest

from src.components.gameEntity import GameEntity

class TestGameEntity(unittest.TestCase):
    imagePath = "assets/images/components/pillar.png"

    def testInitialization(self):
        gameEntity = GameEntity(TestGameEntity.imagePath)
        self.assertEqual(gameEntity.imagePath, TestGameEntity.imagePath)
        self.assertEqual(gameEntity.image.get_rect().topleft, (0, 0))
        
    def testMethods(self):
        self.assertTrue(hasattr(GameEntity, "update"))
        self.assertTrue(hasattr(GameEntity, "scaleByHeight"))
        self.assertTrue(hasattr(GameEntity, "scaleByWidth"))
        self.assertTrue(hasattr(GameEntity, "copyRect"))
    
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
        
    def testCopyRect(self):
        gameEntity = GameEntity(TestGameEntity.imagePath)
        heightFactor = random.random()
        bottomOffset = random.randint(0, 100)
        rectCopy = gameEntity.copyRect(heightFactor, bottomOffset)
        self.assertAlmostEqual(rectCopy.height, gameEntity.rect.height * heightFactor, delta=10)
        self.assertEqual(rectCopy.bottom, gameEntity.rect.bottom - bottomOffset)