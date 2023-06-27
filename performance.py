# Validate that the build_stats() function in DataCapture run at constant time O(1)

from quiz.collect import DataCapture
import random
import datetime


HIGHEST_VALUE = 999


def snippet(number_of_add):
    capture = DataCapture()
    for _ in range(number_of_add):
        capture.add(random.randint(0, HIGHEST_VALUE))
    capture.build_stats()


def measure_build_stats(capture):
    start_time = datetime.datetime.now()
    for _ in range(1000):
        capture.build_stats()
    end_time = datetime.datetime.now()
    return end_time - start_time


def validate_build_stats_in_constant_time():
    test_runs = [1_000, 10_000, 100_000, 1000_000]

    # Prepare a test load with N captures before getting the statistics. Increase N by ten fold between runs
    for number_of_capture in test_runs:
        capture = DataCapture()
        for _ in range(number_of_capture):
            capture.add(random.randint(0, HIGHEST_VALUE))
        t = measure_build_stats(capture)
        print(t)


if __name__ == '__main__':
    validate_build_stats_in_constant_time()
