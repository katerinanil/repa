from aho_rec import aho
import unittest

class SortCase(unittest.TestCase):
    def test0_check_aho_rec(self):
        res = list(aho(('мам','ами','мама','ми','и','ам','а','ма','м'), "мама"))
        ass = [[(0, 'м'), (1, 'а'), (2, 'м'), (3, 'а')], [(0, 'м'), (1, 'а'), (2, 'ма')],
        [(0, 'м'), (1, 'ам'), (3, 'а')], [(0, 'ма'), (2, 'м'), (3, 'а')], [(0, 'ма'), (2, 'ма')],
        [(0, 'мам'), (3, 'а')], [(0, 'мама')]]
        self.assertEqual(res, ass)

if __name__ == '__main__':
    unittest.main()
