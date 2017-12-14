from aho_rec import aho
import unittest

class AhoCase(unittest.TestCase):
    def test_aho0(self):
        ass = [[(0, 'м'), (1, 'а'), (2, 'м'), (3, 'а')], [(0, 'м'), (1, 'а'), (2, 'ма')],
        [(0, 'м'), (1, 'ам'), (3, 'а')], [(0, 'ма'), (2, 'м'), (3, 'а')], [(0, 'ма'), (2, 'ма')],
        [(0, 'мам'), (3, 'а')], [(0, 'мама')]]
        res = sorted(list(aho(('мам','ами','мама','ми','и','ам','а','ма','м'), 'мама')))
        self.assertEqual(res, ass)
        
    def test_aho1(self):
        ass = [[(0, 'a'), (1, 'b'), (2, 'cde')], [(0, 'ab'), (2, 'cde')], [(0, 'abc')]]
        res = sorted(list(aho(('a','b','cde','ab','abc'), 'abcde')))
        self.assertEqual(ass, res)
        
    def test_aho2(self):
        ass = [[(0, 'дым'), (3, 'ок')], [(0, 'дымок')]]
        res = sorted(list(aho(('дым','ок','дымок'), 'дымок')))
        self.assertEqual(ass, res)

if __name__ == '__main__':
    unittest.main()
