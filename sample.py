from quiz import DataCapture


def sample():
    batch = [3, 9, 3, 4, 6]

    # Collect data
    capture = DataCapture()
    for v in batch:
        # v must be between 0 and 1000.
        capture.add(v)

    # Prepare a summary of the data
    stats1 = capture.build_stats()

    # Inspect the summary
    print('collection: ' + str(batch))
    print('between(3, 6): %d' % stats1.between(3, 6))  # should return 4 (3, 3, 4 and 6 are between 3 and 6)

    # Continue collecting data
    additional_value = 7
    capture.add(additional_value)

    # Inspect the data now that it has been updated
    stats2 = capture.build_stats()

    # At that point, both summaries stats1 and stats2 are available for inspection.
    print('collection: ' + str(batch + [additional_value]))


sample()

