import pygame

from player import Player
from src.components.clickable import Clickable
from src.components.staffQuiz import StaffQuiz
from src.dialog.quizDialog import QuizDialog
from src.components.atra import Atra
from src.components.sumateraUtara.bajuBatakSumateraUtara import BajuBatakSumateraUtara
from src.components.sumateraUtara.kainUlosSumateraUtara import KainUlosSumateraUtara
from src.components.sumateraUtara.sisingamangaradjaSumateraUtara import SisingamangaradjaSumateraUtara
from src.components.sumateraUtara.parasastiLobuTuaSumateraUtara import PrasastiLobuTuaSumateraUtara
from src.components.sumateraUtara.prasastiBatuganaSumateraUtara import PrasastiBatuganaSumateraUtara
from src.components.sumateraUtara.pisoGajaSumateraUtara import PisoGajaSumateraUtara
from src.scene.gameScene import GameScene
from src.utils.screenHelper import ScreenHelper
from src.utils.eventHelper import EventHelper
from src.data.quiz import quizSumateraUtara

class RoomSumateraUtaraScene(GameScene):
    def __init__(self, screen: pygame.Surface, lastSceneEvent: int):
        super().__init__(screen, "assets/images/backgrounds/room.png")
        self.lastSceneEvent = lastSceneEvent
        
        self.atra = Atra()
        self.atra.placeBottom()
        
        self.quizDialog: QuizDialog | None = None
        
        self.staffQuiz = StaffQuiz(70, 100)
        self.bajuBatakSumateraUtara = BajuBatakSumateraUtara(470,180)
        self.kainUlosSumateraUtara = KainUlosSumateraUtara(935,40)
        self.sisingamangaradjaSumateraUtara = SisingamangaradjaSumateraUtara(245,30)
        self.prasastiLobuTuaSumateraUtara = PrasastiLobuTuaSumateraUtara(1000,450)
        self.prasastiBatuganaSumateraUtara = PrasastiBatuganaSumateraUtara(1000,200)
        self.pisoGajaSumateraUtara = PisoGajaSumateraUtara(100,450)
        
        self.sprites.add(self.sisingamangaradjaSumateraUtara, self.kainUlosSumateraUtara, self.atra, self.bajuBatakSumateraUtara, self.prasastiBatuganaSumateraUtara, self.prasastiLobuTuaSumateraUtara, self.pisoGajaSumateraUtara, self.staffQuiz)
        self.itemSprites.add(self.kainUlosSumateraUtara, self.sisingamangaradjaSumateraUtara, self.bajuBatakSumateraUtara, self.prasastiBatuganaSumateraUtara, self.prasastiLobuTuaSumateraUtara, self.pisoGajaSumateraUtara, self.staffQuiz)
        
        self.initializeWalls()
        self.initializeObstacle()
        self.changeMusic("oTanoBatakSumateraUtara.mp3")
    
    def initializeWalls(self):
        self.atra.addClampObstacle(self.background.get_rect())
        self.addLevelRect(EventHelper.EVENT_SCENELOBBYMIDDLE, 490, ScreenHelper.getWindowY() - 1, 300, 1)
        
        self.leftWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, 28, ScreenHelper.getWindowY()))
        self.rightWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(ScreenHelper.getWindowX()-28, 0, 28, ScreenHelper.getWindowY()))
        self.leftBottomWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, ScreenHelper.getWindowY() - 36, 490, 36))
        self.rightBottomWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(790, ScreenHelper.getWindowY() - 36, 490, 36))
        self.topWall = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(0, 0, ScreenHelper.getWindowX(), 60))
        
        self.atra.addObstacles([self.leftWall, self.rightWall, self.leftBottomWall, self.rightBottomWall, self.topWall])
    
    def initializeObstacle(self):
        self.atra.addObstacles([
            self.prasastiLobuTuaSumateraUtara.copyRect(0.3), 
            self.prasastiBatuganaSumateraUtara.copyRect(0.3), 
            self.pisoGajaSumateraUtara.copyRect(0.3), 
            self.bajuBatakSumateraUtara.copyRect(0.3)
        ])

    def onKeyDown(self, keys):
        if keys[pygame.K_e] and self.itemPreview and isinstance(self.itemPreview.interactableItem, StaffQuiz):
            def closeQuiz():
                self.quizDialog = None
            self.quizDialog = QuizDialog(128, 72, lambda: closeQuiz(), quizSumateraUtara)
            
        self.atra.onKeyDown(keys)
        super().onKeyDown(keys)
    
    def onEvent(self, event):
        pass
    
    def onClick(self, position: tuple[int, int]):
        super().onClick(position)
        if self.quizDialog:
            for sprite in self.quizDialog:
                if sprite.rect.collidepoint(position) and isinstance(sprite, Clickable):
                    sprite.onClick()
    
    def display(self):
        super().display()
        if self.quizDialog:
            self.quizDialog.draw(self.screen)
    
    def update(self):
        super().update()
        if self.quizDialog:
            self.quizDialog.update()
            if self.quizDialog.isComplete:
                Player.getPlayer().sumateraUtaraCorrectAnswers = self.quizDialog.correctAnswer