import pygame

from src.components.atra import Atra
from src.components.badakStatue import BadakStatue
from src.components.logoSumateraBarat import LogoSumateraBarat
from src.components.kursi import Kursi
from src.scene.gameScene import GameScene
from src.utils.screenHelper import ScreenHelper
from src.utils.eventHelper import EventHelper

class LobbyRightScene(GameScene):
    def __init__(self, screen: pygame.Surface, lastSceneEvent: int):
        super().__init__(screen, "assets/images/backgrounds/lobbyRight.png")
        self.lastSceneEvent = lastSceneEvent
        
        self.atra = Atra()
        self.atra.placeLeft()
        self.badakStatue = BadakStatue(ScreenHelper.getWindowX() / 2 ,ScreenHelper.getWindowY() / 2)
        self.logoSumateraBarat = LogoSumateraBarat(950, 30)
        self.kursi1 = Kursi(72, 556)
        self.kursi2 = Kursi(924, 556)
        self.sprites.add(self.badakStatue, self.logoSumateraBarat, self.kursi1, self.kursi2, self.atra)
        self.itemSprites.add(self.badakStatue, self.logoSumateraBarat)
        self.initializeWalls()
        self.setAtraPosition()
    
    def initializeWalls(self):
        self.atra.addClampObstacle(self.background.get_rect())
        self.addLevelRect(EventHelper.EVENT_SCENEROOMSUMATERABARAT, 506, 0, 265, 1)
        self.addLevelRect(EventHelper.EVENT_SCENELOBBYMIDDLE, 0, 185, 1, 498)
        self.rightWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(ScreenHelper.getWindowX() - 28, 0, 28, ScreenHelper.getWindowY()))
        self.bottomWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, ScreenHelper.getWindowY() - 36, ScreenHelper.getWindowX(), 36))
        self.leftTopWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 490, 60))
        self.rightTopWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(790, 0, 490, 60))
        
        self.atra.addObstacles([self.rightWall, self.bottomWall, self.leftTopWall, self.rightTopWall, self.badakStatue.copyRect(0.1, 100)])
        
    def setAtraPosition(self):
        if self.lastSceneEvent == EventHelper.EVENT_SCENEROOMSUMATERABARAT:
            self.atra.placeTop()
        if self.lastSceneEvent == EventHelper.EVENT_SCENELOBBYMIDDLE:
            self.atra.placeLeft()
    
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