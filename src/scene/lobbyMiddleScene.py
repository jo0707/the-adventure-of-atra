import pygame

from src.components.visitor1 import Visitor1
from src.components.staff import Staff
from src.components.visitor2 import Visitor2
from src.components.visitor3 import Visitor3
from src.components.wallMap import WallMap
from src.components.wallText import WallText
from src.components.sumateraStatue import SumaterStatue
from src.components.atra import Atra
from src.scene.scene import Scene
from src.utils.screenHelper import ScreenHelper
from src.utils.eventHelper import EventHelper

class LobbyMiddleScene(Scene):
    def __init__(self, screen: pygame.Surface, lastSceneEvent: int):
        super().__init__(screen)
        self.lastSceneEvent = lastSceneEvent
        self.background = pygame.image.load("assets/images/backgrounds/lobbyMiddle.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))
        print()
        
        self.atra = Atra()
        self.atra.placeBottom()
        self.sumateraStatue = SumaterStatue(ScreenHelper.getWindowX() / 2, ScreenHelper.getWindowY() / 2, )
        self.wallMap = WallMap(179, 40)
        self.wallText = WallText(829, 71)
        self.visitor1 = Visitor1(900, 600)
        self.visitor3 = Visitor3(250, 85)
        self.visitor2 = Visitor2(900, 200)
        self.staff = Staff(900, 90)
        self.sprites.add(self.sumateraStatue, self.wallMap, self.wallText, self.staff, self.visitor2, self.visitor3, self.visitor1, self.atra)
        self.itemSprites.add(self.sumateraStatue, self.wallMap)
        self.initializeWalls()
        self.setAtraPosition()
    
    def initializeWalls(self):
        self.atra.addClampObstacle(self.background.get_rect())
        self.addLevelRect(EventHelper.EVENT_SCENEROOMSUMATERAUTARA, 506, 0, 265, 1)
        self.addLevelRect(EventHelper.EVENT_SCENELOBBYLEFT, 0, 185, 1, 498)
        self.addLevelRect(EventHelper.EVENT_SCENELOBBYRIGHT, ScreenHelper.getWindowX()-1, 185, 1, 498)
        self.addLevelRect(EventHelper.EVENT_SCENELOBBYFRONT, 480, ScreenHelper.getWindowY() - 1, 295, 1)
        self.leftBottomWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, ScreenHelper.getWindowY() - 36, 490, 36))
        self.rightBottomWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(790, ScreenHelper.getWindowY() - 36, 490, 36))
        self.leftTopWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 490, 60))
        self.rightTopWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(790, 0, 490, 60))
        
        self.atra.addObstacles([self.leftBottomWall, self.rightBottomWall, self.leftTopWall, self.rightTopWall, self.sumateraStatue.copyRect(0.1, 100)])
    
    def setAtraPosition(self):
        if self.lastSceneEvent == EventHelper.EVENT_SCENELOBBYFRONT:
            self.atra.placeBottom()
        if self.lastSceneEvent == EventHelper.EVENT_SCENEROOMSUMATERAUTARA:
            self.atra.placeTop()
        if self.lastSceneEvent == EventHelper.EVENT_SCENELOBBYLEFT:
            self.atra.placeLeft()
        if self.lastSceneEvent == EventHelper.EVENT_SCENELOBBYRIGHT:
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
                
        # collided items always instance of InteractableItem
        collidedItem = pygame.sprite.spritecollideany(self.atra, self.itemSprites)
        if collidedItem is not None:
            collidedItem.onPlayerCollision(True)
        elif self.lastCollidedItem is not None:
            self.lastCollidedItem.onPlayerCollision(False)
        self.lastCollidedItem = collidedItem
