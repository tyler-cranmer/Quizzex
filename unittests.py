import unittest
import mysql.connector
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

    def get_user_info_from_database(self):
        get_user('Allie')
        self.assertEqual((1, 'Allie', 'Password123', 'allie@gmail.com'))

if __name__ == '__main__':
    unittest.main()
