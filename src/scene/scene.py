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
        self.nextSceneRects: dict[int, pygame.rect.Rect] = {}
        
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
    
    # create a popup that receive text and image path to display
    # darken the background1
    def showPopup(self, text: str, imagePath: str):
        self.textboxes.append(Textbox(text, imagePath))
        image = pygame.image.load(imagePath).convert_alpha()
        
            
    def addLevelRect(self, event: int, x: int, y: int, width: int, height: int):
        self.nextSceneRects[event] = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(x, y, width, height))

    def switchSceneEvent(self, nextSceneEvent: int):
        EventHelper.postEvent(nextSceneEvent)
        
    def changeMusic(self, musicName: str):
        pygame.mixer.music.load(f"assets/sounds/{musicName}")
        pygame.mixer.music.set_volume(0.5)
        pygame.mixer.music.play(-1)
