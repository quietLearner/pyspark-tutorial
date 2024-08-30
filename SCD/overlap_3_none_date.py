# https://stackoverflow.com/questions/64332098/intersection-and-complement-of-multiple-lists-of-ranges
# The complement of a set A contains everything that is not in the set A.
# list of intervals
from datetime import datetime, date


def find_intersections(list, lists):
    maxdate = datetime(datetime.max.year, 1, 1)

    # collect all points first into a set and the into a sorted sequence
    breaks = set()
    for l in lists:
        breaks.update(*l)
    # sort None values to the end
    breaks = sorted(breaks, key=lambda x: (x or maxdate))
    # print("breaks", breaks)

    intersections = []
    index = 0
    # For each interval
    for start, end in list:
        if end is not None:
            # Advance b until it falls into this interval:
            while breaks[index] <= start:
                index += 1
            # Now collect all sub-intervals from
            while index < len(breaks) and (
                breaks[index] <= end if breaks[index] is not None else False
            ):
                intersections.append([start, breaks[index]])
                start = breaks[index]
                index += 1
        elif end is None:  # start 1, end None
            # Advance b until it falls into this interval:
            while breaks[index] <= start:
                index += 1
                if breaks[index] is None:
                    intersections.append([start, breaks[index]])
                    return intersections

            # Now collect all sub-intervals from
            while index < len(breaks) and breaks[index] is not None:
                intersections.append([start, breaks[index]])
                start = breaks[index]
                index += 1

            if breaks[index] is None:
                intersections.append([start, breaks[index]])
                return intersections

    return intersections


a = [[datetime(2020, 1, 7), datetime(2020, 1, 17)]]
b = [
    [datetime(2020, 1, 2), datetime(2020, 1, 5)],
    [datetime(2020, 1, 7), datetime(2020, 1, 12)],
    [datetime(2020, 1, 15), datetime(2020, 1, 19)],
    [datetime(2020, 1, 20), datetime(2020, 1, 28)],
]

lists = [a, b]
print("overlap", find_intersections(a, lists))


a = [[datetime(2020, 1, 7), None]]
b = [
    [datetime(2020, 1, 2), datetime(2020, 1, 5)],
    [datetime(2020, 1, 7), datetime(2020, 1, 12)],
    [datetime(2020, 1, 15), datetime(2020, 1, 19)],
    [datetime(2020, 1, 20), datetime(2020, 1, 28)],
]
lists = [a, b]
print("overlap", find_intersections(a, lists))


a = [[datetime(2020, 1, 7), None]]
b = [
    [datetime(2020, 1, 2), datetime(2020, 1, 5)],
    [datetime(2020, 1, 7), datetime(2020, 1, 12)],
    [datetime(2020, 1, 15), datetime(2020, 1, 19)],
    [datetime(2020, 1, 20), None],
]
lists = [a, b]
print("overlap", find_intersections(a, lists))


a = [[datetime(2020, 1, 1), datetime(2020, 1, 2)]]
b = [
    [datetime(2020, 1, 3), datetime(2020, 1, 5)],
    [datetime(2020, 1, 7), datetime(2020, 1, 12)],
    [datetime(2020, 1, 15), datetime(2020, 1, 19)],
    [datetime(2020, 1, 20), None],
]
lists = [a, b]
print("no overlap", find_intersections(a, lists))
