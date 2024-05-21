# tests/test_get_tutorial.py

import unittest
from api.create_tutorial import create_tutorial
from api.get_tutorial import get_tutorial

class TestGetTutorial(unittest.TestCase):
    def setUp(self):
        self.tutorial = create_tutorial("Test Tutorial", "Test Description", True)

    def test_get_tutorial(self):
        fetched_tutorial = get_tutorial(self.tutorial['id'])
        self.assertIsNotNone(fetched_tutorial)
        self.assertEqual(fetched_tutorial['id'], self.tutorial['id'])
        self.assertEqual(fetched_tutorial['title'], self.tutorial['title'])
        self.assertEqual(fetched_tutorial['description'], self.tutorial['description'])
        self.assertEqual(fetched_tutorial['published'], self.tutorial['published'])

if __name__ == '__main__':
    unittest.main()
