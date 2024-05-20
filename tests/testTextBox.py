# import unittest
# import pygame
# from src.utils.fontHelper import FontHelper
# from src.components.textbox import Textbox

# class TestTextbox(unittest.TestCase):
#     def setUp(self):
#         pygame.init()
#         pygame.font.init()
#         FontHelper.initFonts()  # Assuming this method loads necessary fonts
        
#     def testInitialization(self):
#         text = "Hello, World!"
#         x = 50
#         y = 100
#         size = 24
#         color = pygame.Color("white")
#         font = pygame.font.SysFont(None, size)
#         bgColor = None
#         wrap = False
        
#         textbox = Textbox(text, x, y, size, color, font, bgColor, wrap)
        
#         self.assertEqual(textbox._Textbox__text, text)  # Accessing private attribute directly
#         self.assertEqual(textbox.x, x)
#         self.assertEqual(textbox.y, y)
#         self.assertEqual(textbox.size, size)
#         self.assertEqual(textbox.color, color)
#         self.assertEqual(textbox.wrap, wrap)
#         self.assertIsNotNone(textbox.font)
#         self.assertIsNotNone(textbox.surf)
#         self.assertIsNotNone(textbox.rect)
#         self.assertEqual(textbox.rect.topleft, (x, y))
        
#     def testSetText(self):
#         textbox = Textbox()
#         new_text = "New Text"
#         textbox.setText(new_text)
#         self.assertEqual(textbox._Textbox__text, new_text)  # Accessing private attribute directly
        
#     def testRenderWrappedText(self):
#         surface = pygame.Surface((400, 200))
#         textbox = Textbox("This is a long text that should be wrapped", 10, 10, 24, pygame.Color("white"), None, None, True)
#         textbox._Textbox__renderWrappedText(surface)  # Using underscore to access private method
        
#         # Your assertions for the rendering outcome go here
#         # Example:
#         # self.assertEqual(...)
#         # self.assertTrue(...)
#         # self.assertFalse(...)