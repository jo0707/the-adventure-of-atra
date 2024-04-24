import pygame

class Player():
    def __init__(self):
        self.name = "Atra"
        self.paintingCollected = 0
        self.questionAnswered = 0
        
    def reset(self):
        self.name = "Atra"
        self.paintingCollected = 0
        self.questionAnswered = 0
        
    @staticmethod
    def getPlayer():
        return player
        
player = Player()