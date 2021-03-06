import unittest
import sorting

class SortCase(unittest.TestCase):
    def test0_check_sort(self):
        res = list(sorting.sort([1],[2,3],[4,5]))
        ass = [1,2,3,4,5]
        self.assertEqual(res, ass)
    def test1_check_sort(self):
        res = list(sorting.sort([],[],[5]))
        ass = [5]
        self.assertEqual(res, ass)
    def test2_check_sort(self):
        res = list(sorting.sort([1000],[2.2,3],[-1]))
        ass = [-1,2.2,3,1000]
        self.assertEqual(res, ass)
    def test3_check_sort(self):
        res = list(sorting.sort([1],[1,1],[1,5]))
        ass = [1,1,1,1,5]
        self.assertEqual(res, ass)
    def test4_check_sort(self):
        res = list(sorting.sort([5],[3,5],[4,5]))
        ass = [3,4,5,5,5]
        self.assertEqual(res, ass)

if __name__ == '__main__':
    unittest.main()
