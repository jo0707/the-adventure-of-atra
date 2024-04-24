import pygame

from src.scene.GameScene import GameScene
from src.scene.MenuScene import MenuScene
from src.scene.SettingScene import SettingsScene
from src.utils.eventHelper import EventHelper

class SceneManager:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.currentScene = MenuScene(screen)
        
    def onEvent(self, event):
        self.currentScene.onEvent(event)
        if event.type == EventHelper.EVENT_SCENESTART:
            self.currentScene = MenuScene(self.screen)
        if event.type == EventHelper.EVENT_SCENEGAME:
            self.currentScene = GameScene(self.screen)
        if event.type == EventHelper.EVENT_SCENESETTINGS:
            self.currentScene = SettingsScene(self.screen)
        
    def onKeyDown(self, keys):
        self.currentScene.onKeyDown(keys)
        
    def onTick(self):
        self.currentScene.update()
        self.currentScene.display()
        
    def onClick(self, position: tuple[int, int]):
        self.currentScene.onClick(position)