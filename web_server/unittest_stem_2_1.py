import unittest
from stem_2_1 import stemmer

class StemmerCase(unittest.TestCase):
    def test_stem0(self):
        self.assertEqual(list(sorted(stemmer('лаял'))), list(sorted(['лаял', 'ла'])))
    def test_stem1(self):
        self.assertEqual(list(sorted(stemmer('мам'))), list(sorted(['мам'])))
    def test_stem2(self):
        self.assertEqual(list(sorted(stemmer('бабах'))), list(sorted(['бабах', 'баб'])))
    def test_stem3(self):
        self.assertEqual(list(sorted(stemmer('ба'))), list(sorted(['ба', 'б'])))
    def test_stem4(self):
        self.assertEqual(list(sorted(stemmer('ого'))), list(sorted(['ого', 'ог'])))
    def test_stem5(self):
        self.assertEqual(list(sorted(stemmer('пам'))), list(sorted(['пам', 'п'])))
    def test_stem6(self):
        self.assertEqual(list(sorted(stemmer('а'))), list(sorted(['а'])))
    def test_stem7(self):
        self.assertEqual(list(sorted(stemmer('абвгдейку'))), list(sorted(['абвгдейку', 'абвгдейк'])))
    def test_stem8(self):
        self.assertEqual(list(sorted(stemmer('мала'))), list(sorted(['мала', 'м', 'ма', 'мал'])))
    def test_stem9(self):
        self.assertEqual(list(sorted(stemmer('мыла'))), list(sorted(['мыл'])))
    def test_stem10(self):
        self.assertEqual(list(sorted(stemmer('мамами'))), list(sorted(['мам', 'мамам'])))

if __name__ == '__main__':
    unittest.main()
