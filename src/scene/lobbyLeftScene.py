import pygame

from src.components.atra import Atra
from src.scene.scene import Scene
from src.utils.screenHelper import ScreenHelper
from src.utils.eventHelper import EventHelper

class LobbyLeftScene(Scene):
    def __init__(self, screen: pygame.Surface, lastSceneEvent: int):
        super().__init__(screen)
        self.lastSceneEvent = lastSceneEvent
        self.background = pygame.image.load("assets/images/backgrounds/lobbyLeft.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))
        
        self.atra = Atra()
        self.atra.placeRight()
        self.sprites.add(self.atra)
        self.initializeWalls()
        self.setAtraPosition()
    
    def initializeWalls(self):
        self.atra.addClampObstacle(self.background.get_rect())
        self.addLevelRect(EventHelper.EVENT_SCENEROOMLAMPUNG, 506, 0, 265, 1)
        self.addLevelRect(EventHelper.EVENT_SCENELOBBYMIDDLE, ScreenHelper.getWindowX()-1, 185, 1, 498)
        self.leftWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 28, ScreenHelper.getWindowY()))
        self.bottomWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, ScreenHelper.getWindowY() - 36, ScreenHelper.getWindowX(), 36))
        self.leftTopWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 490, 60))
        self.rightTopWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(790, 0, 490, 60))
        
        self.atra.addObstacles([self.leftWall, self.bottomWall, self.leftTopWall, self.rightTopWall])
    
    def setAtraPosition(self):
        if self.lastSceneEvent == EventHelper.EVENT_SCENEROOMLAMPUNG:
            self.atra.placeTop()
        if self.lastSceneEvent == EventHelper.EVENT_SCENELOBBYMIDDLE:
            self.atra.placeRight()
    
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
        for event, rect in self.nextSceneRects.items():
            if self.atra.rect.colliderect(rect):
                self.switchSceneEvent(event)