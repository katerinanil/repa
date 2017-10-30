import unittest
from stem_3 import stemmer

class StemmerCase(unittest.TestCase):
    def test_stem0(self):
        self.assertEqual(list(sorted(stemmer('����'))), list(sorted(['����', '��'])))
    def test_stem1(self):
        self.assertEqual(list(sorted(stemmer('���'))), list(sorted(['���'])))
    def test_stem2(self):
        self.assertEqual(list(sorted(stemmer('�����'))), list(sorted(['�����', '���'])))
    def test_stem3(self):
        self.assertEqual(list(sorted(stemmer('��'))), list(sorted(['��', '�'])))
    def test_stem4(self):
        self.assertEqual(list(sorted(stemmer('���'))), list(sorted(['���', '��'])))
    def test_stem5(self):
        self.assertEqual(list(sorted(stemmer('���'))), list(sorted(['���', '�'])))
    def test_stem6(self):
        self.assertEqual(list(sorted(stemmer('�'))), list(sorted(['�'])))
    def test_stem7(self):
        self.assertEqual(list(sorted(stemmer('���������'))), list(sorted(['���������', '��������'])))
    def test_stem8(self):
        self.assertEqual(list(sorted(stemmer('����'))), list(sorted(['����', '�', '��', '���'])))
    def test_stem9(self):
        self.assertEqual(list(sorted(stemmer('����'))), list(sorted(['���'])))
    def test_stem10(self):
        self.assertEqual(list(sorted(stemmer('������'))), list(sorted(['���', '�����'])))

if __name__ == '__main__':
    unittest.main()
