# import unittest
# import pygame
# from unittest.mock import patch

# # Import the necessary classes from your source code
# from src.components.itemPreview import ItemPreview
# from src.components.interactableItem import InteractableItem

# class TestItemPreview(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         pygame.init()

#     @classmethod
#     def tearDownClass(cls):
#         pygame.quit()

#     def setUp(self):
#         # Use a mock image path for testing
#         self.item = InteractableItem("item_id", "Item Name", "mock_image.png")
#         self.preview = ItemPreview(100, 100, self.item)

#     def test_init(self):
#         # Test the initialization of ItemPreview
#         self.assertEqual(self.preview.x, 100)
#         self.assertEqual(self.preview.y, 100)
#         self.assertEqual(self.preview.width, 600)
#         self.assertEqual(self.preview.height, 180)
#         # Add more assertions as needed

#     def test_draw(self):
#         # Test the draw method of ItemPreview
#         surface = pygame.Surface((800, 600))
#         self.preview.draw(surface)
#         # Add assertions for drawing logic

# if __name__ == "__main__":
#     unittest.main()
