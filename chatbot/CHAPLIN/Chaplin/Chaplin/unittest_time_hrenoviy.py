import unittest
import chaplin
import datetime, db, kb
#from chaplin import check_film_time

class TimeCase(unittest.TestCase):
    def test_time0(self):
        ? = str(base.film_time.time)
        ass = check_film_time("14 12")    
        self.assertEqual((ass), ("14:12"))
    
if __name__ == '__main__':
    unittest.main()
