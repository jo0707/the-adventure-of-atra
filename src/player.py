import pygame

class Player():
    def __init__(self):
        self.name = "Atra"
        self.paintingCollected = 0
        self.lampungCorrectAnswers: int | None = None
        self.sumateraUtaraCorrectAnswers: int | None = None
        self.sumateraBaratCorrectAnswers: int | None = None
        
        
    def reset(self):
        self.name = "Atra"
        self.paintingCollected = 0
        self.lampungCorrectAnswers: int | None = None
        self.sumateraUtaraCorrectAnswers: int | None = None
        self.sumateraBaratCorrectAnswers: int | None = None
        
    @staticmethod
    def getPlayer():
        return player
        
player = Player()