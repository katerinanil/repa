import unittest
import config
import getQuery
from lemmatizer import lemmatizer

class ContextCase(unittest.TestCase):
    def test_doc_count_0(self):
        lemma = lemmatizer()
        qres = getQuery.query('смотреть', config.DATABASE_NAME, lemma, 2, 1, None)
        #resDict - { 'path' : ( [ 'context' ], [ [ (stBoldWord_1 , endBoldWord_1), (stBoldWord_2 , endBoldWord_2) ] ] ) }
        resDict = getQuery.makeContexts(qres, None)
        self.assertEqual(len(resDict.keys()), 2)
    def test_doc_count_1(self):
        lemma = lemmatizer()
        qres = getQuery.query('смотреть', config.DATABASE_NAME, lemma, 1, 1, None)
        #resDict - { 'path' : ( [ 'context' ], [ [ (stBoldWord_1 , endBoldWord_1), (stBoldWord_2 , endBoldWord_2) ] ] ) }
        resDict = getQuery.makeContexts(qres, None)
        self.assertEqual(len(resDict.keys()), 1)
    def test_doc_count_2(self):
        lemma = lemmatizer()
        qres = getQuery.query('смотреть', config.DATABASE_NAME, lemma, 0, 1, None)
        #resDict - { 'path' : ( [ 'context' ], [ [ (stBoldWord_1 , endBoldWord_1), (stBoldWord_2 , endBoldWord_2) ] ] ) }
        resDict = getQuery.makeContexts(qres, None)
        self.assertEqual(len(resDict.keys()), 0)
    def test_doc_count_3(self):
        lemma = lemmatizer()
        qres = getQuery.query('смотреть', config.DATABASE_NAME, lemma, 1, 2, None)
        #resDict - { 'path' : ( [ 'context' ], [ [ (stBoldWord_1 , endBoldWord_1), (stBoldWord_2 , endBoldWord_2) ] ] ) }
        resDict = getQuery.makeContexts(qres, None)
        self.assertEqual(len(resDict.keys()), 1)
    def test_doc_count_4(self):
        lemma = lemmatizer()
        qres = getQuery.query('смотреть', config.DATABASE_NAME, lemma, 1, 3, None)
        #resDict - { 'path' : ( [ 'context' ], [ [ (stBoldWord_1 , endBoldWord_1), (stBoldWord_2 , endBoldWord_2) ] ] ) }
        resDict = getQuery.makeContexts(qres, None)
        self.assertEqual(len(resDict.keys()), 0)
    def test_doc_names(self):
        lemma = lemmatizer()
        qres = getQuery.query('смотреть', config.DATABASE_NAME, lemma, 2, 1, None)
        #resDict - { 'path' : ( [ 'context' ], [ [ (stBoldWord_1 , endBoldWord_1), (stBoldWord_2 , endBoldWord_2) ] ] ) }
        resDict = getQuery.makeContexts(qres, None)
        self.assertEqual(sorted(resDict.keys()), ['mid_text_1.txt', 'mid_text_2.txt'])
    def test_context_0(self):
        lemma = lemmatizer()
        qres = getQuery.query('смотреть', config.DATABASE_NAME, lemma, 2, 1, None)
        #resDict - { 'path' : ( [ 'context' ], [ [ (stBoldWord_1 , endBoldWord_1), (stBoldWord_2 , endBoldWord_2) ] ] ) }
        resDict = getQuery.makeContexts(qres, None)
        self.assertEqual(sorted(resDict['mid_text_1.txt'][0]),
            ['Разве можно оставаться понасмотревшийся смотрел посмотрел смотреть смотрю смотрит спокойною в наше время, когда есть у человека чувство?',
             '– отвечал, нисколько смотреть не смутясь такою встречей, вошедший князь, в придворном, шитом мундире, в чулках, башмаках, при звездах, с светлым выражением плоского лица.'])
    def test_context_1(self):
        lemma = lemmatizer()
        quotes = ((2, 0), (5, 0))
        qres = getQuery.query('смотреть', config.DATABASE_NAME, lemma, 2, 1, quotes)
        #resDict - { 'path' : ( [ 'context' ], [ [ (stBoldWord_1 , endBoldWord_1), (stBoldWord_2 , endBoldWord_2) ] ] ) }
        resDict = getQuery.makeContexts(qres, quotes)
        self.assertEqual(sorted(resDict['mid_text_1.txt'][0]),
            ['Разве можно оставаться понасмотревшийся смотрел посмотрел смотреть смотрю смотрит спокойною в наше время, когда есть у человека чувство?',
             '– отвечал, нисколько смотреть не смутясь такою встречей, вошедший князь, в придворном, шитом мундире, в чулках, башмаках, при звездах, с светлым выражением плоского лица.'])
    def test_context_2(self):
        lemma = lemmatizer()
        quotes = ((1, 0), (5, 0))
        qres = getQuery.query('смотреть', config.DATABASE_NAME, lemma, 2, 1, quotes)
        #resDict - { 'path' : ( [ 'context' ], [ [ (stBoldWord_1 , endBoldWord_1), (stBoldWord_2 , endBoldWord_2) ] ] ) }
        resDict = getQuery.makeContexts(qres, quotes)
        self.assertEqual(sorted(resDict['mid_text_1.txt'][0]),
            ['– отвечал, нисколько смотреть не смутясь такою встречей, вошедший князь, в придворном, шитом мундире, в чулках, башмаках, при звездах, с светлым выражением плоского лица.'])
    
if __name__ == '__main__':
    unittest.main()
