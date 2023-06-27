import unittest
from quiz.collect import DataCapture

HIGHEST_VALUE = 999


# Factorize the set-up code in a single place for all tests
class BaseCase(unittest.TestCase):
    def setUp(self):
        self.capture = DataCapture()


class Add(BaseCase):
    def test_value_lower_than_lower_boundary(self):
        self.assertRaises(AssertionError, self.capture.add, -1)

    def test_value_greater_than_upper_boundary(self):
        self.assertRaises(AssertionError, self.capture.add, 1001)

    def test_value_recorded(self):
        # Check whether a sample capture is recorded where it is expected
        sampling = [100]

        for v in sampling:
            self.capture.add(v)
            stats = self.capture.build_stats()

            self.assertEqual(stats.between(v, v), 1)


if __name__ == '__main__':
    unittest.main()


