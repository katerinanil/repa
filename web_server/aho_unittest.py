import unittest

from string_algorithms import aho_corrasick, naive_find

class TestAhoCorrasick(unittest.TestCase):
    def test_find(self):
        patterns = ('at', 'gag', 'gc', 'gata')
        text = 'tatatattgcgccatattagagattagatagga'
        result = set()
        for pattern in patterns:
            occurrences = naive_find.find(pattern, text)
            result |= set(((o, pattern) for o in occurrences))

        self.assertSetEqual(result, set(aho_corrasick.find(patterns, text)))

if __name__ == '__main__':
    unittest.main()