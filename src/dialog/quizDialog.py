import copy
from functools import partial
from typing import List, Tuple
import pygame

from src.components.quizButton import QuizButton
from src.data.quiz import Quiz
from src.components.closeButton import CloseButton
from src.components.textbox import Textbox
from src.components.interactableItem import InteractableItem
from src.components.gameEntity import GameEntity

class QuizDialog(pygame.sprite.Group):
    def __init__(self, x: int, y: int, onClose = lambda: print("Close item detail clicked"), quizzez: List[Quiz] = []):
        super().__init__()
        self.width = 1024
        self.height = 575
        self.pad = 48
        self.correctAnswer = 0
        self.quizzez = quizzez
        self.onClose = onClose
        
        # need to create and store surface and its rect to be able to wrap the text inside surface
        self.textboxes: List[List[pygame.surface.Surface, pygame.rect.Rect, Textbox]] = []
        self.currentIndex = 0
        
        self.grayBackground = pygame.surface.Surface((pygame.display.get_window_size()), pygame.SRCALPHA, 32)
        self.grayBackground.fill((0, 0, 0, 128))
        
        self.background = GameEntity('assets/images/components/dialogBackground.png', x, y, width=self.width, height=self.height)
        self.closeButton = CloseButton(x + self.pad, y + self.pad, 1.5, action=onClose)
        
        self.insertText("Saatnya kita kuis!", x + self.pad, y + 72, 26, (self.width - 2 * self.pad, 100))
        self.insertText("Jawablah pertanyaan berikut dengan benar! kamu bisa menemukan jawabannya dari item di sekitar sini...", x + self.pad, y + 100, 18, (self.width - 2 * self.pad, 100))
        # initialize quiz layout
        self.insertText(f"{self.currentIndex + 1}/{len(self.quizzez)} | benar : {self.correctAnswer}", x + self.pad, y + 124, 18, (self.width - 2 * self.pad, 100))
        self.insertText(self.quizzez[self.currentIndex].question, x + self.pad, y + 148, 24, (self.width - 2 * self.pad, 100))
        
        self.quizButtons: List[QuizButton] = []
        for i, answer in enumerate(self.quizzez[self.currentIndex].options):
            print(answer)
            self.quizButtons.append(QuizButton(x + self.pad, y + self.pad + 170 + i * 80, 896, 75, answer, action=partial(self.nextQuestion, answer)))
        
        self.add(self.background, self.closeButton, *self.quizButtons)
        
    def nextQuestion(self, answer: str):
        print(answer)
        print(self.quizzez[self.currentIndex].answer)
        if answer == self.quizzez[self.currentIndex].answer:
            self.correctAnswer += 1
            
        self.currentIndex += 1
        
        if self.currentIndex != len(self.quizzez):
            self.textboxes[2][2].setText(f"{self.currentIndex + 1}/{len(self.quizzez)} | benar : {self.correctAnswer}")
            self.textboxes[3][2].setText(self.quizzez[self.currentIndex].question)
            
            for i, option in enumerate(self.quizzez[self.currentIndex].options):
                self.quizButtons[i].setText(option)
                self.quizButtons[i].setAction(lambda: self.nextQuestion(option))
        else:
            self.onClose()
            return
        
    def insertText(self, text: str, x: int, y: int, textSize: int, rectSize: Tuple[int, int], color: Tuple[int, int, int] = pygame.colordict.THECOLORS['black']):
        surface = pygame.surface.Surface(rectSize, pygame.SRCALPHA, 32)
        textbox = Textbox(text, size=textSize, color=color, wrap=True)
        self.textboxes.append([surface, surface.get_rect(topleft=(x, y)), textbox])
        
    def draw(self, surface: pygame.Surface, bgsurf: pygame.Surface | None = None, special_flags: int = 0) -> List[pygame.Rect]:
        surface.blit(self.grayBackground, (0, 0))
        super().draw(surface, bgsurf, special_flags)
        
        for (s, r, textbox) in self.textboxes:
            # clear the surface first
            s.fill((0, 0, 0, 0))
            textbox.display(s)
            surface.blit(s, r)