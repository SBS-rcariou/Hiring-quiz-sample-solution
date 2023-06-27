"""
The _DataCapture_ class allows capturing a large volume of small positive integers.
Once captured, the Statistics class allows to inspect the data distribution across intervals.
"""

__all__ = ['Statistics', 'DataCapture']

HIGHEST_VALUE = 999    # upper boundary for any collected values


class Statistics:
    """
    The statistics functions accept values between 0 and n, n set by default to 999
    """

    def __init__(self, bins, from_factory=False):
        def accumulate(histogram):
            # This function is similar to numpy.cumsum() which could be used instead for faster performance.

            # Build a cumulative sum of all frequencies on the left of index i, for all indices.
            accumulator = 0
            cumulative_sum = []
            for v in histogram:
                accumulator += v
                cumulative_sum.append(accumulator)

            return cumulative_sum

        # Walk the bins from left to right
        self._cum_sum_left = accumulate(bins)

    def between(self, lower, upper):
        """
        Inspect an arbitrary interval [lower, upper]
        :param lower: positive integer
        :param upper: positive integer
        :return: the sum of frequencies of all values in the interval
        """
        assert 0 <= lower <= upper <= HIGHEST_VALUE
        
        sum_0_to_upper = self._cum_sum_left[upper]

        # If the interval does not exist, the cumulative sum would be 0, as none of the values collected are negative.
        sum_0_to_lower = self._cum_sum_left[lower - 1] if lower > 0 else 0

        # Remove [0..lower) from [0..upper] to get [lower..upper]
        return sum_0_to_upper - sum_0_to_lower


class DataCapture:
    """
    Captures a large amount of integers, and inspect them from time to time.
    """
    def __init__(self):
        # Starts with 0 occurrences for all possibles values
        self._bins = [0 for _ in range(0, HIGHEST_VALUE + 1)]

    def add(self, value):
        """
        Aggregate the values to a local store, a fixed-sized memory structure. Accept an unbounded number of values.
        :param value: an integer in a range set by default to 0..999. See the constants HIGHEST_VALUE
        :return: nothing
        """
        assert 0 <= value <= HIGHEST_VALUE

        self._bins[value] += 1

    def build_stats(self):
        """
        Take a snapshot of the data already captured. Data collection can resume after calling this function.
        :return: a Statistics object
        """

        return Statistics(self._bins, from_factory=True)

