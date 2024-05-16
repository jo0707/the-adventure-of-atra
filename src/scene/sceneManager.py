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

"""
SceneManager class manages the scene transition
SceneManager will change the current scene based on the event
1. Capturing key events (keyboard)
"""

class SceneManager:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.currentScene = MenuScene(screen, 0)
        self.lastSceneEvent = EventHelper.EVENT_SCENESTART
        
    def onEvent(self, event):
        self.currentScene.onEvent(event)
        if event.type == EventHelper.EVENT_SCENESTART:
            self.currentScene = MenuScene(self.screen, self.lastSceneEvent)
            self.lastSceneEvent = EventHelper.EVENT_SCENESTART
        if event.type == EventHelper.EVENT_SCENEGAME:
            self.currentScene = OutdoorScene(self.screen, self.lastSceneEvent)
            self.lastSceneEvent = EventHelper.EVENT_SCENEGAME
        if event.type == EventHelper.EVENT_SCENELOBBYFRONT:
            self.currentScene = LobbyFrontScene(self.screen, self.lastSceneEvent)
            self.lastSceneEvent = EventHelper.EVENT_SCENELOBBYFRONT
        if event.type == EventHelper.EVENT_SCENELOBBYMIDDLE:
            self.currentScene = LobbyMiddleScene(self.screen, self.lastSceneEvent)
            self.lastSceneEvent = EventHelper.EVENT_SCENELOBBYMIDDLE
        if event.type == EventHelper.EVENT_SCENELOBBYLEFT:
            self.currentScene = LobbyLeftScene(self.screen, self.lastSceneEvent)
            self.lastSceneEvent = EventHelper.EVENT_SCENELOBBYLEFT
        if event.type == EventHelper.EVENT_SCENELOBBYRIGHT:
            self.currentScene = LobbyRightScene(self.screen, self.lastSceneEvent)
            self.lastSceneEvent = EventHelper.EVENT_SCENELOBBYRIGHT
        if event.type == EventHelper.EVENT_SCENEROOMLAMPUNG:
            self.currentScene = RoomLampungScene(self.screen, self.lastSceneEvent)
            self.lastSceneEvent = EventHelper.EVENT_SCENEROOMLAMPUNG
        if event.type == EventHelper.EVENT_SCENEROOMSUMATERAUTARA:
            self.currentScene = RoomSumateraUtaraScene(self.screen, self.lastSceneEvent)
            self.lastSceneEvent = EventHelper.EVENT_SCENEROOMSUMATERAUTARA
        if event.type == EventHelper.EVENT_SCENEROOMSUMATERABARAT:
            self.currentScene = RoomSumateraBaratScene(self.screen, self.lastSceneEvent)
            self.lastSceneEvent = EventHelper.EVENT_SCENEROOMSUMATERABARAT
        if event.type == EventHelper.EVENT_SCENESETTINGS:
            self.currentScene = SettingsScene(self.screen, self.lastSceneEvent)
            self.lastSceneEvent = EventHelper.EVENT_SCENESETTINGS
        
    def onKeyDown(self, keys):
        self.currentScene.onKeyDown(keys)
        
    def onTick(self):
        self.currentScene.update()
        self.currentScene.display()
        
    def onClick(self, position: tuple[int, int]):
        self.currentScene.onClick(position)