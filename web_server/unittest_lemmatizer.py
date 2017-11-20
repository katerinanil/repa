import unittest
from lemmatizer import lemmatizer

class StemmerCase(unittest.TestCase):
    def test_stem0(self):
        #create new temporary data base
        #pass it to constructor parameter of lemmatizer
        #lemmatize some query
        #remove data base files
        #assert it
        lemma = lemmatizer()
        self.assertEqual(list(sorted(stemmer('лаял'))), list(sorted(['лаял', 'ла'])))
    
if __name__ == '__main__':
    unittest.main()