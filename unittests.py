import unittest

class TestHelperFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    # Unit Tests below here

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()
