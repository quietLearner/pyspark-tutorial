# https://stackoverflow.com/questions/64332098/intersection-and-complement-of-multiple-lists-of-ranges
# The complement of a set A contains everything that is not in the set A.
# list of intervals


def find_intersections(list, lists):

    # collect all points first into a set and the into a sorted sequence
    breaks = set()
    for l in lists:
        breaks.update(*l)
    # sort None values to the end
    breaks = sorted(breaks, key=lambda x: (x is None, x))

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


a = [[120, 130]]
b = [[3, 5], [8, 12], [15, 18], [20, 100]]
c = [[4, 6], [12, 14], [21, 23], [28, 40]]

lists = [a, b, c]
print("no overlap", find_intersections(a, lists))


a = [[1, 2]]
b = [[3, 5], [8, 12], [15, 18], [20, 100]]
c = [[4, 6], [12, 14], [21, 23], [28, 40]]

lists = [a, b, c]
print("no overlap", find_intersections(a, lists))


a = [[1, 20]]
b = [[3, 5], [8, 12], [15, 18], [20, 100]]
c = [[4, 6], [12, 14], [21, 23], [28, 40]]

lists = [a, b, c]
print("overlap", find_intersections(a, lists))


a = [[1, 120]]
b = [[3, 5], [8, 12], [15, 18], [20, 100]]
c = [[4, 6], [12, 14], [21, 23], [28, 40]]

lists = [a, b, c]
print("overlap", find_intersections(a, lists))


a = [[7, 120]]
b = [[3, 5], [8, 12], [15, 18], [20, 100]]
c = [[4, 6], [12, 14], [21, 23], [28, 40]]

lists = [a, b, c]
print("overlap", find_intersections(a, lists))


a = [[7, 20]]
b = [[3, 5], [8, 12], [15, 18], [20, 100]]
c = [[4, 6], [12, 14], [21, 23], [28, 40]]

lists = [a, b, c]
print("overlap", find_intersections(a, lists))


print("*" * 100)

a = [[120, 130]]
b = [[3, 5], [8, 12], [15, 18], [20, 100]]
c = [[4, 6], [12, 14], [21, 23], [28, None]]

lists = [a, b, c]
print("no overlap, end of lists is None", find_intersections(a, lists))


a = [[1, 2]]
b = [[3, 5], [8, 12], [15, 18], [20, None]]
c = [[4, 6], [12, 14], [21, 23], [28, 40]]

lists = [a, b, c]
print("no overlap, end of lists is None", find_intersections(a, lists))


a = [[1, 20]]
b = [[3, 5], [8, 12], [15, 18], [20, 100]]
c = [[4, 6], [12, 14], [21, 23], [28, None]]

lists = [a, b, c]
print("overlap, end of lists is None", find_intersections(a, lists))


a = [[1, 120]]
b = [[3, 5], [8, 12], [15, 18], [20, None]]
c = [[4, 6], [12, 14], [21, 23], [28, 40]]

lists = [a, b, c]
print("overlap, end of lists is None", find_intersections(a, lists))


a = [[7, 120]]
b = [[3, 5], [8, 12], [15, 18], [20, 100]]
c = [[4, 6], [12, 14], [21, 23], [28, None]]

lists = [a, b, c]
print("overlap, end of lists is None", find_intersections(a, lists))


a = [[7, 20]]
b = [[3, 5], [8, 12], [15, 18], [20, None]]
c = [[4, 6], [12, 14], [21, 23], [28, 40]]

lists = [a, b, c]
print("overlap, end of lists is None", find_intersections(a, lists))

print(
    "#####################################################################################################"
)

a = [[120, None]]
b = [[3, 5], [8, 12], [15, 18], [20, 100]]
c = [[4, 6], [12, 14], [21, 23], [28, 40]]

lists = [a, b, c]
print("no overlap, end is None", find_intersections(a, lists))


a = [[1, None]]
b = [[3, 5], [8, 12], [15, 18], [20, 100]]
c = [[4, 6], [12, 14], [21, 23], [28, 40]]

lists = [a, b, c]
print("overlap, end is None", find_intersections(a, lists))


a = [[7, None]]
b = [[3, 5], [8, 12], [15, 18], [20, 100]]
c = [[4, 6], [12, 14], [21, 23], [28, 40]]

lists = [a, b, c]
print("overlap, end is None", find_intersections(a, lists))


print("*" * 100)
a = [[120, None]]
b = [[3, 5], [8, 12], [15, 18], [20, None]]
c = [[4, 6], [12, 14], [21, 23], [28, 40]]

lists = [a, b, c]
print("overlap, both have None", find_intersections(a, lists))


a = [[1, None]]
b = [[3, 5], [8, 12], [15, 18], [20, 100]]
c = [[4, 6], [12, 14], [21, 23], [28, None]]

lists = [a, b, c]
print("overlap, both have None", find_intersections(a, lists))


a = [[7, None]]
b = [[3, 5], [8, 12], [15, 18], [20, None]]
c = [[4, 6], [12, 14], [21, 23], [28, 40]]

lists = [a, b, c]
print("overlap, both have None", find_intersections(a, lists))
