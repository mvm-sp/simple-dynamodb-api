# tests/test_list_tutorials.py

import unittest
from api.create_tutorial import create_tutorial
from api.list_tutorials import list_tutorials

class TestListTutorials(unittest.TestCase):
    def setUp(self):
        self.tutorial1 = create_tutorial("Test Tutorial 1", "Test Description 1", True)
        self.tutorial2 = create_tutorial("Test Tutorial 2", "Test Description 2", False)

    def test_list_tutorials(self):
        tutorials = list_tutorials()
        self.assertGreaterEqual(len(tutorials), 2)
        ids = [tutorial['id'] for tutorial in tutorials]
        self.assertIn(self.tutorial1['id'], ids)
        self.assertIn(self.tutorial2['id'], ids)

if __name__ == '__main__':
    unittest.main()
