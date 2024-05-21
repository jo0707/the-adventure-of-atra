import pygame

from src.scene.scene import Scene
from src.components.button import Button
from src.components.clickable import Clickable
from src.components.textbox import Textbox
from src.utils.fontHelper import FontHelper
from src.utils.screenHelper import ScreenHelper
from src.utils.eventHelper import EventHelper

class EndEcene(Scene):
    def __init__(self, screen: pygame.Surface, lastSceneEvent: int):
        super().__init__(screen)
        self.lastSceneEvent = lastSceneEvent
        self.background = pygame.image.load("assets/images/backgrounds/end.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))
        
    def onKeyDown(self, keys):
        pass
    
    def onEvent(self, event):
        pass
    
    def onClick(self, position: tuple[int, int]):
        for sprite in self.sprites:
            if sprite.rect.collidepoint(position) and isinstance(sprite, Clickable):
                sprite.onClick()
    
    def display(self):
        self.screen.blit(self.background, (0, 0))
        self.sprites.draw(self.screen)
    
    def update(self):
        self.sprites.update()
    