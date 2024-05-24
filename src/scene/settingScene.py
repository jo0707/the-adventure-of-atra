import pygame

from src.scene.scene import Scene

class SettingsScene(Scene):
    def __init__(self, screen: pygame.Surface, lastSceneEvent: int):
        super().__init__(screen)
        self.lastSceneEvent = lastSceneEvent
        self.background = pygame.image.load("assets/background.png").convert_alpha()
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))
    
    def onKeyDown(self, keys):
        pass
    
    def onEvent(self, event):
        pass
    
    def onClick(self, position: tuple[int, int]):
        super().onClick(position)
    
    def display(self):
        self.screen.blit(self.background, (0, 0))
        self.sprites.draw(self.screen)
        for textbox in self.textboxes:
            textbox.display(self.screen)
    
    def update(self):
        for sprite in self.sprites:
            sprite.update()