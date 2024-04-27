import pygame

from src.components.character import Character
from src.scene.scene import Scene
from src.utils.screenHelper import ScreenHelper

class Level0Scene(Scene):
    def __init__(self, screen: pygame.Surface):
        super().__init__(screen)
        self.background = pygame.image.load("assets/images/scene0/background.png")
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))
        
        self.character = Character()
        self.character.rect.bottomleft = (ScreenHelper.getWindowX() / 2, ScreenHelper.getWindowY())
        self.sprites.add(self.character)
    
    def onKeyDown(self, keys):
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.character.moveUp()
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.character.moveDown()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.character.moveLeft()
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.character.moveRight()
    
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