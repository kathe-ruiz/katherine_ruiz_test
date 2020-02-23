import unittest
import time
from LRUCache import LRUCache


class LRUCacheTest(unittest.TestCase):
    def test_default_behaviour(self):
        self.LRU = LRUCache(2)
        self.assertEqual(self.LRU.get(1), -1)
        self.LRU.put(1, 1)
        self.assertEqual(self.LRU.get(1), 1)
        self.LRU.put(2, 4)
        self.LRU.put(3, 9)
        self.LRU.put(4, 16)
        self.assertEqual(self.LRU.get(4), 16)
        self.assertEqual(self.LRU.get(2), -1)
        self.assertEqual(len(self.LRU.get_all()), 2)
        self.LRU.put(5, 5)
        self.LRU.put(6, 6)
        self.LRU.put(7, 7)
        self.assertEqual(self.LRU.get(6), 6)
        self.assertEqual(self.LRU.get(5), -1)

    def test_lru_cache_expired(self):
        self.LRU = LRUCache(3)
        self.LRU.put(1, 1, 2)
        self.assertEqual(self.LRU.get(1), 1)
        time.sleep(3)
        self.assertEqual(self.LRU.get(1), -1)
        self.LRU.put(1, 1, 3)
        self.LRU.put(2, 2, 10)
        self.LRU.put(3, 3, 3)
        time.sleep(4)
        self.assertEqual(self.LRU.get(2), 2)
        self.assertEqual(self.LRU.get(3), -1)
        self.assertEqual(self.LRU.get(1), -1)


if __name__ == "__main__":
    unittest.main()
