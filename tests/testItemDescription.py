# import unittest
# import pygame
# from src.components.interactableItem import InteractableItem
# from src.components.itemDescription import ItemDetail

# class TestItemDetail(unittest.TestCase):
#     def setUp(self):
#         pygame.init()

#     def test_initialization(self):
#         item = InteractableItem("assets/images/components/pillar.png", "This is a test item", "pillar")
#         item_detail = ItemDetail(100, 100, item)

#         self.assertEqual(item_detail.width, 1024)
#         self.assertEqual(item_detail.height, 575)
#         self.assertIsInstance(item_detail.grayBackground, pygame.Surface)
#         self.assertIsInstance(item_detail.background, pygame.sprite.Sprite)
#         self.assertIsInstance(item_detail.image, pygame.sprite.Sprite)
#         self.assertIsInstance(item_detail.closeButton, pygame.sprite.Sprite)
#         self.assertIsInstance(item_detail.titleTextbox, pygame.sprite.Sprite)
#         self.assertIsInstance(item_detail.descriptionSurface, pygame.Surface)
#         self.assertIsInstance(item_detail.descriptionRect, pygame.Rect)
#         self.assertIsInstance(item_detail.descriptionTextbox, pygame.sprite.Sprite)

#     def tearDown(self):
#         pygame.quit()
