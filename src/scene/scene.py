from abc import ABC, abstractmethod
from typing import List
import pygame

from src.components.textbox import Textbox
from src.utils.eventHelper import EventHelper

class Scene(ABC):
    def __init__(self, screen: pygame.Surface):
        self.sprites = pygame.sprite.Group()
        self.textboxes: List[Textbox] = []
        self.screen = screen
        
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

    @abstractmethod
    def update(self):
        pass

    def switchSceneEvent(self, nextSceneEvent: int):
        EventHelper.postEvent(nextSceneEvent)
