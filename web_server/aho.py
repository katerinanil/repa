#from string_algorithm import aho_corrasick
from aho_cor import aho_corrasick
from collections import deque
#from .trie import Trie, TrieNode
import unittest

"""morphArr = ('мам','ами','а','ми','ам','и')

def getMorph(query):
    morphemes = aho_corrasick.find(morphArr, query)
    return(morphemes)"""
class TestAhoCorrasick(unittest.TestCase):
    def test_find(self):
        patterns = ('at', 'gag', 'gc', 'gata')
        text = 'tatatattgcgccatattagagattagatagga'
        result = set()
        for pattern in patterns:
            occurrences = naive_find(pattern, text)
            result |= set(((o, pattern) for o in occurrences))

        self.assertSetEqual(result, set(aho_corrasick(patterns, text))


if __name__ == '__main__':
        unittest.main()
