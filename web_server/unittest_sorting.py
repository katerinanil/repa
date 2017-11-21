import unittest
import sorting

class SortCase(unittest.TestCase):
    def check_sort(self):
        res = list(sorting.sort([1],[2,3],[4,5]))
        ass = [1,2,3,4,5]
        self.assertEqual(res, ass)

if __name__ == '__main__':
    unittest.main()
