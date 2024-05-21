# tests/test_delete_tutorial.py

import unittest
from api.create_tutorial import create_tutorial
from api.delete_tutorial import delete_tutorial
from api.get_tutorial import get_tutorial

class TestDeleteTutorial(unittest.TestCase):
    def setUp(self):
        self.tutorial = create_tutorial("Test Tutorial", "Test Description", True)

    def test_delete_tutorial(self):
        delete_response = delete_tutorial(self.tutorial['id'])
        self.assertIsNone(get_tutorial(self.tutorial['id']))

if __name__ == '__main__':
    unittest.main()
