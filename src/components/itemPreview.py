import pygame


from src.components.textbox import Textbox
from src.components.interactableItem import InteractableItem
from src.components.gameEntity import GameEntity

class ItemPreview(pygame.sprite.Group):
    width = 740
    height = 240
    
    def __init__(self, x: int, y: int, interactableItem: InteractableItem):
        self.interactableItem = interactableItem
        self.background = GameEntity('assets/images/components/button3.png', x, y, width=ItemPreview.width, height=ItemPreview.height)
        self.titleTextbox = Textbox(interactableItem.title, x + 10, y + 10, 30, pygame.colordict.THECOLORS['black'])
        self.image = GameEntity(interactableItem.image., x + 10, y + 50, scale=0.5)
        self.enterToOpenTextbox = Textbox('⏎ Tekan Enter untuk membuka', ItemPreview.width - 10, ItemPreview.height + 10, 18, pygame.colordict.THECOLORS['black'])
        self.add(self.titleTextbox, self.image, self.enterToOpenTextbox)