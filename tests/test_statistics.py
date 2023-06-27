import unittest
import copy

from quiz.collect import DataCapture, Statistics

HIGHEST_VALUE = 999


# Factorize the set-up code in a single place for all tests
class BaseCase(unittest.TestCase):
    def setUp(self):
        self.capture = DataCapture()

    def build(self, sample):
        for v in sample:
            self.capture.add(v)


class Between(BaseCase):
    def test_boundary_with_0_collect(self):
        stats = self.capture.build_stats()

        self.assertEqual(stats.between(0), 0)
        self.assertEqual(stats.between(HIGHEST_VALUE), 0)

    def test_value_recorded(self):
        # Check whether a data capture is properly reported by all statistics functions where it is supposed to be

        # Set all the bins to 1 occurrence
        for v in range(0, HIGHEST_VALUE):
            self.capture.add(v)

        # Set one of the bin to 3 occurrences
        v = 100
        self.capture.add(v)
        self.capture.add(v)

        stats = self.capture.build_stats()

        self.assertEqual(stats.between(v, v), 3)

    def test_boundaries(self):
        # capture values that are at the boundary. Then check out the interval at the boundary
        sampling = [0, HIGHEST_VALUE]
        for v in sampling:
            self.capture.add(v)
            stats = self.capture.build_stats()
            self.assertEqual(stats.between(v, v), 1)
        self.assertEqual(stats.between(0, HIGHEST_VALUE), 2)


class Sample(BaseCase):
    def test_sample_code_file(self):
        batch = [3, 9, 3, 4, 6]

        capture = DataCapture()
        for v in batch:
            capture.add(v)

        stats1 = capture.build_stats()
        self.assertEqual(stats1.between(3, 6), 4)


if __name__ == '__main__':
    unittest.main()
