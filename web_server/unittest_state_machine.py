from state_machine import MorphSM, getCombo
import unittest

class AhoCase(unittest.TestCase):
    def test_combo0(self):
        test_morphs = { 'мам' : {MorphSM.R}, 'а' : {MorphSM.S, MorphSM.F}, 'ми' : {MorphSM.F}, 'ами' : {MorphSM.F},
           'и' : {MorphSM.F, MorphSM.S}}
        test_word = 'мамами'
        ass = ['мам R, а S, ми F, ', 'мам R, ами F, ']
        res = sorted(list(getCombo(test_word, test_morphs)))
        self.assertEqual(res, ass)

    def test_combo1(self):
        test_morphs = { 'пере' : {MorphSM.Pr}, 'бег' : {MorphSM.R}, 'а' : {MorphSM.F, MorphSM.S}, 'л' : {MorphSM.S},
           'и' : {MorphSM.F, MorphSM.S}, 'е' : {MorphSM.F, MorphSM.S, MorphSM.I}, 'пер' : {MorphSM.R}, 'гал' : {MorphSM.R}}
        test_word = 'перебегали'
        ass = ['пер R, е I, бег R, а S, л S, и F, ',
               'пер R, е I, бег R, а S, л S, и S, ',
               'пере Pr, бег R, а S, л S, и F, ',
               'пере Pr, бег R, а S, л S, и S, ']
        res = sorted(list(getCombo(test_word, test_morphs)))
        self.assertEqual(res, ass)
        
    def test_combo2(self):
        test_morphs = { 'каракатиц' : {MorphSM.R}, 'а' : {MorphSM.S, MorphSM.F}, 'кар' : {MorphSM.R}, 'кат' : {MorphSM.R},
           'и' : {MorphSM.F, MorphSM.S}, 'иц' : {MorphSM.S}}
        test_word = 'каракатица'
        ass = ['каракатиц R, а F, ', 'каракатиц R, а S, ']
        res = sorted(list(getCombo(test_word, test_morphs)))
        self.assertEqual(res, ass)

if __name__ == '__main__':
    unittest.main()
