import copy
from functools import partial
from typing import List, Tuple
import pygame

from src.components.button import Button
from src.components.quizButton import QuizButton
from src.data.quiz import Quiz
from src.components.closeButton import CloseButton
from src.components.textbox import Textbox
from src.components.interactableItem import InteractableItem
from src.components.gameEntity import GameEntity

class EndDialog(pygame.sprite.Group):
    def __init__(self, x: int, y: int, onClose = lambda: print("Close item detail clicked"), quizzez: List[Quiz] = []):
        super().__init__()
        self.width = 1024
        self.height = 575
        self.pad = 48
        self.onClose = onClose
        
        # need to create and store surface and its rect to be able to wrap the text inside surface
        self.textboxes: List[List[pygame.surface.Surface, pygame.rect.Rect, Textbox]] = []
        self.currentIndex = 0
        
        self.grayBackground = pygame.surface.Surface((pygame.display.get_window_size()), pygame.SRCALPHA, 32)
        self.grayBackground.fill((0, 0, 0, 128))
        
        self.background = GameEntity('assets/images/components/dialogBackground.png', x, y, width=self.width, height=self.height)
        self.closeButton = CloseButton(x + self.pad, y + self.pad, 1.5, action=onClose)
        
        quizDoneTextbox = Textbox("Kuis selesai!", 0, 0, 32, (0, 0, 0))
        correctAnswerTextbox = Textbox(f"Jawaban benar kamu ada {self.correctAnswer} dari {len(self.quizzez)}", 0, 0, 24, (45, 134, 45))
        quizDoneTextbox.rect.center = (self.width // 2, self.height // 2)
        correctAnswerTextbox.rect.center = (self.width // 2, self.height // 2 + 48)
        quizDoneTextbox.display(self.background.image)
        correctAnswerTextbox.display(self.background.image)
        
        self.okButton = Button(x + self.pad, y + self.pad + 170, 896, 75, "Keren!", action=onClose)
        self.add(self.background, self.closeButton, *self.quizButtons)
        
    def insertText(self, text: str, x: int, y: int, textSize: int, rectSize: Tuple[int, int], color: Tuple[int, int, int] = pygame.colordict.THECOLORS['black']):
        surface = pygame.surface.Surface(rectSize, pygame.SRCALPHA, 32)
        textbox = Textbox(text, size=textSize, color=color, wrap=True)
        self.textboxes.append([surface, surface.get_rect(topleft=(x, y)), textbox])
        
    def draw(self, surface: pygame.Surface, bgsurf: pygame.Surface | None = None, special_flags: int = 0) -> List[pygame.Rect]:
        surface.blit(self.grayBackground, (0, 0))
        super().draw(surface, bgsurf, special_flags)
        
        