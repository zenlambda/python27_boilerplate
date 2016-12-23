""" Tests for main module """

import unittest

import main


class MainTestCase(unittest.TestCase):
    """ Tests for the main module """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_greeting(self):
        """ Test that the correct greeting is used """
        self.assertEqual(main.greeting(), 'hello world')


if __name__ == '__main__':
    unittest.main()
