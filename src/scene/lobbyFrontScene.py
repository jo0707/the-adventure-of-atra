import pygame

from src.components.frontLeftTable import FrontLeftTable
from src.components.frontRightTable import FrontRightTable
from src.components.atra import Atra
from src.components.wallText import WallText
from src.components.staff import Staff
from src.scene.gameScene import GameScene
from src.utils.screenHelper import ScreenHelper
from src.utils.eventHelper import EventHelper

class LobbyFrontScene(GameScene):
    def __init__(self, screen: pygame.Surface, lastSceneEvent: int):
        super().__init__(screen, "assets/images/backgrounds/lobbyFront.png")
        self.lastSceneEvent = lastSceneEvent
        
        self.walltext1= WallText(330, 70)
        self.walltext2= WallText(845, 70)

        self.staff1 = Staff(200, 550, "up")
        self.staff2 = Staff(972, 550, "left")

        self.atra = Atra()
        self.frontLeftTable = FrontLeftTable(0, ScreenHelper.getWindowY())
        self.frontRightTable = FrontRightTable(ScreenHelper.getWindowX(), ScreenHelper.getWindowY())
        self.atra.placeBottom()
        
        self.sprites.add(self.walltext1, self.walltext2, self.atra, self.frontLeftTable, self.frontRightTable, self.staff1, self.staff2)
        self.initializeWalls()
        self.setAtraPosition()
    
    def initializeWalls(self):
        self.atra.addClampObstacle(self.background.get_rect())
        self.addLevelRect(EventHelper.EVENT_SCENELOBBYMIDDLE, 506, 0, 265, 1)
        self.addLevelRect(EventHelper.EVENT_SCENEGAME, 480, ScreenHelper.getWindowY() - 1, 295, 1)
        self.leftWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 505, 60))
        self.rightWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(770, 0, 530, 60))
        self.leftStair = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 290, 225))
        self.rightStair = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(987, 0, 290, 225))
        self.atra.addObstacles([self.frontLeftTable.copyRect(0.8), self.frontRightTable.copyRect(0.8), self.leftWall, self.rightWall, self.leftStair, self.rightStair])
    
    def setAtraPosition(self):
        if self.lastSceneEvent == EventHelper.EVENT_SCENEGAME:
            self.atra.placeBottom()
        if self.lastSceneEvent == EventHelper.EVENT_SCENELOBBYMIDDLE:
            self.atra.placeTop()
    
    def onKeyDown(self, keys):
        self.atra.onKeyDown(keys)
    
    def onEvent(self, event):
        pass
    
    def onClick(self, position: tuple[int, int]):
        pass
    
    def display(self):
        super().display()
    
    def update(self):
        super().update()