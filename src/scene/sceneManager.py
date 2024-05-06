import pygame

from src.scene.lobbyLeftScene import LobbyLeftScene
from src.scene.lobbyMiddleScene import LobbyMiddleScene
from src.scene.lobbyRightScene import LobbyRightScene
from src.scene.roomLampungScene import RoomLampungScene
from src.scene.roomSumateraBaratScene import RoomSumateraBaratScene
from src.scene.roomSumateraUtaraScene import RoomSumateraUtaraScene
from src.scene.lobbyFrontScene import LobbyFrontScene
from src.scene.outdoorScene import OutdoorScene
from src.scene.menuScene import MenuScene
from src.scene.settingScene import SettingsScene
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
            self.currentScene = OutdoorScene(self.screen)
        if event.type == EventHelper.EVENT_SCENELOBBYFRONT:
            self.currentScene = LobbyFrontScene(self.screen)
        if event.type == EventHelper.EVENT_SCENELOBBYMIDDLE:
            self.currentScene = LobbyMiddleScene(self.screen)
        if event.type == EventHelper.EVENT_SCENELOBBYLEFT:
            self.currentScene = LobbyLeftScene(self.screen)
        if event.type == EventHelper.EVENT_SCENELOBBYRIGHT:
            self.currentScene = LobbyRightScene(self.screen)
        if event.type == EventHelper.EVENT_SCENEROOMLAMPUNG:
            self.currentScene = RoomLampungScene(self.screen)
        if event.type == EventHelper.EVENT_SCENEROOMSUMATERAUTARA:
            self.currentScene = RoomSumateraUtaraScene(self.screen)
        if event.type == EventHelper.EVENT_SCENEROOMSUMATERABARAT:
            self.currentScene = RoomSumateraBaratScene(self.screen)
        if event.type == EventHelper.EVENT_SCENESETTINGS:
            self.currentScene = SettingsScene(self.screen)
        
    def onKeyDown(self, keys):
        self.currentScene.onKeyDown(keys)
        
    def onTick(self):
        self.currentScene.update()
        self.currentScene.display()
        
    def onClick(self, position: tuple[int, int]):
        self.currentScene.onClick(position)