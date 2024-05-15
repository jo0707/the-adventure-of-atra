import pygame

from constants import FPS, SCREEN_HEIGHT, SCREEN_WIDTH, WINDOW_TITLE
from src.scene.sceneManager import SceneManager
from src.utils.fontHelper import FontHelper
from src.utils.soundHelper import SoundHelper

"""
Game class defines global variables and game loop
"""

class Game:
    running = True
    # set window title
    pygame.display.set_caption(WINDOW_TITLE)
    # Window creation
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    # Clock for frame rate
    clock = pygame.time.Clock()
    
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        FontHelper.initFonts()
        SoundHelper.initSounds()
        self.sceneManager = SceneManager(Game.screen)
        
    def onEvent(self):
        self.sceneManager.onKeyDown(pygame.key.get_pressed())
        for event in pygame.event.get():
            if event.type == pygame.QUIT or not Game.running:
                self.quitGame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.sceneManager.onClick(event.pos)
            else:
                self.sceneManager.onEvent(event)
                
    def gameLoop(self):
        while Game.running:
            self.onEvent()
            self.sceneManager.onTick()
            pygame.display.flip()
            Game.clock.tick(FPS)

    def quitGame(self):
        pygame.quit()