# https://stackoverflow.com/questions/64332098/intersection-and-complement-of-multiple-lists-of-ranges
# The complement of a set A contains everything that is not in the set A.
# list of intervals
from datetime import datetime, date
from collections import namedtuple


def find_date_intersections(a, lists):
    # collect all endpoints first into a set and the into a sorted sequence
    breaks = set()
    for l in lists:
        for x in l:
            breaks.add(x.start_date)
            breaks.add(x.end_date)

    maxdate = datetime(datetime.max.year, 1, 1)
    breaks = sorted(breaks, key=lambda x: (x or maxdate))
    # print(breaks)

    intersections: list[NT] = []
    index = 0
    for id, start, end in a:
        # print(id, start, end)
        if end is not None:
            # Advance b until it falls into this interval:
            while breaks[index] <= start:
                index += 1
            # Now collect all sub-intervals from
            while index < len(breaks) and (
                breaks[index] <= end if breaks[index] is not None else False
            ):
                intersections.append(NT(id, start, breaks[index]))
                start = breaks[index]
                index += 1
        elif end is None:
            # Advance b until it falls into this interval:
            while breaks[index] <= start:
                index += 1
                if breaks[index] is None:
                    intersections.append(NT(id, start, breaks[index]))
                    return intersections

            # Now collect all sub-intervals from
            while index < len(breaks) and breaks[index] is not None:
                intersections.append(NT(id, start, breaks[index]))
                start = breaks[index]
                index += 1

            if breaks[index] is None:
                intersections.append(NT(id, start, breaks[index]))
                return intersections

    return intersections


NT = namedtuple("NT", ["id", "start_date", "end_date"])

nt1 = NT(1, datetime(2012, 1, 15), datetime(2012, 5, 10))
nt2a = NT(2, datetime(2012, 1, 5), datetime(2012, 9, 15))
nt2b = NT(2, datetime(2012, 9, 15), None)
nt2c = NT(2, datetime(2012, 1, 2), None)
nt2d = NT(3, datetime(2012, 1, 2), datetime(2012, 1, 4))
nt2e = NT(3, datetime(2012, 5, 12), datetime(2012, 5, 20))

a = [nt1]
b = [nt2a]

lists = [a, b]
intersections = find_date_intersections(a, lists)
print("case 1, overlap", intersections)

a = [nt1]
b = [nt2b]

lists = [a, b]
intersections = find_date_intersections(a, lists)
print("case 2, no overlap", intersections)


a = [nt1]
b = [nt2c]

lists = [a, b]
intersections = find_date_intersections(a, lists)
print("case 3, no overlap", intersections)

a = [nt1]
b = [nt2d]

lists = [a, b]
intersections = find_date_intersections(a, lists)
print("case 4, no overlap", intersections)

a = [nt1]
b = [nt2e]

lists = [a, b]
intersections = find_date_intersections(a, lists)
print("case 5, no overlap", intersections)


nt1 = NT(1, datetime(2012, 1, 15), None)
nt2a = NT(2, datetime(2012, 1, 5), datetime(2012, 9, 15))
nt2b = NT(2, datetime(2012, 9, 15), None)
nt2c = NT(2, datetime(2012, 1, 2), None)
nt2d = NT(3, datetime(2012, 1, 2), datetime(2012, 1, 4))
nt2e = NT(3, datetime(2012, 5, 12), datetime(2012, 5, 20))


a = [nt1]
b = [nt2a]

lists = [a, b]
intersections = find_date_intersections(a, lists)
print("case 6, overlap", intersections)

a = [nt1]
b = [nt2b]

lists = [a, b]
intersections = find_date_intersections(a, lists)
print("case 7, overlap", intersections)


a = [nt1]
b = [nt2c]

lists = [a, b]
intersections = find_date_intersections(a, lists)
print("case 8, overlap", intersections)

a = [nt1]
b = [nt2d]

lists = [a, b]
intersections = find_date_intersections(a, lists)
print("case 9, no overlap", intersections)

a = [nt1]
b = [nt2e]

lists = [a, b]
intersections = find_date_intersections(a, lists)
print("case 10, overlap", intersections)
