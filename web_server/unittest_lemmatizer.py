import unittest
import config
import shelve
from lemmatizer import lemmatizer

class StemmerCase(unittest.TestCase):
    def test_stem0(self):
        lemma = lemmatizer("db_lem_stems2", "db_lem_flex2")
        lst = []
        st = "мама ! мыла по ушами пирожка уху дым мамами" #видимо знаки преп фильтруются позднее в Query
        ass = ['мама', '!', 'мыл', 'п', 'по', 'ухо', 'пирожк', 'пирожка','ухо', 'дым', 'мама']
        for w in filter(bool, st.split()):
            for lem in lemma.lemmatize(w):
                lst.append(lem)
        #где-то тут поunlinkать        
        self.assertEqual(sorted(lst), (sorted(ass)))
    
if __name__ == '__main__':
    unittest.main()

#create new temporary data base
#pass it to constructor parameter of lemmatizer
#lemmatize some query
#remove data base files
#assert it
