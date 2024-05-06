import pygame

from src.components.sumateraStatue import SumaterStatue
from src.components.atra import Atra
from src.scene.scene import Scene
from src.utils.screenHelper import ScreenHelper
from src.utils.eventHelper import EventHelper

class LobbyMiddleScene(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.background = pygame.image.load("assets/images/backgrounds/lobbyMiddle.png")
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))
        
        self.atra = Atra()
        self.sumateraStatue = SumaterStatue(ScreenHelper.getWindowX() / 2, ScreenHelper.getWindowY() / 2)
        self.atra.rect.bottomleft = (ScreenHelper.getWindowX() / 2, ScreenHelper.getWindowY())
        self.sprites.add(self.atra, self.sumateraStatue)
    
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
        if self.atra.rect.top < 0:
            self.switchSceneEvent(EventHelper.EVENT_SCENEROOMSUMATERAUTARA)
        if self.atra.rect.bottom > ScreenHelper.getWindowY():
            self.switchSceneEvent(EventHelper.EVENT_SCENELOBBYFRONT)
        if self.atra.rect.left < 0:
            self.switchSceneEvent(EventHelper.EVENT_SCENELOBBYLEFT)
        if self.atra.rect.right > ScreenHelper.getWindowX():
            self.switchSceneEvent(EventHelper.EVENT_SCENELOBBYRIGHT)