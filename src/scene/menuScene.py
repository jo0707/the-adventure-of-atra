import pygame

from src.components.button import Button
from src.components.clickable import Clickable
from src.components.textbox import Textbox
from src.scene.scene import Scene
from src.utils.fontHelper import FontHelper
from src.utils.screenHelper import ScreenHelper
from src.utils.eventHelper import EventHelper

class MenuScene(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.background = pygame.image.load("assets/images/backgrounds/menu.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))
        
        buttonX = ScreenHelper.getWindowX() // 2 - 150
        buttonY = (ScreenHelper.getWindowY() // 2) - 100
        self.title = Textbox("AdventureAtra!", font=FontHelper.fonts["title1"], size=48)
        self.title.rect.center = (ScreenHelper.getWindowX() // 2, 100)
        self.sprites.add(
            Button(
                x=buttonX,
                y=buttonY,
                width=350,
                height=100,
                text="Mulai Permainan",
                action=lambda: self.switchSceneEvent(EventHelper.EVENT_SCENELOBBYFRONT)
            ),
            Button(
                x=buttonX,
                y=buttonY + 110,
                width=350,
                height=100,
                text="Pengaturan",
                action=lambda: pygame.event.post(pygame.event.Event(EventHelper.EVENT_SCENESETTINGS)),
            ),
            Button(
                x=buttonX,
                y=buttonY + 220,
                width=350,
                height=100,
                text="Keluar",
                action=lambda: pygame.event.post(pygame.event.Event(pygame.QUIT)),
            )
        )
    
    def onKeyDown(self, keys):
        pass
    
    def onEvent(self, event):
        pass
    
    def onClick(self, position: tuple[int, int]):
        for sprite in self.sprites:
            if sprite.rect.collidepoint(position) and isinstance(sprite, Clickable):
                sprite.onClick()
    
    def display(self):
        self.screen.blit(self.background, (0, 0))
        self.sprites.draw(self.screen)
        self.title.display(self.screen)
    
    def update(self):
        self.sprites.update()
    