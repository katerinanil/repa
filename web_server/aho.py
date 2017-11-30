#from string_algorithm import aho_corrasick
from aho_cor import aho_corrasick
from collections import deque
from .trie import Trie, TrieNode

morphArr = ('мам','ами','а','ми','ам','и')

def getMorph(query):
    morphemes = aho_corrasick.find(morphArr, query)
    return(morphemes)
