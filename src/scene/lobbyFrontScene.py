import pygame

from src.components.frontLeftTable import FrontLeftTable
from src.components.frontRightTable import FrontRightTable
from src.components.atra import Atra
from src.components.wallText import WallText
from src.components.staff import Staff
from src.scene.scene import Scene
from src.utils.screenHelper import ScreenHelper
from src.utils.eventHelper import EventHelper

class LobbyFrontScene(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.background = pygame.image.load("assets/images/backgrounds/lobbyFront.png")
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))

        self.walltext1= WallText(330, 70)
        self.walltext2= WallText(845, 70)

        self.staff1 = Staff(200, 550, "up")
        self.staff2 = Staff(972, 550, "left")

        self.atra = Atra()
        self.frontLeftTable = FrontLeftTable(0, ScreenHelper.getWindowY())
        self.frontRightTable = FrontRightTable(ScreenHelper.getWindowX(), ScreenHelper.getWindowY())
        self.atra.rect.bottomleft = (ScreenHelper.getWindowX() / 2, ScreenHelper.getWindowY())
        self.sprites.add(self.atra, self.frontLeftTable, self.frontRightTable, self.walltext1, self.walltext2, self.staff1, self.staff2)
    
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
            self.switchSceneEvent(EventHelper.EVENT_SCENELOBBYMIDDLE)
        if self.atra.rect.top > ScreenHelper.getWindowY():
            self.switchSceneEvent(EventHelper.EVENT_SCENEGAME)