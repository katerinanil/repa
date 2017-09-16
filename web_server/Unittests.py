import os
import shelve
import unittest
import makeDB
import getQuery

class getQueryTests(unittest.TestCase):  
	def test_getalltokens(self):
		ass = 'bla alpha;123 digit;'
		res = ''
		tokens = getQuery.getalltokens('bla 123')
		for t in tokens:
			res += t.string + ' ' + t.token_type + ';'
		self.assertEqual(ass, res)
	def test_query(self):
		f1 = open('f1.txt', 'w')
		f1.write('foo bar')
		f1.close()

		f1 = open('f2.txt', 'w')
		f1.write('egg foo ham')
		f1.close()

		makeDB.makeDB(['f1.txt', 'f2.txt'], 'testdb')
		ass = "OrderedDict([('f2.txt', [(4, 7), (8, 11)])])"
		res = str(getQuery.query('foo ham', 'testdb'))

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
		self.assertEqual(ass, res)

	def test_makeContexts(self):
		f1 = open('f1.txt', 'w')
		f1.write('foo bar')
		f1.close()

		f1 = open('f2.txt', 'w')
		f1.write('egg foo ham')
		f1.close()

		makeDB.makeDB(['f1.txt', 'f2.txt'], 'testdb')
		ass = "OrderedDict([('f2.txt', ['egg foo ham'])])"
		res = getQuery.query('foo ham', 'testdb')
		res = str(getQuery.makeContexts(res))

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
		self.assertEqual(ass, res)
if __name__ == '__main__':
    unittest.main()
