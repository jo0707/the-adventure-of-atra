import pygame

from src.components.atra import Atra
from src.components.badakStatue import BadakStatue
from src.components.logoSumateraBarat import LogoSumateraBarat
from src.scene.scene import Scene
from src.utils.screenHelper import ScreenHelper
from src.utils.eventHelper import EventHelper

class LobbyRightScene(Scene):
    def __init__(self, screen: pygame.Surface, lastSceneEvent: int):
        super().__init__(screen)
        self.lastSceneEvent = lastSceneEvent
        self.background = pygame.image.load("assets/images/backgrounds/lobbyRight.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))
        
        self.atra = Atra()
        self.atra.placeLeft()
        self.badakStatue = BadakStatue(ScreenHelper.getWindowX() / 2 ,ScreenHelper.getWindowY() / 2)
        self.logoSumateraBarat = LogoSumateraBarat(950, 30)
        self.sprites.add(self.badakStatue, self.logoSumateraBarat, self.atra)
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
