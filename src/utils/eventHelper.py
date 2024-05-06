import pygame

EVENT_COUNT = 0

class EventHelper:
    @staticmethod
    def newEvent():
        global EVENT_COUNT
        EVENT_COUNT = EVENT_COUNT + 1
        return pygame.USEREVENT + EVENT_COUNT

    @staticmethod
    def postEvent(event: int):
        pygame.event.post(pygame.event.Event(event))

    EVENT_SCENESTART = newEvent()
    EVENT_SCENESETTINGS = newEvent()
    EVENT_SCENEGAME = newEvent()
    EVENT_SCENELOBBYFRONT = newEvent()
    EVENT_SCENELOBBYMIDDLE = newEvent()
    EVENT_SCENELOBBYLEFT = newEvent()
    EVENT_SCENELOBBYRIGHT = newEvent()
    EVENT_SCENEROOMLAMPUNG = newEvent()
    EVENT_SCENEROOMSUMATERAUTARA = newEvent()
    EVENT_SCENEROOMSUMATERABARAT = newEvent()