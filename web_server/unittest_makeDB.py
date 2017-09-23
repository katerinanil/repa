import os
import shelve
import unittest
import makeDB
import getQuery

class getDBTests(unittest.TestCase):
    def test_makeDB(self):
        f1 = open('f1.txt', 'w')
        f1.write('мама')
        f1.close()

        f2 = open('f2.txt', 'w')
        f2.write('мыла раму')
        f2.close()

        db_name = "testdb"
        makeDB.makeDB(['f1.txt', 'f2.txt'], db_name)
        ass = "[('мам', {'f1.txt': [(0, 4)]}), ('мама', {'f1.txt': [(0, 4)]}), " + \
              "('мы', {'f2.txt': [(0, 4)]}), ('мыл', {'f2.txt': [(0, 4)]}), " + \
              "('мыла', {'f2.txt': [(0, 4)]}), ('рам', {'f2.txt': [(5, 9)]}), " + \
              "('раму', {'f2.txt': [(5, 9)]})]"
        db = shelve.open(db_name)
        res = str(sorted(db.items()))
        db.close()
        self.assertEqual(ass, res)
        
        os.unlink('f1.txt')
        os.unlink('f2.txt')
        if os.path.exists('testdb'):
            os.unlink('testdb')
        if os.path.exists('testdb.dat'):
            os.unlink('testdb.dat')
        if os.path.exists('testdb.bak'):
            os.unlink('testdb.bak')
        if os.path.exists('testdb.dir'):
            os.unlink('testdb.dir')
        #self.assertEqual(ass, res)
                
if __name__ == '__main__':
    unittest.main()
#{'слово': {'путь к файлу': [(индекс начала, индекс конца слова)]}}
