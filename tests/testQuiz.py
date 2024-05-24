
import unittest

from src.data.quiz import Quiz
from src.scene.sceneManager import SceneManager
from tests.tools import getScreen

class TestQuiz(unittest.TestCase):
    def setUp(self):
        self.question = "What is the capital of the Philippines?"
        self.choices = ["Manila", "Cebu", "Davao", "Quezon City"]
        self.answer = "Manila"
    
    def test_initialization(self): 
        quiz = Quiz(self.question, self.choices, self.answer)
        self.assertEqual(quiz.question, self.question)
        self.assertEqual(quiz.options, self.choices)    
        self.assertEqual(quiz.answer, self.answer)
        
    def test_methods(self):
        quiz = Quiz(self.question, self.choices, self.answer)
        self.assertTrue(hasattr(quiz, "isCorrect"))