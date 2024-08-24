# https://stackoverflow.com/questions/64332098/intersection-and-complement-of-multiple-lists-of-ranges

# The complement of a set A contains everything that is not in the set A.

# list of intervals
a = [[0, 2], [5, 10], [13, 23], [24, 25]]
b = [[1, 5], [8, 12], [15, 18], [20, 24]]

lists = [a, b]

# collect all points first into a set and the into a sorted sequence
breaks = set()
for l in lists:
    for i in l:
        breaks.update(i)
breaks = sorted(breaks)

# first sort all the points, and save into a set
# [0, 1, 2, 5, 8, 10, 12, 13, 15, 18, 20, 23, 24, 25]
print(breaks)


for l in lists:
    output = []
    b = 0
    # For each interval
    for start, end in l:
        # Advance b until it falls into this interval:
        while breaks[b] <= start:
            b += 1
        # Now collect all sub-intervals from
        while b < len(breaks) and breaks[b] <= end:
            output.append([start, breaks[b]])
            start = breaks[b]
            b += 1
    print(output)
