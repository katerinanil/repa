import unittest
from aho_rec import aho

class AhoCase(unittest.TestCase):
    def test_aho0(self):
        ass = [[(0, 'a'), (1, 'b')], [(0, 'ab')]]
        res = sorted(list(aho(('a', 'b', 'ab'), 'ab')))
        self.assertEqual(ass, res)

if __name__ == '__main__':
    unittest.main()
