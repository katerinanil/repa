import unittest
from state_machine import morphs, _getCombo, getStem

class StateMachineCase(unittest.TestCase):
    def test_get_stem_0(self):
        ass = ''
        res = ''
        for st in getStem('ами', morphs):
            res += st
        self.assertEqual(ass, res)
    def test_get_stem_1(self):
        ass = 'мам'
        res = ''
        for st in getStem('мамами', morphs):
            res += st
        self.assertEqual(ass, res)
    def test_get_stem_2(self):
        ass = 'понасмотрся'
        res = ''
        for st in getStem('понасмотревшийся', morphs):
            res += st
        self.assertEqual(ass, res)
    def test_get_stem_3(self):
        ass = ''
        res = ''
        for st in getStem('ёжик', morphs):
            res += st
        self.assertEqual(ass, res)

    def test_get_combo_0(self):
        ass = ''
        res = ''
        for ans, p in _getCombo('ами', morphs):
            for sub in ans: res += sub[1]
        self.assertEqual(ass, res)
    def test_get_combo_1(self):
        ass = 'мамами'
        res = ''
        for ans, p in _getCombo('мамами', morphs):
            for sub in ans: res += sub[1]
        self.assertEqual(ass, res)
    def test_get_combo_2(self):
        ass = 'понасмотревшийся'
        res = ''
        for ans, p in _getCombo('понасмотревшийся', morphs):
            for sub in ans: res += sub[1]
        self.assertEqual(ass, res)
    def test_get_combo_3(self):
        ass = ''
        res = ''
        for ans, p in _getCombo('ёжик', morphs):
            for sub in ans: res += sub[1]
        self.assertEqual(ass, res)
    
if __name__ == '__main__':
    unittest.main()