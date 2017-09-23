import unittest
from stem_0 import stemmer

class StemmerCase (unittest.TestCase):    
    def test_stem0(self):
        self.assertEqual(stemmer('лаял'),"ла")
    def test_stem1(self):
        self.assertEqual(stemmer('мам'),"м")
    def test_stem2(self):
        self.assertEqual(stemmer('бабах'),"баб")
    def test_stem3(self):
        self.assertEqual(stemmer('ба'),"б")
    def test_stem4(self):
        self.assertEqual(stemmer('ого'),"ог")
    def test_stem5(self):
        self.assertEqual(stemmer('пам'),"п")
    def test_stem6(self):
        self.assertEqual(stemmer('а'),"а")
    def test_stem7(self):
        self.assertEqual(stemmer('их'),"их")
    def test_stem8(self):
        self.assertEqual(stemmer(''),"")

if __name__ == '__main__':
    unittest.main()
