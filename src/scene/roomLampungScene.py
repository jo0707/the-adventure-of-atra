import pygame

from src.components.radenintan2 import RadenIntan2
from src.components.atra import Atra
from src.scene.scene import Scene
from src.utils.screenHelper import ScreenHelper
from src.utils.eventHelper import EventHelper

class RoomLampungScene(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.background = pygame.image.load("assets/images/backgrounds/room.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))
        
        self.atra = Atra()
        self.radenintan2 = RadenIntan2(ScreenHelper.getWindowX() / 2, 40)
        self.atra.rect.bottomleft = (ScreenHelper.getWindowX() / 2, ScreenHelper.getWindowY())
        self.sprites.add(self.radenintan2, self.atra)
    
    def onKeyDown(self, keys):
        self.atra.onKeyDown(keys)
    
    def onEvent(self, event):
        pass
    
    def onClick(self, position: tuple[int, int]):
        pass
    
    def display(self):
        self.screen.blit(self.background, (0, 0))
        self.sprites.draw(self.screen)
    
    def update(self):
        for sprite in self.sprites:
            sprite.update()
        if pygame.sprite.collide_rect(self.atra, self.radenintan2):
            pass
            
        if self.atra.rect.top > ScreenHelper.getWindowY():
            self.switchSceneEvent(EventHelper.EVENT_SCENELOBBYLEFT)