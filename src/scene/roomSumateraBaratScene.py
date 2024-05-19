import pygame

from src.components.sumateraBarat.tuankuImamBonjol import TuankuImamBonjol
from src.components.sumateraBarat.prasastiKuburajo import PrasastiKuburajo
from src.components.sumateraBarat.kainSongket import KainSongket
from src.components.sumateraBarat.karih import Karih
from src.components.sumateraBarat.jamGadang import JamGadang
from src.components.sumateraBarat.rumahGadang import RumahGadang
from src.components.atra import Atra
from src.scene.scene import Scene
from src.utils.screenHelper import ScreenHelper
from src.utils.eventHelper import EventHelper

class RoomSumateraBaratScene(Scene):
    def __init__(self, screen: pygame.Surface, lastSceneEvent: int):
        super().__init__(screen)
        self.lastSceneEvent = lastSceneEvent
        self.background = pygame.image.load("assets/images/backgrounds/room.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))
        
        self.atra = Atra()
        self.atra.placeBottom()
        self.portraitSumbar = TuankuImamBonjol(900, 30)
        self.prasastiKuburajo = PrasastiKuburajo(950, 200)
        self.kainSongket = KainSongket(210, 40)
        self.karih = Karih(525, 330)
        self.rumahGadang = RumahGadang(900, 418)
        self.jamGadang = JamGadang(200, 335)
        self.sprites.add(self.kainSongket, self.portraitSumbar, self.atra, self.rumahGadang, self.jamGadang, self.karih, self.prasastiKuburajo)
        self.itemSprites.add(self.kainSongket, self.portraitSumbar, self.rumahGadang, self.jamGadang, self.karih, self.prasastiKuburajo)
        self.initializeWalls()
        self.initializeObstacle()
        self.changeMusic("galombangSumateraBarat.mp3")
    
    def initializeWalls(self):
        self.atra.addClampObstacle(self.background.get_rect())
        self.addLevelRect(EventHelper.EVENT_SCENELOBBYRIGHT, 490, ScreenHelper.getWindowY() - 1, 300, 1)
        self.leftWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 28, ScreenHelper.getWindowY()))
        self.rightWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(ScreenHelper.getWindowX()-28, 0, 28, ScreenHelper.getWindowY()))
        self.leftBottomWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, ScreenHelper.getWindowY() - 36, 490, 36))
        self.rightBottomWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(790, ScreenHelper.getWindowY() - 36, 490, 36))
        self.topWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, ScreenHelper.getWindowX(), 60))
        self.atra.addObstacles([self.leftWall, self.rightWall, self.leftBottomWall, self.rightBottomWall, self.topWall])
    
    def initializeObstacle(self):
        self.atra.addObstacles([
            self.prasastiKuburajo.copyRect(0.2), 
            self.karih.copyRect(0.3, 5), 
            self.rumahGadang.copyRect(0.3, 5), 
            self.jamGadang.copyRect(0.3, 10),
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
                
        # collided items always instance of InteractableItem
        collidedItem = pygame.sprite.spritecollideany(self.atra, self.itemSprites)
        if collidedItem is not None:
            collidedItem.onPlayerCollision(True)
        elif self.lastCollidedItem is not None:
            self.lastCollidedItem.onPlayerCollision(False)
        self.lastCollidedItem = collidedItem