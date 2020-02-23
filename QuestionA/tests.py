import unittest
from Overlap import Overlap


class OverlapTest(unittest.TestCase):
    def test_overlap_false(self):
        overlap = Overlap([1, 2], [3, 4])
        self.assertFalse(overlap.is_iverlap())
        overlap = Overlap([1, 1], [2, 2])
        self.assertFalse(overlap.is_iverlap())
        overlap = Overlap([0, 1], [2, 4])
        self.assertFalse(overlap.is_iverlap())
        overlap = Overlap([-1, 2], [3, 4])
        self.assertFalse(overlap.is_iverlap())
        overlap = Overlap([-2, 0], [1, 4])
        self.assertFalse(overlap.is_iverlap())
        overlap = Overlap([-5, -3], [-2, -1])
        self.assertFalse(overlap.is_iverlap())
        overlap = Overlap([0, 0], [4, 0])
        self.assertFalse(overlap.is_iverlap())

    def test_overlap_true(self):
        overlap = Overlap([1, 4], [3, 4])
        self.assertTrue(overlap.is_iverlap())
        overlap = Overlap([1, 2], [2, 2])
        self.assertTrue(overlap.is_iverlap())
        overlap = Overlap([-8, -3], [-5, -1])
        self.assertTrue(overlap.is_iverlap())
        overlap = Overlap([-5, 6], [1, 2])
        self.assertTrue(overlap.is_iverlap())
        overlap = Overlap([0, 0], [0, 0])
        self.assertTrue(overlap.is_iverlap())


if __name__ == "__main__":
    unittest.main()
