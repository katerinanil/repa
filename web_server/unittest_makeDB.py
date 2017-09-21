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

        makeDB.makeDB(['f1.txt', 'f2.txt'], "testdb")
        print("DB was made")
        ass = "[('м[18 chars]0, 4)]}), ('мама', {'f1.txt': [(0, 4)]}), ('мы[147 chars]]})]"
        res = shelve.open("testdb")
        res = str(sorted(res.items()))
        self.assertEqual(ass, result)
        res.close()
       
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
                
if __name__ == '__main__':
    unittest.main()

#dict.get(key[, default])
