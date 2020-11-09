import unittest
import helper_functions
from helper_functions import *


mydb= connect_db()
mycursor = mydb.cursor(buffered=True)
mycursor.execute("use flashcards")

class TestHelperFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Unit Tests below here

<<<<<<< HEAD
    def test_get_user_info_from_database(self):
        self.assertEqual((1,'Allie','Password123','allie@gmail.com'),get_user('Allie'))

    def test_get_user_for_nonexistant_user(self):
        #this should return None if user is not in database
        self.assertEqual(None,get_user('Mike'))

    #def testEqual(self):
    #    self.assertEqual(1, 3-1)
    
=======
    def get_user_info_from_database(self):
        get_user('Allie')
        self.assertEqual((1, 'Allie', 'Password123', 'allie@gmail.com'))
>>>>>>> 2156cb4cfae211fd568a1f82836a82153f1600fe

if __name__ == '__main__':
    unittest.main()
