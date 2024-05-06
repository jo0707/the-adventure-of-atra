import pygame

from src.components.pillar import Pillar
from src.components.atra import Atra
from src.scene.scene import Scene
from src.utils.screenHelper import ScreenHelper
from src.utils.eventHelper import EventHelper

class OutdoorScene(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.background = pygame.image.load("assets/images/backgrounds/outdoor.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))
        self.pillarTopLeftPositions = ((0, 234), (392, 234), (800, 234), (1198, 234), (392, 509), (800, 509))
        
        self.atra = Atra()
        self.atra.rect.bottomleft = (ScreenHelper.getWindowX() / 2, ScreenHelper.getWindowY())
        
        self.sprites.add(self.atra)
        self.pillarSprites = pygame.sprite.Group()
        for coordinate in self.pillarTopLeftPositions:
            pillar = Pillar(coordinate[0], coordinate[1])
            self.sprites.add(pillar)
            self.pillarSprites.add(pillar)
    
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
            self.switchSceneEvent(EventHelper.EVENT_SCENELOBBYFRONT)