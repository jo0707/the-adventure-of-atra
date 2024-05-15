import pygame

from src.components.lampung.radenIntan2Lampung import RadenIntan2Lampung
from src.components.lampung.kerisLampung import KerisLampung
from src.components.lampung.prasastiBungkukLampung import PrasastiBungkukLampung
from src.components.lampung.prasastiDadakLampung import PrasastiDadakLampung
from src.components.lampung.sigerLampung import SigerLampung
from src.components.lampung.tapisLampung import TapisLampung
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
        self.atra.placeBottom()
        self.tapisLampung = TapisLampung(125, 40)
        self.radenintan2 = RadenIntan2Lampung(935, 30)
        self.prasastiDadakLampung = PrasastiDadakLampung(130, 256)
        self.prasastiBungkukLampung = PrasastiBungkukLampung(130, 425)
        self.sigerLampung = SigerLampung(505, 210)
        self.kerisLampung = KerisLampung(1067, 198)
        self.kerisLampung2 = KerisLampung(1067, 425)
        self.sprites.add(self.tapisLampung,  self.radenintan2, self.atra, self.prasastiDadakLampung, self.prasastiBungkukLampung, self.kerisLampung, self.kerisLampung2, self.sigerLampung)
        self.initializeWalls()
        self.initializeObstacle()
        self.changeMusic("tabuhSanakLampung.mp3")
    
    def initializeWalls(self):
        self.atra.addClampObstacle(self.background.get_rect())
        self.addLevelRect(EventHelper.EVENT_SCENELOBBYLEFT, 490, ScreenHelper.getWindowY() - 1, 300, 1)
        self.leftWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 28, ScreenHelper.getWindowY()))
        self.rightWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(ScreenHelper.getWindowX()-28, 0, 28, ScreenHelper.getWindowY()))
        self.leftBottomWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, ScreenHelper.getWindowY() - 36, 490, 36))
        self.rightBottomWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(790, ScreenHelper.getWindowY() - 36, 490, 36))
        self.topWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, ScreenHelper.getWindowX(), 60))
        self.atra.addObstacles([self.leftWall, self.rightWall, self.leftBottomWall, self.rightBottomWall, self.topWall])

    def initializeObstacle(self):
        self.atra.addObstacles([
            # self.tapisLampung.copyRect(0.6), 
            # self.radenintan2.copyRect(0.6), 
            self.prasastiDadakLampung.copyRect(0.4), 
            self.prasastiBungkukLampung.copyRect(0.4), 
            self.kerisLampung.copyRect(0.4), 
            self.kerisLampung2.copyRect(0.4), 
            self.sigerLampung.copyRect(0.4)
        ])
    
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