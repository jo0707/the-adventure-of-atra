from abc import ABC, abstractmethod
import pygame

from src.components.clickable import Clickable
from src.components.itemDescription import ItemDetail
from src.scene.scene import Scene
from src.components.itemPreview import ItemPreview
from src.components.interactableItem import InteractableItem
from src.components.textbox import Textbox
from src.utils.eventHelper import EventHelper

"""
GameScene class used for the gameplay scenes
ex: OutdoorScene, RoomScene, etc
"""

class GameScene(Scene, ABC):
    def __init__(self, screen: pygame.Surface, backgroundPath: str):
        super().__init__(screen)
        self.background = pygame.image.load(backgroundPath).convert_alpha()
        self.background = pygame.transform.scale(self.background, (pygame.display.get_window_size()))
        
        # contains all interacable sprites in scene (InteractableItem)
        self.itemSprites = pygame.sprite.Group()
        # contains all the transparent rects for next scene
        self.nextSceneRects: dict[int, pygame.rect.Rect] = {}
        self.itemPreview: ItemPreview | None = None
        self.itemDetail: ItemDetail | None = None
        self.lastCollidedItem: InteractableItem | None = None
        
    @abstractmethod
    def onEvent(self, event: pygame.event.Event):
        pass
    
    def onKeyDown(self, keys):
        if keys[pygame.K_e] and self.itemPreview:
            def closeItemDetail():
                print("from GameScene")
                self.itemDetail = None
            self.itemDetail = ItemDetail(128, 72, self.itemPreview.interactableItem, lambda: closeItemDetail())
            self.itemPreview = None

    def onClick(self, position: tuple[int, int]):
        if self.itemDetail:
            for sprite in self.itemDetail:
                if sprite.rect.collidepoint(position) and isinstance(sprite, Clickable):
                    sprite.onClick()
                    
        if self.itemPreview:
            for sprite in self.itemPreview:
                if sprite.rect.collidepoint(position) and isinstance(sprite, Clickable):
                    sprite.onClick()
                    
        for sprite in self.sprites:
            if sprite.rect.collidepoint(position) and isinstance(sprite, Clickable):
                sprite.onClick()
                
    # display method is used to draw the sprites and textboxes on the screen
    # this method only draws the sprites and textboxes
    def display(self):
        self.screen.blit(self.background, (0, 0))
        self.sprites.draw(self.screen)
        if self.itemPreview:
            self.itemPreview.draw(self.screen)
        if self.itemDetail:
            self.itemDetail.draw(self.screen)
            

    # update method is used to update the sprites condition and textboxes
    # this method only updates the sprites and textboxes logic
    # ex: moving the sprite, changing the text, etc
    def update(self):
        if self.itemDetail:
            self.itemDetail.update()
        
        for sprite in self.sprites:
            sprite.update()
            
        for event, rect in self.nextSceneRects.items():
            if self.atra.rect.colliderect(rect):
                self.switchSceneEvent(event)
                
        # collided items always instance of InteractableItem
        collidedItem = pygame.sprite.spritecollideany(self.atra, self.itemSprites)
        
        # if there is a collided item,
        if collidedItem is not None:
            collidedItem.onPlayerCollision(True) # darken the item
            self.itemPreview = ItemPreview(320, 480, collidedItem) # create the item preview
        elif self.lastCollidedItem is not None:
            self.lastCollidedItem.onPlayerCollision(False) # lighten the item
            self.itemPreview = None # hide the item preview
        self.lastCollidedItem = collidedItem
        
    # create new transparent box to switch scene when atra collides with it
    # and when atra collides with it, it will post the desired event from parameter
    def addLevelRect(self, event: int, x: int, y: int, width: int, height: int):
        self.nextSceneRects[event] = pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(x, y, width, height))