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
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.background = pygame.image.load("assets/images/backgrounds/lobbyMiddle.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))
        
        self.atra = Atra()
        self.atra.placeBottom()
        self.sumateraStatue = SumaterStatue(ScreenHelper.getWindowX() / 2, ScreenHelper.getWindowY() / 2)
        self.wallMap = WallMap(179, 40)
        self.wallText = WallText(829, 71)
        self.visitor1 = Visitor1(900, 600)
        self.visitor3 = Visitor3(250, 85)
        self.visitor2 = Visitor2(900, 200)
        self.staff = Staff(900, 90)
        self.sprites.add(self.sumateraStatue, self.wallMap, self.wallText, self.staff, self.visitor2, self.visitor3, self.visitor1, self.atra)
    
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
            self.switchSceneEvent(EventHelper.EVENT_SCENEROOMSUMATERAUTARA)
        if self.atra.rect.bottom > ScreenHelper.getWindowY():
            self.switchSceneEvent(EventHelper.EVENT_SCENELOBBYFRONT)
        if self.atra.rect.left < 0:
            self.switchSceneEvent(EventHelper.EVENT_SCENELOBBYLEFT)
        if self.atra.rect.right > ScreenHelper.getWindowX():
            self.switchSceneEvent(EventHelper.EVENT_SCENELOBBYRIGHT)