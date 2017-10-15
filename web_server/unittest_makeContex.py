import os
import unittest
import shelve
from makeDB import makeDB
from getQuery import query, makeContexts

class StemmerCase(unittest.TestCase):
    def test_makeContext0(self):
        f1_name = 'test_f1.txt'
        f2_name = 'test_f2.txt'
        f1 = open(f1_name, 'w')
        f1.write('Ляляля маму. Мррррррр. Бебебе!')
        f1.close()

        f2 = open(f2_name, 'w')
        f2.write('мамами мыла раму. М')
        f2.close()

        db_name = 'testdb'
        makeDB([f1_name, f2_name], db_name)
        ass = "[(['Ляляля маму'], [[(7, 11)]]), (['мамами мыла раму'], [[(0, 6)]])]"
        db = shelve.open(db_name)
        qres = query('маме', db_name)
        res = str(list(makeContexts(qres).values()))
        db.close()
        self.assertEqual(ass, res)
        
        os.unlink(f1_name)
        os.unlink(f2_name)
        if os.path.exists(db_name): os.unlink(db_name)
        if os.path.exists(db_name + '.dat'): os.unlink(db_name + '.dat')
        if os.path.exists(db_name + '.bak'): os.unlink(db_name + '.bak')
        if os.path.exists(db_name + '.dir'): os.unlink(db_name + '.dir')

if __name__ == '__main__':
    unittest.main()
