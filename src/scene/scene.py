from abc import ABC, abstractmethod
from typing import List
import pygame

from src.components.itemPreview import ItemPreview
from src.components.interactableItem import InteractableItem
from src.components.textbox import Textbox
from src.utils.eventHelper import EventHelper

"""
Scene class defines the structure of a scene
Scene class is an abstract class that defines the structure of a scene
Scene class will have all the same methods that will be implemented by the child class
"""

class Scene(ABC):
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        # contains all sprites in scene
        self.sprites = pygame.sprite.Group()
        # contains all textboxes in scene
        self.textboxes: List[Textbox] = []
        
    @abstractmethod
    def onEvent(self, event: pygame.event.Event):
        pass
    
    @abstractmethod
    def onKeyDown(self, keys):
        pass

    @abstractmethod
    def onClick(self, position: tuple[int, int]):
        pass

    @abstractmethod
    def display(self):
        pass

    # update method is used to update the sprites condition and textboxes
    # this method only updates the sprites and textboxes logic
    # ex: moving the sprite, changing the text, etc
    @abstractmethod
    def update(self):
        pass

    def switchSceneEvent(self, nextSceneEvent: int):
        EventHelper.postEvent(nextSceneEvent)
        
    def changeMusic(self, musicName: str, volume: float = 0.3):
        pygame.mixer.music.load(f"assets/sounds/{musicName}")
        # pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.set_volume(0)
        pygame.mixer.music.play(-1)
