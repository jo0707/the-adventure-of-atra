# import unittest
# import pygame
# from unittest.mock import MagicMock

# from src.components.button import Button

# class TestButton(unittest.TestCase):

#     def setUp(self):
#         pygame.init()
#         self.font = pygame.font.Font(None, 24)  # Use a default font for testing
#         self.button = Button(100, 100, 200, 50, "Button", self.font)

#     def tearDown(self):
#         pygame.quit()

#     def test_init(self):
#         self.assertEqual(self.button.rect.topleft, (100, 100))
#         self.assertEqual(self.button.rect.size, (200, 50))
#         self.assertEqual(self.button.textbox.text, "Button")
#         self.assertEqual(self.button.textColor, pygame.Color("white"))
#         self.assertEqual(self.button.textHoverColor, pygame.Color("slategray"))

#     def test_update(self):
#         # Simulate a mouse hover
#         self.button.getHoverState = MagicMock(return_value=True)
#         self.button.update()
#         self.assertTrue(self.button.isHovered)
#         # Simulate a mouse not hovering
#         self.button.getHoverState = MagicMock(return_value=False)
#         self.button.update()
#         self.assertFalse(self.button.isHovered)

#     def test_onClick(self):
#         # Mock the action method
#         self.button.action = MagicMock()
#         self.button.onClick()
#         self.button.action.assert_called_once()

#     def test_setText(self):
#         new_text = "New Button"
#         self.button.setText(new_text)
#         self.assertEqual(self.button.textbox.text, new_text)

#     def test_getHoverState(self):
#         # Test mouse position inside the button
#         pygame.mouse.get_pos = MagicMock(return_value=(150, 125))
#         self.assertTrue(self.button.getHoverState())
#         # Test mouse position outside the button
#         pygame.mouse.get_pos = MagicMock(return_value=(50, 50))
#         self.assertFalse(self.button.getHoverState())

# if __name__ == "__main__":
#     unittest.main()
