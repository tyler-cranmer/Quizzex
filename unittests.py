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
    
    def test_get_user_info_from_database(self):
        self.assertEqual((1,'Allie','Password123','allie@gmail.com'),get_user('Allie'))

    def test_get_user_for_nonexistant_user(self):
        #this should return None if user is not in database
        self.assertEqual(None,get_user('Mike'))

    def test_add_new_user(self):
        user_id=add_user('Shannon','12345','shannon@gmail.com')
        #if add user worked, then 'get_user' should return the correct users info
        self.assertEqual((user_id,'Shannon','12345','shannon@gmail.com'),get_user('Shannon'))
    
    def test_try_to_add_existing_user(self):
        user = add_user('Allie','11111', 'allie@gmail.com')
        #user should not be added if username already exists
        self.assertEqual(user,"This username is already taken")

    def test_remove_existing_user(self):
        remove_user('Shannon')
        #if this works, calling 'get_user' for shannon should return None as they are no longer a user
        self.assertEqual(None,get_user('Shannon'))

    def test_remove_user_that_does_not_exist(self):
        fake_user = remove_user('sldkfmsldkfm')
        #if this works, it should return 'This user does not exist'
        self.assertEqual(fake_user, 'This user does not exist')




if __name__ == '__main__':
    unittest.main()
