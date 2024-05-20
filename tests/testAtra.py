# import unittest
# import pygame
# from src.components.atra import Atra

# class TestAtra(unittest.TestCase):

#     def setUp(self):
#         pygame.init()
#         self.atra = Atra()

#     def test_initialization(self):
#         self.assertEqual(self.atra.isKeyDown, False)
#         self.assertEqual(len(self.atra.obstacles), 0)
#         self.assertEqual(len(self.atra.clamps), 0)
#         self.assertEqual(self.atra.firstTickColliding, False)

#     def test_onKeyDown_moveDown(self):
#         keys = {pygame.K_DOWN: True, pygame.K_UP: False, pygame.K_LEFT: False, pygame.K_RIGHT: False}
#         originalX, originalY = self.atra.rect.x, self.atra.rect.y
#         self.atra.onKeyDown(keys)
#         self.assertTrue(self.atra.isKeyDown)
#         self.assertEqual(self.atra.currentDirection, "down")
#         self.assertNotEqual(self.atra.rect.x, originalX)
#         self.assertNotEqual(self.atra.rect.y, originalY)

#     def test_onKeyDown_collision(self):
#         # Assuming an obstacle is added at (100, 100) with a size of 50x50
#         obstacle = pygame.Rect(100, 100, 50, 50)
#         self.atra.addObstacle(obstacle)
#         keys = {pygame.K_DOWN: True, pygame.K_UP: False, pygame.K_LEFT: False, pygame.K_RIGHT: False}
#         originalX, originalY = self.atra.rect.x, self.atra.rect.y
#         self.atra.onKeyDown(keys)
#         self.assertFalse(self.atra.isKeyDown)
#         self.assertEqual(self.atra.currentDirection, "down")
#         self.assertEqual(self.atra.rect.x, originalX)
#         self.assertEqual(self.atra.rect.y, originalY)

#     def tearDown(self):
#         pygame.quit()
