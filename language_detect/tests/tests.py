import unittest
from src.reco_lang.get_lang import GetLang

class TestGetLang(unittest.TestCase):
    def setUp(self):
        self.get_lang = GetLang()
    def recognizeru(self):
        self.assertEqual(self.get_lang.recog_lang("привет я русский"))
    def recognizefr(self):
        self.assertEqual(self.get_lang.recog_lang("Sono francese"))
    def recognizede(self):
        self.assertEqual(self.get_lang.recog_lang("Ich bin Deutsche"))
    def recognizekr(self):
        self.assertEqual(self.get_lang.recog_lang("나는 한국인이다"))
    def recognizesp(self):
        self.assertEqual(self.get_lang.recog_lang("Yo soy español"))
    def recognizesp(self):
        self.assertEqual(self.get_lang.recog_lang("Eu sou portugues"))
    def recognizeit(self):
        self.assertEqual(self.get_lang.recog_lang("Sono italiano"))



unittest.main()