import pygame

from src.components.pillar import Pillar
from src.components.atra import Atra
from src.scene.gameScene import GameScene
from src.utils.eventHelper import EventHelper

class OutdoorScene(GameScene):
    def __init__(self, screen: pygame.Surface, lastSceneEvent: int):
        super().__init__(screen, "assets/images/backgrounds/outdoor.png")
        self.lastSceneEvent = lastSceneEvent
        self.pillarTopLeftPositions = ((0, 234), (392, 234), (800, 234), (1198, 234), (392, 509), (800, 509))
            
        self.atra = Atra()
        self.sprites.add(self.atra)
        self.pillarSprites = pygame.sprite.Group()
        
        self.initializeWalls()
        self.initializePillars()
        self.setAtraPosition()
        
    # creating walls and its rects for collision detection
    def initializeWalls(self):
        self.atra.addClampObstacle(self.background.get_rect())
        # create transparent box for scene transition
        self.addLevelRect(EventHelper.EVENT_SCENELOBBYFRONT, 580, 0, 120, 1)
        self.leftWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 530, 40))
        self.rightWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(750, 0, 530, 40))
        self.atra.addObstacles([self.leftWall, self.rightWall])
        
    # creating pillars and its rects for collision detection
    def initializePillars(self):
        for coordinate in self.pillarTopLeftPositions:
            pillar = Pillar(coordinate[0], coordinate[1])
            self.sprites.add(pillar)
            self.pillarSprites.add(pillar)
            self.atra.addObstacle(pillar.copyRect(0.1))
    
    def setAtraPosition(self):
        if self.lastSceneEvent == EventHelper.EVENT_SCENESTART:
            self.atra.placeBottom()
        if self.lastSceneEvent == EventHelper.EVENT_SCENELOBBYFRONT:
            self.atra.placeTop()
    
    def onKeyDown(self, keys):
        self.atra.onKeyDown(keys)
        super().onKeyDown(keys)
    
    def onEvent(self, event):
        pass
    
    def onClick(self, position: tuple[int, int]):
        pass
    
    def display(self):
        super().display()
    
    def update(self):
        super().update()