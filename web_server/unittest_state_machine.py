from state_machine import MorphSM, getCombo
import unittest

class AhoCase(unittest.TestCase):
    def test_combo0(self):
        test_morphs = { 'мам' : {MorphSM.R}, 'а' : {MorphSM.So, MorphSM.F}, 'ми' : {MorphSM.F}, 'ами' : {MorphSM.F},
           'и' : {MorphSM.F, MorphSM.So}}
        test_word = 'мамами'
        ass = ['мам', 'мама']
        res = sorted(list(getCombo(test_word, test_morphs)))
        self.assertEqual(res, ass)

    def test_combo1(self):
        test_morphs = { 'пере' : {MorphSM.Pr}, 'бег' : {MorphSM.R}, 'а' : {MorphSM.F, MorphSM.So}, 'л' : {MorphSM.So},
           'и' : {MorphSM.F, MorphSM.So}, 'е' : {MorphSM.F, MorphSM.So, MorphSM.I}, 'пер' : {MorphSM.R}, 'гал' : {MorphSM.R}}
        test_word = 'перебегали'
        ass = ['перебегал', 'перебегал', 'перебегали', 'перебегали']
        res = sorted(list(getCombo(test_word, test_morphs)))
        self.assertEqual(res, ass)
        
    def test_combo2(self):
        test_morphs = { 'каракатиц' : {MorphSM.R}, 'а' : {MorphSM.So, MorphSM.F}, 'кар' : {MorphSM.R}, 'кат' : {MorphSM.R},
           'и' : {MorphSM.F, MorphSM.So}, 'иц' : {MorphSM.So}}
        test_word = 'каракатица'
        ass = ['каракатиц', 'каракатица']
        res = sorted(list(getCombo(test_word, test_morphs)))
        self.assertEqual(res, ass)

if __name__ == '__main__':
    unittest.main()
