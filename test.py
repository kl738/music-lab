"""
Test cases
"""
import unittest
from world import *

class MusicLabTestCase(unittest.TestCase):
    """Tests for `world.py`."""
    def test_world(self):
        self.assertTrue(is_prime(5))

if __name__ == '__main__':
    unittest.main()
