from datetime import datetime
from collections import namedtuple

Range = namedtuple("Range", ["start", "end"])

r1 = Range(start=datetime(2012, 1, 15), end=datetime(2012, 5, 10))

r2 = Range(start=datetime(2012, 3, 20), end=datetime(2012, 9, 15))

r3 = Range(start=datetime(2012, 3, 15), end=None)

r4 = Range(start=datetime(2012, 4, 20), end=datetime(2012, 9, 15))

r5 = Range(start=datetime(2012, 2, 15), end=None)

r6 = Range(start=datetime(2012, 3, 20), end=None)


def is_overlap(r1, r2):

    latest_start = max(r1.start, r2.start)

    if r1.end and r2.end:
        earliest_end = min(r1.end, r2.end)
    elif r1.end:
        earliest_end = r1.end
    elif r2.end:
        earliest_end = r2.end
    else:
        earliest_end = None

    return latest_start < earliest_end if earliest_end else True


assert is_overlap(r1, r2), f"failed, {r1} does notoverlap {r2}"

assert is_overlap(r3, r4), f"failed, {r1} does notoverlap {r2}"

assert is_overlap(r5, r6), f"failed, {r1} does notoverlap {r2}"
