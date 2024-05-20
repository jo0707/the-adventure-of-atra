import os
import unittest

import pygame

from src.components.movable import Movable

class TestAssets(unittest.TestCase):
    provinces = ["lampung", "sumateraUtara", "sumateraBarat"]
    
    # check if all file names inside assets/images/components/{province} is exists in assets/images/real/{province}
    def testRealAssets(self):
        for province in TestAssets.provinces:
            components = os.listdir(f"assets/images/components/{province}")
            real = os.listdir(f"assets/images/real/{province}")
            for component in components:
                print(f"Checking {component} in {province}...")
                self.assertTrue(component in real)
            for r in real:
                print(f"Checking {r} in {province}...")
                self.assertTrue(r in components)