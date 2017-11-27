import unittest
import config
import shelve
from lemmatizer import lemmatizer

class StemmerCase(unittest.TestCase):
    def test_stem0(self):
        lemma = lemmatizer("db_lem_stems2", "db_lem_flex2")
        lst = []
        st = "мама мыла по ушами пирожка уху дым мамами"
        ass = ['мама', 'мыл', 'п', 'по', 'ухо', 'пирожк', 'пирожка','ухо', 'дым', 'мама']
        for w in filter(bool, st.split()):
            for lem in lemma.lemmatize(w):
                lst.append(lem)      
        self.assertEqual(sorted(lst), (sorted(ass)))
    
if __name__ == '__main__':
    unittest.main()
