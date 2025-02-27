import unittest
from translator import englishToFrench, frenchToEnglish

class Test(unittest.TestCase):
    def test1(self):
        self.assertEqual(englishToFrench ('Hello'), ('Bonjour'))
    def test2(self):
        self.assertNotEqual(englishToFrench ('Hello'), ('Hello'))

    def test3(self):
        self.assertEqual(frenchToEnglish ('Bonjour'), ('Hello'))
    def test4(self):
        self.assertNotEqual(frenchToEnglish ('Bonjour'), ('Bonjour'))

unittest.main()