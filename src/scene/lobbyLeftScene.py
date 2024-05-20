import pygame

from src.components.atra import Atra
from src.components.gajahStatue import GajahStatue
from src.components.logoLampung import LogoLampung
from src.components.kursi import Kursi
from src.scene.gameScene import GameScene
from src.utils.screenHelper import ScreenHelper
from src.utils.eventHelper import EventHelper

class LobbyLeftScene(GameScene):
    def __init__(self, screen: pygame.Surface, lastSceneEvent: int):
        super().__init__(screen, "assets/images/backgrounds/lobbyLeft.png")
        self.lastSceneEvent = lastSceneEvent
        
        self.atra = Atra()
        self.atra.placeRight()
        self.gajahStatue = GajahStatue(ScreenHelper.getWindowX() / 2, ScreenHelper.getWindowY() / 2)
        self.logoLampung = LogoLampung(950, 30)
        self.kursi1 = Kursi(72, 556)
        self.kursi2 = Kursi(924, 556)
        self.sprites.add(self.gajahStatue, self.logoLampung, self.kursi1, self.kursi2, self.atra)
        
        self.itemSprites.add(self.gajahStatue, self.logoLampung)
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
        
        self.atra.addObstacles([self.leftWall, self.bottomWall, self.leftTopWall, self.rightTopWall, self.gajahStatue.copyRect(0.1, 100)])
    
    def setAtraPosition(self):
        if self.lastSceneEvent == EventHelper.EVENT_SCENEROOMLAMPUNG:
            self.atra.placeTop()
        if self.lastSceneEvent == EventHelper.EVENT_SCENELOBBYMIDDLE:
            self.atra.placeRight()
    
    def onKeyDown(self, keys):
        self.atra.onKeyDown(keys)
        super().onKeyDown(keys)
    
    def onEvent(self, event):
        pass
    
    def onClick(self, position: tuple[int, int]):
        super().onClick(position)
    
    def display(self):
        super().display()
    
    def update(self):
        super().update()    